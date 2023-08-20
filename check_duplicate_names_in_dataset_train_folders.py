import os
import numpy as np
import time
import shutil

ROOT_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET"





for dataset in os.listdir(ROOT_PATH):

    dataset_path = os.path.join(ROOT_PATH, dataset)
    dataset_images_path = os.path.join(dataset_path, "train", "images")
    dataset_dest_path = os.path.join(dataset_path, "train", "images_no_name_duplicates")
    os.makedirs(dataset_dest_path, exist_ok=True)


    start = time.time()


    #O(n)

    saved_names = dict()
    saved_names_full_path = []
    for current_name in os.listdir(dataset_images_path):
        current_name_actual = current_name.split(".rf")[0]
        try:
            x = saved_names[current_name_actual]
        except:
            saved_names[current_name_actual] = 1
            saved_names_full_path.append(os.path.join(dataset_images_path, current_name))

    print(len(saved_names_full_path))


    for current_path in saved_names_full_path:
        shutil.copy(current_path, dataset_dest_path)


    print(f"Time taken: {time.time() - start}")

