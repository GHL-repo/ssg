from site_generator import clean_up_folder, copy_static_to_public

PUBLIC_PATH = "./public/"
STATIC_PATH = "./static/"


def main():
    clean_up_folder(PUBLIC_PATH)
    copy_static_to_public(STATIC_PATH, PUBLIC_PATH)


if __name__ == "__main__":
    main()
