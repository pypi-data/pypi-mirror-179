# -*- coding: utf-8 -*-
import errno
import logging
from pathlib import Path
from typing import Optional
from uuid import UUID
from xmlrpc.client import Boolean

from apistar.exceptions import ErrorResponse
from arkindex import ArkindexClient
from lxml import etree as ET
from lxml import objectify
from rich.progress import Progress, track

from arkindex_cli.argtypes import URLArgument
from arkindex_cli.auth import Profiles
from arkindex_cli.commands.upload.alto.parser import AltoElement, RootAltoElement

logger = logging.getLogger(__name__)


def add_alto_parser(subcommands):
    parser = subcommands.add_parser(
        "alto",
        description="Upload ALTO XML documents to Arkindex.",
        help="Upload ALTO XML documents to Arkindex.",
    )
    parser.add_argument(
        "path",
        help="Path to a directory which contains ALTO XML documents. Defaults to the current working directory.",
        type=Path,
        default=Path.cwd(),
    )
    parser.add_argument(
        "--iiif-base-url",
        help="Base URL for the IIIF images, which will be prepended to all source image file names.",
        type=URLArgument(allow_query=False),
        required=True,
    )
    parser.add_argument(
        "--parent-id",
        help="UUID of a parent folder under which page elements will be created.",
        type=UUID,
        required=True,
    )
    types = parser.add_mutually_exclusive_group(required=True)
    types.add_argument(
        "--create-types",
        help="Create an element type in the Arkindex corpus for each element type in the ALTO files.",
        action="store_true",
    )
    types.add_argument(
        "--existing-types",
        help='Specify correspondences between element types in the Arkindex corpus and in the ALTO files. Format: --existing-types="alto_type:arkindex_type alto_type_2:arkindex_type_2"',
        type=str,
    )
    parser.set_defaults(func=run)


def check_element_type(corpus: dict, type_slug: str) -> None:
    types = {type["slug"] for type in corpus["types"]}
    if type_slug not in types:
        raise ValueError(f"Type {type_slug} not found.")
    return True


def create_iiif_image(client: ArkindexClient, url: str) -> str:
    try:
        image = client.request("CreateIIIFURL", body={"url": url})
        return image["id"]
    except ErrorResponse as e:
        # When the image already exists, its ID is returned in a HTTP 400
        if e.status_code == 400 and "id" in e.content:
            return e.content["id"]
        raise


def get_element_type(
    client: ArkindexClient,
    corpus_id: UUID,
    node_name: str,
    types_dict: Optional[dict],
    create_types: Boolean = False,
):
    """
    Retrieve or create an alto node's corresponding Arkindex element type.
    """
    arkindex_corpus_types = [
        item["slug"] for item in client.request("RetrieveCorpus", id=corpus_id)["types"]
    ]
    if types_dict is not None:
        if node_name not in types_dict:
            logger.info(
                f"Skipping alto element {node_name}: not in given types dictionary."
            )
        else:
            return types_dict[node_name]
    elif create_types:
        if node_name not in arkindex_corpus_types:
            logger.info(
                f"Creating element type {node_name} in target corpus {corpus_id}…"
            )
            try:
                client.request(
                    "CreateElementType",
                    body={
                        "slug": node_name,
                        "display_name": node_name,
                        "corpus": corpus_id,
                    },
                )
            except ErrorResponse as e:
                logger.error(
                    f"Failed to create element type {node_name} in target corpus {corpus_id}."
                )
                raise Exception(e.content)
        else:
            logger.info(
                f"Element type {node_name} exists in target corpus {corpus_id}."
            )
        return node_name


def create_elements(
    client, item, image_id, element_name, corpus, parent_id, types_dict, create_types
):
    # Specific handling of the Page node, which is the "base" element created from the
    # image on Arkindex, and which is parent to all other elements.
    if type(item) == AltoElement and item.node_name == "page":
        page_node = item
        # For page nodes, a polygon can be defined by WIDTH, HEIGHT, V_POS and H_POS
        # like other nodes, or from WIDTH and HEIGHT only.
        if page_node.polygon:
            page_polygon = page_node.polygon
        else:
            page_polygon = [
                [0, 0],
                [0, page_node.height],
                [page_node.width, page_node.height],
                [page_node.width, 0],
                [0, 0],
            ]
        logger.info(f"Creating page {element_name}…")
        page = client.request(
            "CreateElement",
            body={
                "corpus": corpus["id"],
                "parent": str(parent_id),
                "type": get_element_type(
                    client,
                    corpus["id"],
                    page_node.node_name,
                    types_dict,
                    create_types,
                ),
                "name": element_name,
                "image": image_id,
                "polygon": page_polygon,
            },
            slim_output=True,
        )
        page_subelements = page_node.serialized_children
        for subelement in page_subelements:
            create_elements(
                client,
                subelement,
                image_id,
                None,
                corpus,
                page["id"],
                types_dict,
                create_types,
            )
    elif type(item) == dict:
        if "polygon" in item:
            base_dict = item.copy()
            base_dict.pop("children")
            base_dict.pop("text", None)
            element_name = "0"
            if "name" in base_dict:
                element_name = base_dict["name"]
            element_type = get_element_type(
                client, corpus["id"], base_dict["type"], types_dict, create_types
            )
            if element_type:
                element_body = {
                    "type": element_type,
                    "name": element_name,
                    "parent": parent_id,
                    "corpus": corpus["id"],
                    "image": image_id,
                    "polygon": base_dict["polygon"],
                }
                logger.info(f"Creating {element_type} {element_name}…")
                created_element = client.request(
                    "CreateElement", body=element_body, slim_output=True
                )
                parent_element_id = created_element["id"]

                # Create transcription if there is one
                if "text" in item:
                    transcription_body = {"text": item["text"]}
                    logger.info(
                        f"Creating transcription {item['text']} for {element_type} {element_name}…"
                    )
                    client.request(
                        "CreateTranscription",
                        id=created_element["id"],
                        body=transcription_body,
                    )
            else:
                parent_element_id = parent_id
        if len(item["children"]) > 0:
            for child in item["children"]:
                create_elements(
                    client,
                    child,
                    image_id,
                    None,
                    corpus,
                    parent_element_id,
                    types_dict,
                    create_types,
                )


