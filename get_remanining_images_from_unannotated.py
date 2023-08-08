import os
import numpy as np
import shutil
from utils.leave_only_the_wanted_class_and_copy_txt import leave_only_the_wanted_class_and_copy_txt
from utils.find_the_dataset_of_the_name import find_the_dataset_of_the_name
from utils.find_the_id_of_class_in_dataset import find_the_id_of_class_in_dataset
import time

start = time.time()

SOURCE_NAME_PATH = "/home/umut/Desktop/random_selected_images"



COPY_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET"



DEST_PATH = "/home/umut/Desktop/remaining_images_speed_test"

DEST_PATH_IMAGES = os.path.join(DEST_PATH, "images")
DEST_PATH_LABELS = os.path.join(DEST_PATH, "labels")

os.makedirs(DEST_PATH_IMAGES, exist_ok=True)
os.makedirs(DEST_PATH_LABELS, exist_ok=True)


all_paths = os.listdir(SOURCE_NAME_PATH)


for image in all_paths:
    image_name_split = image.split(".")


    image_name = ".".join(image_name_split[0:-1])
    image_ext = image_name_split[-1]

    current_dataset_path = find_the_dataset_of_the_name(image_name, COPY_PATH)

    shutil.copy(os.path.join(current_dataset_path, "images", image), DEST_PATH_IMAGES)


    # # copy the original txt file
    #shutil.copy(os.path.join(current_dataset_path, "labels", image_name + ".txt"), DEST_PATH_LABELS)

    current_dataset_path_parent = "/".join(current_dataset_path.split("/")[:-1])

    # find the humans id
    humans_id = [find_the_id_of_class_in_dataset(current_dataset_path_parent, "Person")]


    # copy the txt file that has only the wanted class
    # leave_only_the_wanted_class_and_copy_txt(os.path.join(current_dataset_path, "labels", image_name + ".txt"),
    #                                          os.path.join(DEST_PATH_LABELS, image_name + ".txt"),
    #                                          humans_id)


print(f"Time taken: {time.time() - start}")








