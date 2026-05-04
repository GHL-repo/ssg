import os
import shutil


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
