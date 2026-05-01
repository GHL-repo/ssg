import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "This is a paragraph", None, None)
        node2 = HTMLNode("p", "This is a paragraph", None, None)
        node3 = HTMLNode("a", "This is a link", None, None)
        node4 = HTMLNode("a", "This is a different link", None, None)
        node5 = HTMLNode("p", "This is a paragraph", None, None)
        node6 = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"href": "https://example.com", "target": "_blank"},
        )
        self.assertEqual(node1, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)

    def test_props_to_html(self):
        node7 = HTMLNode(
            "a", "Click", None, {"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node7.props_to_html(), ' href="https://example.com" target="_blank"'
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<b>Hello, world!</b>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
