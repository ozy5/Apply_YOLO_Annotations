import os
import shutil
import random

n=36

DATASET_ROOT_PATH = "/home/umut/Desktop/ANNOTATED_DRONE_AIRCRAFT_HELICOPTER_AKONS"

DATASET_DEST_PATH = "/home/umut/Desktop/36_PARTS_DATASET"

for i in range(n):
    os.makedirs(os.path.join(DATASET_DEST_PATH, "part_" + str(i)), exist_ok=True)

datasets = os.listdir(DATASET_ROOT_PATH)

for dataset in datasets:
    current_dataset_path = os.path.join(DATASET_ROOT_PATH, dataset)
    datasets_sub_folder = os.listdir(current_dataset_path)

    for sub_folder in datasets_sub_folder:
        current_dataset_sub_folder_path = os.path.join(current_dataset_path, sub_folder)
        current_dataset_sub_folder_images = os.listdir(current_dataset_sub_folder_path)

        current_dataset_sub_folder_images_count = len(current_dataset_sub_folder_images)

        number_to_divide = current_dataset_sub_folder_images_count / n

        #random.shuffle(current_dataset_sub_folder_images)
        current_dataset_sub_folder_images.sort()

        merged_dataset_path = os.path.join(dataset, sub_folder)

        for i in range(n):
            os.makedirs(os.path.join(DATASET_DEST_PATH, "part_" + str(i), merged_dataset_path), exist_ok=True)



        for ind, image in enumerate(current_dataset_sub_folder_images):
            current_image_path = os.path.join(current_dataset_sub_folder_path, image)

            dataset_no = int(ind // number_to_divide)

            shutil.copy(current_image_path, os.path.join(DATASET_DEST_PATH, "part_" + str(dataset_no), merged_dataset_path))














