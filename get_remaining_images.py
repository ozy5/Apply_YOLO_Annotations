import os
import numpy as np
import shutil


SOURCE_NAME_PATH = "/home/umut/Desktop/random_selected_images"

POSTFIX = "_humans_annotated"


COPY_PATH = "/home/umut/Desktop/all_images_and_labels_no_duplicate_names"

COPY_PATH_IMAGES = os.path.join(COPY_PATH, "images")
COPY_PATH_LABELS = os.path.join(COPY_PATH, "labels")




DEST_PATH = "/home/umut/Desktop/remaining_images"

DEST_PATH_IMAGES = os.path.join(DEST_PATH, "images")
DEST_PATH_LABELS = os.path.join(DEST_PATH, "labels")

os.makedirs(DEST_PATH_IMAGES, exist_ok=True)
os.makedirs(DEST_PATH_LABELS, exist_ok=True)


all_paths = os.listdir(SOURCE_NAME_PATH)


for image in all_paths:
    image_name_split = image.split(POSTFIX)

    image_name = image_name_split[0]
    print(image_name)
    image_ext = image_name_split[1]
    print(os.path.join(COPY_PATH_IMAGES, image_name + ".jpg"))

    # shutil.copy(os.path.join(COPY_PATH_IMAGES, image_name + ".jpg"), DEST_PATH_IMAGES)
    # shutil.copy(os.path.join(COPY_PATH_LABELS, image_name + ".txt"), DEST_PATH_LABELS)








