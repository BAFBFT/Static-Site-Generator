
class HTMLNode:
    def __init__(self, tag=None, value=None, children=list|None, props=dict|None):
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