
class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props or self.props == {}:
            return ""
        
        string_repr = ""
        for k, v in self.props.items():
            string_repr += f' {k}="{v}"'
        
        return string_repr

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str | None = None, 
            value : str = "", 
            props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have a value.")
        if not self.tag:
            return self.value
        html_props = super().props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str, 
        children : list["HTMLNode"],
        props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent node must have tag")
        if not self.children:
            raise ValueError("parent node must have children")
        value = "" 
        for child in self.children:
            value += child.to_html()
        html_props = super().props_to_html()

        return f"<{self.tag}{html_props}>{value}</{self.tag}>"