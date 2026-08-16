import unittest

from split_delimeter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_split(self):
        # equality tests between 2 nodes
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is text with a ", TextType.TEXT),
                             TextNode("bolded phrase", TextType.BOLD),
                             TextNode(" in the middle", TextType.TEXT)
                             ])

    def test_multiple_split(self):
        node = TextNode("This is text with a **bolded phrase** in the middle and **the end.**",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is text with a ", TextType.TEXT),
                             TextNode("bolded phrase", TextType.BOLD),
                             TextNode(" in the middle and ", TextType.TEXT),
                             TextNode("the end.", TextType.BOLD)
                             ])
    
    def test_delimeter_start(self):
        node = TextNode("**This is text with** a bolded phrase at the start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is text with", TextType.BOLD),
                             TextNode(" a bolded phrase at the start", TextType.TEXT),
                             ])        
        
    def test_invalid_markdown(self):
        # equality tests between 2 nodes
        node = TextNode("This is text with a bolded phrase** in the middle", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()