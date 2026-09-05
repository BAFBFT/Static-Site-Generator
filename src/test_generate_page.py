import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """# Hello

This is a paragraph.
"""
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_no_heading(self):
        md = """This is a paragraph.

## Not an h1
"""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_multiple_h1(self):
        md = """# First heading

Some text.

# Second heading
"""
        self.assertEqual(extract_title(md), "First heading")


if __name__ == "__main__":
    unittest.main()
