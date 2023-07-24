import os
import numpy as np
import time
import shutil

ROOT_PATH = "/home/umut/datasets_raw/Roboflow"

SAVE_ROOT_PATH = "/home/umut/dataset_no_duplicate_names"

sub_dirs = os.listdir(ROOT_PATH)
print(sub_dirs)

all_paths_images = []
all_paths_labels = []


saved_names = dict()
for dir in sub_dirs:
    current_sub_dir = os.path.join(ROOT_PATH, dir)

    
    for sub_sub_dir in os.listdir(current_sub_dir):
        try:
                current_files_path = os.path.join(current_sub_dir, sub_sub_dir)
                current_labels = os.listdir(os.path.join(current_files_path, "labels"))
                for label_name in current_labels:

                    current_file_sole_name = label_name.split(".txt")[0].split(".rf")[0]


                    try:
                        x = saved_names[current_file_sole_name]
                    except:
                        saved_names[current_file_sole_name] = 1

                        current_label_path = os.path.join(current_files_path, "labels", label_name)
                        all_paths_labels.append(current_label_path)

                        current_image_path = os.path.join(current_files_path, "images", label_name.split(".txt")[0] + ".jpg")
                        all_paths_images.append(current_image_path)


        except:
            continue


all_paths_images = np.array(all_paths_images)
all_paths_labels = np.array(all_paths_labels)






os.makedirs("annotated_images_no_duplicates", exist_ok=True)

for img_path, label_path in zip(all_paths_images, all_paths_labels):
    img_split_list = img_path.split("/")
    img_save_dir = os.path.join(SAVE_ROOT_PATH, "/".join(img_split_list[4:8]))
    os.makedirs(img_save_dir, exist_ok=True)
    shutil.copy(img_path, img_save_dir)

    label_split_list = label_path.split("/")
    label_save_dir = os.path.join(SAVE_ROOT_PATH, "/".join(label_split_list[4:8]))
    os.makedirs(label_save_dir, exist_ok=True)
    shutil.copy(label_path, label_save_dir)













