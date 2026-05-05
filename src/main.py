from site_generator import clean_up_folder, copy_static_to_public, generate_page

PUBLIC_PATH = "public/"
STATIC_PATH = "static/"
from_path = "content/index.md"
template_path = "template.html"
dest_path = "public/index.html"


def main():
    clean_up_folder(PUBLIC_PATH)
    copy_static_to_public(STATIC_PATH, PUBLIC_PATH)
    generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()
