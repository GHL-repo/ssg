import sys

from site_generator import (
    clean_up_folder,
    copy_static_to_public,
    generate_pages_recursive,
)

public_path = "docs/"
static_path = "static/"
content_path = "content/"
template_path = "template.html"

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    clean_up_folder(public_path)
    copy_static_to_public(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path, basepath)


if __name__ == "__main__":
    main()
