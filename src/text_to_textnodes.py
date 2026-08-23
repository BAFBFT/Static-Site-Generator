import extract_links
import split_delimeter
from textnode import TextNode, TextType

DELIMETERS_TYPE = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}

def text_to_textnodes(text: str):
    node = TextNode(text, TextType.TEXT)
    start_nodes : list[TextNode] = [node]
    # split by delimeter
    for delimeter, texttype in DELIMETERS_TYPE.items():
        start_nodes = split_delimeter.split_nodes_delimiter(start_nodes, delimeter, texttype)
    
    # important to extract images before links, an image would also match the current link identifying logic
    img_extracted_nodes = extract_links.split_nodes_image(start_nodes)
    link_extracted_nodes = extract_links.split_nodes_link(img_extracted_nodes)

    return link_extracted_nodes
