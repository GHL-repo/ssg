from src.textnode import TextNode, TextType


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
