import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


HEADING_PATTERN = re.compile(r"#{1,6} .+")
CODE_PATTERN = re.compile(r"```\n[\s\S]*```")
QUOTE_PATTERN = re.compile(r">.*(?:\n>.*)*")
UNORDERED_LIST_PATTERN = re.compile(r"- .*(?:\n- .*)*")
ORDERED_LIST_PATTERN = re.compile(r"\d+\. .*(?:\n\d+\. .*)*")
ORDERED_ITEM_PATTERN = re.compile(r"(\d+)\. ")


def is_ordered_list(block: str) -> bool:
    if not ORDERED_LIST_PATTERN.fullmatch(block):
        return False
    for expected, line in enumerate(block.split("\n"), start=1):
        if int(ORDERED_ITEM_PATTERN.match(line).group(1)) != expected: # type: ignore
            return False
    return True


def block_to_block_type(block: str) -> BlockType:
    match block:
        case _ if HEADING_PATTERN.fullmatch(block):
            return BlockType.HEADING
        case _ if CODE_PATTERN.fullmatch(block):
            return BlockType.CODE
        case _ if QUOTE_PATTERN.fullmatch(block):
            return BlockType.QUOTE
        case _ if UNORDERED_LIST_PATTERN.fullmatch(block):
            return BlockType.UNORDERED_LIST
        case _ if is_ordered_list(block):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
