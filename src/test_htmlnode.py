import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        # test fro 
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
        

if __name__ == "__main__":
    unittest.main()