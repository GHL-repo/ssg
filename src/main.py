from site_generator import (
    clean_up_folder,
    copy_static_to_public,
    generate_pages_recursive,
)

PUBLIC_PATH = "public/"
STATIC_PATH = "static/"
# from_path = "content/index.md"
# template_path = "template.html"
# dest_path = "public/index.html"
dir_path_content = "content/"
template_path = "template.html"
dest_dir_path = "public/"


def main():
    clean_up_folder(PUBLIC_PATH)
    copy_static_to_public(STATIC_PATH, PUBLIC_PATH)
    # generate_page(from_path, template_path, dest_path)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)


if __name__ == "__main__":
    main()
