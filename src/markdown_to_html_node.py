from block_to_block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def _heading_depth(hashtag_count : int) -> str:
    match hashtag_count:
        case 1:
            return "h1"
        case 2:
            return "h2"
        case 3:
            return "h3"
        case 4:
            return "h4"
        case 5:
            return "h5"
        case 6:
            return "h6"
        case _:
            raise ValueError("hash tag count > 6, invalid heading depth")
        

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes: list[HTMLNode] = list(map(text_node_to_html_node, text_nodes))
    return html_nodes


def paragraph_html(block : str) -> ParentNode:
    cleaned_text = block.replace('\n', ' ')
    html_nodes = text_to_children(cleaned_text.strip())
    parent_node = ParentNode('p', html_nodes)
    return parent_node


def heading_html(block: str) -> ParentNode:
    hashtag_count = len(block.split()[0])
    heading_text = block.split(maxsplit=1)[1]
    tag = _heading_depth(hashtag_count)
    html_nodes = text_to_children(heading_text.strip())
    parent_node = ParentNode(tag, html_nodes)
    return parent_node


# code block should not do any inline markdown parsing
# everything should remain as is, no splitting on delimeters and text types
def code_html(block: str) -> ParentNode:
    # text only
    code_text = block.split("```")[1]
    # text_node --> html_node
    code_text_node = TextNode(code_text.lstrip(), TextType.CODE)
    html_node = text_node_to_html_node(code_text_node)
    parent_node = ParentNode('pre', [html_node])
    return parent_node


def blockquote_html(block: str) -> ParentNode:
    text_lines = block.split('\n')
    cleaned_text_list : list[str] = []
    for line in text_lines:
        # strip '>' from the start of each line
        cleaned_line = line.lstrip('>')
        cleaned_text_list.append(cleaned_line.strip())
    cleaned_text = " ".join(cleaned_text_list)
    html_nodes = text_to_children(cleaned_text)
    parent_node = ParentNode('blockquote', html_nodes)
    return parent_node


def unordered_list_html(block: str) -> ParentNode:
    text_lines = block.split('\n')
    cleaned_text_list : list[str] = []
    for line in text_lines:
        # strip '-' from the start of each line
        cleaned_line = line.lstrip('-')
        cleaned_text_list.append(cleaned_line.strip())
    
    list_items : list[HTMLNode] = []
    # each line represents a list item
    for line in cleaned_text_list:
        html_nodes = text_to_children(line)
        list_item_html_node = ParentNode('li', html_nodes)
        list_items.append(list_item_html_node)
    
    parent_node = ParentNode('ul', list_items)
    return parent_node

def ordered_list_html(block: str) -> ParentNode:
    text_lines = block.split('\n')
    cleaned_text_list : list[str] = []
    for i, line in enumerate(text_lines, 1):
        number = f"{i}."
        # strip '-' from the start of each line
        cleaned_line = line.removeprefix(number)
        cleaned_text_list.append(cleaned_line.strip())
    
    list_items : list[HTMLNode] = []
    # each line represents a list item
    for line in cleaned_text_list:
        html_nodes = text_to_children(line)
        list_item_html_node = ParentNode('li', html_nodes)
        list_items.append(list_item_html_node)
    
    parent_node = ParentNode('ol', list_items)
    return parent_node

def block_to_html_node(block : str, block_type: BlockType) -> ParentNode:
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_html(block)
        case BlockType.HEADING:
            return heading_html(block)
        case BlockType.CODE:
            return code_html(block)
        case BlockType.QUOTE:
            return blockquote_html(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_html(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_html(block)
        case _:
            raise ValueError(f"unknown BlockType: {block_type}")


def block_type_map(blocks: list[str]) -> list[tuple[str, BlockType]]:
    mapped_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        mapped_blocks.append((block, block_type))
    return mapped_blocks


def markdown_to_html_node(markdown : str) -> HTMLNode:
    # 1. Split markdown to blocks
    blocks = markdown_to_blocks(markdown)

    # 2. Determine the block type 
    mapped_blocks = block_type_map(blocks) 
    html_nodes : list[HTMLNode] = []
    # 3. 
    for block, block_type in mapped_blocks:
        child_node = block_to_html_node(block, block_type)
        html_nodes.append(child_node)
    html_block = ParentNode('div', html_nodes)
    return html_block
