import re

from textnode import TextNode, TextType


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    extracted_imgs = re.findall(pattern, text)
    return extracted_imgs


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"\[([^\]]*)\]\(([^)]+)\)"
    extracted_links = re.findall(pattern, text)
    return extracted_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes : list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sub_new_nodes = []
        node_imgs = extract_markdown_images(node.text)
        if not node_imgs:
            new_nodes.append(node)
            continue
        new_text = node.text
        for img in node_imgs:
            alt_text, link = img[0], img[1]
            split_text = new_text.split(f"![{alt_text}]({link})", 1)
            if not split_text[0]:
                sub_new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
                new_text = split_text[1]
                continue
            sub_new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            sub_new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
            new_text = split_text[1]
        if new_text:
            sub_new_nodes.append(TextNode(new_text, TextType.TEXT))
        new_nodes.extend(sub_new_nodes)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes : list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sub_new_nodes = []
        node_imgs = extract_markdown_links(node.text)
        if not node_imgs:
            new_nodes.append(node)
            continue
        new_text = node.text
        for img in node_imgs:
            alt_text, link = img[0], img[1]
            split_text = new_text.split(f"[{alt_text}]({link})", 1)
            if not split_text[0]:
                sub_new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                new_text = split_text[1]
                continue
            sub_new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            sub_new_nodes.append(TextNode(alt_text, TextType.LINK, link))
            new_text = split_text[1]
        if new_text:
            sub_new_nodes.append(TextNode(new_text, TextType.TEXT))
        new_nodes.extend(sub_new_nodes)
    return new_nodes