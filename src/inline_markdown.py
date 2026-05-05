import re

from textnode import TextNode, TextType


def text_to_textnodes(text):
    initial_text = [TextNode(text, TextType.TEXT)]

    output1 = split_nodes_delimiter(initial_text, "**", TextType.BOLD)
    output2 = split_nodes_delimiter(output1, "`", TextType.CODE)
    output3 = split_nodes_delimiter(output2, "_", TextType.ITALIC)
    output4 = split_nodes_image(output3)
    output5 = split_nodes_link(output4)

    return output5


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter) % 2 == 1:
            raise Exception("Invalid Markdown syntax")
        else:
            split_text = old_node.text.split(delimiter)

            for i, phrase in enumerate(split_text):
                if i % 2 == 0:
                    new_nodes.append(TextNode(phrase, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(phrase, text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted_images = extract_markdown_images(old_node.text)

        if not extracted_images:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text

        for alt, url in extracted_images:
            delimiter = f"![{alt}]({url})"
            split_text = current_text.split(delimiter, 1)

            if len(split_text) != 2:
                raise ValueError("malformed markdown")

            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            current_text = split_text[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted_links = extract_markdown_links(old_node.text)

        if not extracted_links:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text

        for text, url in extracted_links:
            delimiter = f"[{text}]({url})"
            split_text = current_text.split(delimiter, 1)

            if len(split_text) != 2:
                raise ValueError("malformed markdown")

            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            new_nodes.append(TextNode(text, TextType.LINK, url))

            current_text = split_text[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