def upload_alto_file(
    path: Path,
    client: ArkindexClient,
    iiif_base_url: str,
    corpus: dict,
    parent_id: UUID,
    types_dict: Optional[dict],
    create_types: Boolean,
) -> None:
    with open(path) as file:
        # This ensures that comments in the XML files do not cause the
        # "no Alto namespace found" exception.
        parser = ET.XMLParser(remove_comments=True)
        tree = objectify.parse(file, parser=parser)
        root = RootAltoElement(tree.getroot())

    # Skip empty files immediately
    if not len(root.content):
        logger.warning(f"No content found in file {path}")
        return

    page_nodes = root.content.findall(".//alto:Page", namespaces=root.namespaces)
    if len(page_nodes) == 1:
        # We use + here and not urljoin or path.join to create image URLs
        # because the base URL could contain a portion of the identifier:
        # 'http://server/iiif/root%2Fdirectory'
        # urljoin or path.join would erase that identifier prefix.
        image_id = create_iiif_image(client, iiif_base_url + root.filename)
        page_name = root.filename
        page_node = AltoElement(page_nodes[0])
        page_node.parse_children()
        create_elements(
            client,
            page_node,
            image_id,
            page_name,
            corpus,
            parent_id,
            types_dict,
            create_types,
        )
    elif len(page_nodes) > 1:
        for page_node in page_nodes:
            page_node = AltoElement(page_node)
            if page_node.page_image_id is None:
                logger.warning(
                    "Attribute PHYSICAL_IMG_NR was not set for this Page node. Skipping…"
                )
                return
            image_id = create_iiif_image(
                client, iiif_base_url + page_node.page_image_id
            )
            page_name = page_node.name
            create_elements(
                client,
                page_node,
                image_id,
                page_name,
                corpus,
                parent_id,
                types_dict,
                create_types,
            )
    else:
        logger.warning(f"No Page node found in file {root.filename}. Skipping…")
        return


def run(
    path: Path,
    iiif_base_url: str,
    parent_id: UUID,
    create_types: Boolean,
    existing_types: Boolean,
    profile_slug: Optional[str] = None,
) -> int:
    with Progress(transient=True) as progress:
        progress.add_task(start=False, description="Loading API client")
        client = Profiles().get_api_client_or_exit(profile_slug)

    if not path.is_dir():
        logger.error(f"{path} is not a directory.")
        return errno.ENOTDIR

    file_paths = list(path.glob("*.xml"))
    if not file_paths:
        logger.error(f"No XML files found in {path}.")

    with Progress(transient=True) as progress:
        progress.add_task(start=False, description="Fetching parent element")
        try:
            parent = client.request("RetrieveElement", id=parent_id)
        except ErrorResponse as e:
            logger.error(
                f"Could not retrieve parent element {parent_id}: HTTP {e.status_code} - {e.content}"
            )
            return errno.EREMOTEIO

    with Progress(transient=True) as progress:
        progress.add_task(start=False, description="Fetching corpus")
        corpus_id = parent["corpus"]["id"]
        try:
            corpus = client.request("RetrieveCorpus", id=corpus_id)
        except ErrorResponse as e:
            logger.error(
                f"Could not retrieve corpus {corpus_id}: HTTP {e.status_code} - {e.content}"
            )
            return errno.EREMOTEIO

    types_dict = None
    if existing_types:
        split_str = existing_types.split(" ")
        types_dict = {}
        for item in split_str:
            split_item = item.split(":")
            types_dict[str(split_item[0]).lower()] = str(split_item[1]).lower()
        for key, arkindex_type in types_dict.items():
            try:
                check_element_type(corpus, arkindex_type)
            except ValueError as e:
                logger.error(str(e))
                return errno.EINVAL

    failed = 0
    for file_path in track(file_paths, description="Uploading"):
        try:
            upload_alto_file(
                path=file_path,
                client=client,
                iiif_base_url=iiif_base_url,
                corpus=corpus,
                parent_id=parent_id,
                types_dict=types_dict,
                create_types=create_types,
            )
        except ErrorResponse as e:
            logger.error(
                f"Upload failed for file {file_path}: HTTP {e.status_code} - {e.content}"
            )
            failed += 1
        except Exception as e:
            logger.error(f"Upload failed for file {file_path}: {e!r}")
            failed += 1

    # Return a non-zero error code when all files have failed
    return failed >= len(file_paths)
