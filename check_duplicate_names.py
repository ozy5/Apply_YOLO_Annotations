import os
import numpy as np
import time
import shutil

ROOT_PATH = "/home/umut/Desktop/NEW_DATA_AKONS/Helicopters-of-DC.v2-copterfinder1.2.yolov5pytorch/train/images"
DEST_PATH = "/home/umut/Desktop/NEW_DATA_AKONS/images"

os.makedirs(DEST_PATH, exist_ok=True)


start = time.time()


#O(n)

saved_names = dict()
saved_names_full_path = []
for current_name in os.listdir(ROOT_PATH):
    current_name_actual = current_name.split(".rf")[0]
    try:
        x = saved_names[current_name_actual]
    except:
        saved_names[current_name_actual] = 1
        saved_names_full_path.append(os.path.join(ROOT_PATH, current_name))

print(len(saved_names_full_path))


for current_path in saved_names_full_path:
    shutil.copy(current_path, DEST_PATH)


print(f"Time taken: {time.time() - start}")













