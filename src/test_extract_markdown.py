import unittest

import extract_markdown


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_md_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extract_markdown.extract_markdown_images(text)

    def test_extract_md_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extract_markdown.extract_markdown_links(text)


if __name__ == "__main__":
    unittest.main()
