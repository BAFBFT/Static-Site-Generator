from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if not isinstance(text_type, TextType):
        raise TypeError(f"invalid text type: {text_type}")
    
    new_nodes : list[TextNode] = []

    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            # odd occurences of delimeter
            if node.text.count(delimiter) % 2 == 1:
                raise ValueError(f"'{node.text}' is invalid Markdown")
            
            node_text_list = node.text.split(delimiter)
            new_from_text_nodes = []
            for i, sub_text in enumerate(node_text_list):
                if sub_text == '':
                    # empty case, don't build node
                    continue
                if i%2==0:
                    new_from_text_nodes.append(TextNode(sub_text, TextType.TEXT))
                else:
                    new_from_text_nodes.append(TextNode(sub_text, text_type))
            new_nodes.extend(new_from_text_nodes)
        else:
            new_nodes.append(node)

    return new_nodes
