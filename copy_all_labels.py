import glob
import shutil
import os

DATASET_ROOT_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET"


DEST_PATH = "/home/umut/Desktop/all_labels"

os.makedirs(DEST_PATH, exist_ok=True)


for label_path in (glob.glob(os.path.join(DATASET_ROOT_PATH, "**/**/labels/*.txt"), recursive=True)):
    shutil.copy(label_path, DEST_PATH)






