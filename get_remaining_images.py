import os
import numpy as np
import shutil
from utils.leave_only_the_wanted_class_and_copy_txt import leave_only_the_wanted_class_and_copy_txt
from utils.find_the_dataset_of_the_name import find_the_dataset_of_the_name
from utils.find_the_id_of_class_in_dataset import find_the_id_of_class_in_dataset

SOURCE_NAME_PATH = "/home/umut/Desktop/new_test"

POSTFIX = "_humans_annotated"


COPY_PATH = "/home/umut/datasets_raw/Roboflow"



DEST_PATH = "/home/umut/Desktop/remaining_images_for_new_test"

DEST_PATH_IMAGES = os.path.join(DEST_PATH, "images")
DEST_PATH_LABELS = os.path.join(DEST_PATH, "labels")

os.makedirs(DEST_PATH_IMAGES, exist_ok=True)
os.makedirs(DEST_PATH_LABELS, exist_ok=True)


all_paths = os.listdir(SOURCE_NAME_PATH)


for image in all_paths:
    image_name_split = image.split(POSTFIX)


    image_name = image_name_split[0]
    image_ext = image_name_split[1]
    

    current_dataset_path = find_the_dataset_of_the_name(image_name, COPY_PATH)

    shutil.copy(os.path.join(current_dataset_path, "images", image_name + image_ext), DEST_PATH_IMAGES)


    # # copy the original txt file
    # shutil.copy(os.path.join(COPY_PATH_LABELS, image_name + ".txt"), DEST_PATH_LABELS)

    current_dataset_path_parent = "/".join(current_dataset_path.split("/")[:-1])


    # find the humans id
    humans_id = [find_the_id_of_class_in_dataset(current_dataset_path_parent, "person")]

    print(os.path.join(current_dataset_path, "labels", image_name + ".txt"))
    print(os.path.join(DEST_PATH_LABELS, image_name + ".txt"),"\n")

    # copy the txt file that has only the wanted class
    leave_only_the_wanted_class_and_copy_txt(os.path.join(current_dataset_path, "labels", image_name + ".txt"),
                                             os.path.join(DEST_PATH_LABELS, image_name + ".txt"),
                                             humans_id)











