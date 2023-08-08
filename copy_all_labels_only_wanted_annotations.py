import glob
import shutil
import os

DATASET_ROOT_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET"


DEST_PATH = "/home/umut/Desktop/AKONS_TRAINING_DATASET_all_labels_only_human_annotations"

os.makedirs(DEST_PATH, exist_ok=True)


datasets_dict = {
    "attemp6.v1i.yolov5pytorch" : {"0":"0"},
    "Drone Detection.v4i.yolov5pytorch": {"2":"0"},
    "drone_detection_final roboflow universe.v1i.yolov5pytorch": {"0":"0"},
    "Drony.v8i.yolov5pytorch": {"0":"0"},
    "Heli Drone Missile.v4i.yolov5pytorch": {"0":"0"},
    "KILINC3.v3i.yolov5pytorch": {"1":"0"},
    "x2.v1i.yolov8": {"0":"0"}
}



for label_path in (glob.glob(os.path.join(DATASET_ROOT_PATH, "**/**/labels/*.txt"), recursive=True)):
    dataset_name = label_path.split("/")[-4]
    current_dataset_dict = datasets_dict[dataset_name]
    wanted_indexes = list(current_dataset_dict.keys())

    dest_txt_path = os.path.join(DEST_PATH, label_path.split("/")[-1])

    with open(label_path, 'r') as in_file:
        lines = in_file.readlines()

    filtered_lines = [(current_dataset_dict[line[0]] + line[1:]) for line in lines if (line.split(' ', 1)[0] in wanted_indexes)]

    with open(dest_txt_path, 'w') as out_file:
        out_file.writelines(filtered_lines)
    #return True if everything is ok
        
















