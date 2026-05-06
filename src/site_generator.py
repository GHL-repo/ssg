import os
import shutil
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    current_path = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)

    for entry in current_path.iterdir():
        if entry.is_file() and entry.suffix.lower() == ".md":
            new_path = dest_dir_path / entry.relative_to(dir_path_content).with_suffix(
                ".html"
            )
            generate_page(entry, template_path, new_path)
        elif entry.is_dir():
            new_dest = dest_dir_path / entry.name
            generate_pages_recursive(entry, template_path, new_dest)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f_md = open(from_path, "r")
    markdown = f_md.read()
    f_md.close()

    f_tmpl = open(template_path, "r")
    template = f_tmpl.read()
    f_tmpl.close()

    node = markdown_to_html_node(markdown)
    content = node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown):
    title = ""

    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            title = line[2:]
            title = title.strip()
            return title

    raise ValueError("no title found")


def clean_up_folder(current_path):
    if os.path.exists(current_path):
        dir_list = os.listdir(current_path)
        for item in dir_list:
            item_path = os.path.join(current_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                # print(f"{item_path} deleted")
            else:
                shutil.rmtree(item_path)
                # print(f"{item_path} deleted")


def copy_static_to_public(current_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    dir_list = os.listdir(current_path)
    for item in dir_list:
        item_path = os.path.join(current_path, item)
        item_dst = os.path.join(target_path, item)

        item_path = os.path.join(current_path, item)
        if os.path.isfile(item_path):
            # print("copying ", item_path, " to ", item_dst)
            shutil.copy(item_path, item_dst)
        else:
            # print("entering folder: ", item_path)
            copy_static_to_public(item_path, item_dst)
