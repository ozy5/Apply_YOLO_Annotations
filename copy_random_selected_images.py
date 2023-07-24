import os
import numpy as np
import shutil
import random

SOURCE_PATH = "/home/umut/Desktop/0_human_images_annotated"

DEST_PATH = "/home/umut/Desktop/selected_images"

RANDOM_IMAGE_COUNT = 300

all_paths = os.listdir(SOURCE_PATH)

random.shuffle(all_paths)

all_paths = all_paths[:RANDOM_IMAGE_COUNT]

for current_path in all_paths:
    shutil.copy(os.path.join(SOURCE_PATH, current_path), DEST_PATH)




