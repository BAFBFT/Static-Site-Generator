import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdowntoHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list_with_links_bold_and_italics(self):
        md = """
- Item with a [link](https://example.com)
- Item with **bold** text
- Item with _italic_ text and `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul>'
            '<li>Item with a <a href="https://example.com">link</a></li>'
            "<li>Item with <b>bold</b> text</li>"
            "<li>Item with <i>italic</i> text and <code>code</code></li>"
            "</ul></div>",
        )

    def test_ordered_list_with_inline_formatting(self):
        md = """
1. First **bold** item
2. Second _italic_ item
3. Third with [link](https://boot.dev)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol>"
            "<li>First <b>bold</b> item</li>"
            "<li>Second <i>italic</i> item</li>"
            '<li>Third with <a href="https://boot.dev">link</a></li>'
            "</ol></div>",
        )

    def test_list_item_with_multiple_links_and_mixed_inline(self):
        md = """
- [a](https://a.com) then [b](https://b.com)
- **bold** plus _italic_ plus [link](https://x.com)
- plain text only
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul>"
            '<li><a href="https://a.com">a</a> then <a href="https://b.com">b</a></li>'
            '<li><b>bold</b> plus <i>italic</i> plus <a href="https://x.com">link</a></li>'
            "<li>plain text only</li>"
            "</ul></div>",
        )

    def test_all_heading_levels(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading 1</h1>"
            "<h2>Heading 2</h2>"
            "<h3>Heading 3</h3>"
            "<h4>Heading 4</h4>"
            "<h5>Heading 5</h5>"
            "<h6>Heading 6</h6>"
            "</div>",
        )

    def test_heading_with_link_bold_and_italic(self):
        md = """
## Read [the docs](https://docs.example.com) now

### A **bold** and _italic_ heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            '<h2>Read <a href="https://docs.example.com">the docs</a> now</h2>'
            "<h3>A <b>bold</b> and <i>italic</i> heading</h3>"
            "</div>",
        )

    def test_blockquote_multiline_with_inline_markdown(self):
        md = """
> line one with **bold**
> line two with _italic_ and `code`
> line three with [link](https://q.com)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>"
            "line one with <b>bold</b> "
            "line two with <i>italic</i> and <code>code</code> "
            'line three with <a href="https://q.com">link</a>'
            "</blockquote></div>",
        )

    def test_codeblock_does_not_parse_links_or_lists(self):
        md = """
```
- not a list
[not a link](https://x.com) **not bold**
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>- not a list\n"
            "[not a link](https://x.com) **not bold**\n"
            "</code></pre></div>",
        )

    def test_full_document_with_every_block_type(self):
        md = """
# My **Big** Title

Intro paragraph with a [link](https://boot.dev) and _italics_.

- first with [link](https://a.com)
- second with **bold**

1. step one `run`
2. step two _fast_

> quoted **wisdom**
> from [someone](https://s.com)

```
code with [link](https://x.com) and - list
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>My <b>Big</b> Title</h1>"
            '<p>Intro paragraph with a <a href="https://boot.dev">link</a> and <i>italics</i>.</p>'
            "<ul>"
            '<li>first with <a href="https://a.com">link</a></li>'
            "<li>second with <b>bold</b></li>"
            "</ul>"
            "<ol>"
            "<li>step one <code>run</code></li>"
            "<li>step two <i>fast</i></li>"
            "</ol>"
            "<blockquote>quoted <b>wisdom</b> from <a href=\"https://s.com\">someone</a></blockquote>"
            "<pre><code>code with [link](https://x.com) and - list\n</code></pre>"
            "</div>",
        )

    def test_image_in_paragraph_and_list(self):
        # KNOWN FAILURE: text_node_to_html_node builds an img LeafNode with an
        # empty value, and LeafNode.to_html rejects a falsy value, so any block
        # containing an image raises "all leaf nodes must have a value."
        md = """
Look at ![alt text](https://img.com/a.png) here

- ![cat](https://c.com/c.png) caption
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            '<p>Look at <img src="https://img.com/a.png" alt="alt text"> </img> here</p>'
            '<ul><li><img src="https://c.com/c.png" alt="cat"> </img> caption</li></ul>'
            "</div>",
        )

if __name__ == "__main__":
    unittest.main()