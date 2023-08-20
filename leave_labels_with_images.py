import os
import shutil

ROOT_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET"

for dataset in os.listdir(ROOT_PATH):
    dataset_path = os.path.join(ROOT_PATH, dataset)
    dataset_images_path = os.path.join(dataset_path, "train", "images")
    dataset_labels_path = os.path.join(dataset_path, "train", "labels")
    
    dataset_images_path_raw_names = dict()

    for image_name in os.listdir(dataset_images_path):
        #dataset_images_path_raw_names.append(".".join(image_name.split(".")[:-1]))
        dataset_images_path_raw_names[".".join(image_name.split(".")[:-1])] = True

    for label_name in os.listdir(dataset_labels_path):
        raw_name = ".".join(label_name.split(".")[:-1])
        try:
            x = dataset_images_path_raw_names[raw_name]
        except:
            #remove label
            os.remove(os.path.join(dataset_labels_path, label_name))
            continue

