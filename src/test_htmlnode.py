import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        # test html repr
        node = HTMLNode("<p>", "yo, I like your cut G", children=None, props=None)
        node_repr = "HTMLNode(<p>, yo, I like your cut G, None, None)"
        self.assertEqual(node.__repr__(), node_repr)


    def test_props_to_html_no_props(self):
        # test empty props
        node = HTMLNode("p", "yo, I like your cut G", children=None, props=None)
        html_repr =''
        self.assertEqual(node.props_to_html(), html_repr)


    def test_props_to_html_string_match(self):
        # test leading and trailing whitespace
        node = HTMLNode("p", "yo, I like your cut s", children=None, 
                        props={
                                "href": "https://www.google.com",
                            }
                        )
        html_repr =' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), html_repr)


    def test_props_to_html_insertion_order(self):
        # test insertion order
        node = HTMLNode("p", "yo, I like your cut G", children=None, 
                        props={
                                "href": "https://www.google.com",
                                "target": "_blank",
                            }
                        )
        html_repr =' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), html_repr)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.__repr__(), "LeafNode(p, Hello, world!, None)")


    def test_leaf_children_is_none(self):
        node = LeafNode("p", "hello")
        self.assertIsNone(node.children)


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),
                        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )        


    def test_parent_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(
            ValueError,
            parent_node.to_html,
        )        
    

    def test_parent_no_tag(self):
        child_node = LeafNode("b", "grandchild")
        parent_node = ParentNode("", [child_node])
        self.assertRaises(
            ValueError,
            parent_node.to_html,
        ) 

if __name__ == "__main__":
    unittest.main()