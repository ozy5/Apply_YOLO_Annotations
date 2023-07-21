import yaml
import cv2
import os
import random
from yaml.loader import SafeLoader
import numpy as np
from PIL import Image


#SAVE_PATH_OPENCV = "./annotated_images/OPENCV"
#os.makedirs(SAVE_PATH_OPENCV, exist_ok=True)


# Open the file and load the file
with open('data.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

#randomize the bbox colors for detection classes
class_count = data["nc"]
color_map = dict()
for key in range(class_count):
    color_map[key] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class_names = data["names"]

project_name = data["roboflow"]["project"]


SAVE_PATH_PIL = os.path.join("./annotated_images/", project_name)
os.makedirs(SAVE_PATH_PIL, exist_ok=True)


#Find the paths of all images
train_img_dir = data["train"][1:]
train_image_names = [(train_img_dir + "/" + x) for x in os.listdir(train_img_dir)]

val_img_dir = data["val"][1:]
val_image_names = [(val_img_dir + "/" + x) for x in os.listdir(val_img_dir)]

if(os.path.exists(data["test"][1:])):
    test_img_dir = data["test"][1:]
    test_image_names = [(test_img_dir + "/" + x) for x in os.listdir(test_img_dir)]







all_images_paths = train_image_names + val_image_names

if(os.path.exists(data["test"][1:])):
    all_images_paths = all_images_paths + test_image_names



random.shuffle(all_images_paths)


#Find the paths of all labels


train_label_dir = train_img_dir[0 : (len(train_img_dir) - 6)] + "labels"
train_label_names = [(train_label_dir + "/" + x) for x in os.listdir(train_label_dir)]
train_label_names_array = np.array(train_label_names)

val_label_dir = val_img_dir[0 : (len(val_img_dir) - 6)] + "labels"
val_label_names = [(val_label_dir + "/" + x) for x in os.listdir(val_label_dir)]
val_label_names_array = np.array(val_label_names)

if(os.path.exists(data["test"][1:])):
    test_label_dir = test_img_dir[0 : (len(test_img_dir) - 6)] + "labels"
    test_label_names = [(test_label_dir + "/" + x) for x in os.listdir(test_label_dir)]
    test_label_names_array = np.array(test_label_names)


all_labels_paths = np.concatenate((train_label_names_array, val_label_names_array), axis=0)

if(os.path.exists(data["test"][1:])):
    all_labels_paths = np.concatenate((all_labels_paths, test_label_names_array), axis=0)


for current_image in all_images_paths:

    name_length = len(current_image)
    ext_name = current_image.split(".")[-1]
    ext_lenght = len(ext_name)

    img_name_without_ext = current_image[0 :(name_length - 2 - ext_lenght)]
    absolute_img_name = img_name_without_ext.split("/")[-1]

    #check if label exists
    seek_func = np.vectorize(lambda x: absolute_img_name in x)

    if_label_exists = seek_func(all_labels_paths)

    if(if_label_exists.any()):
        current_label_path = all_labels_paths[if_label_exists][0]

        current_img_array = cv2.imread(current_image)
        current_img_width = current_img_array.shape[1]
        current_img_height = current_img_array.shape[0]
        
        with open(current_label_path, "r") as f:
            labels = f.readlines()
            for i in range(len(labels)):
                current_label = labels[i]

                current_labels_class = current_label.split(" ")[0]
                
                current_labels_bbox_x = float(current_label.split(" ")[1])
                current_labels_bbox_y = float(current_label.split(" ")[2])
                current_labels_bbox_w = float(current_label.split(" ")[3])
                current_labels_bbox_h = float(current_label.split(" ")[4])

                #calculate the bbox coordinates from center x and y normalized values

                (bbox_x1, bbox_y1) = (int((current_labels_bbox_x - current_labels_bbox_w/2) * current_img_width), int((current_labels_bbox_y - current_labels_bbox_h/2) * current_img_height))
                (bbox_x2, bbox_y2) = (int((current_labels_bbox_x + current_labels_bbox_w/2) * current_img_width), int((current_labels_bbox_y + current_labels_bbox_h/2) * current_img_height))

                #add bbox with the correntponding color regarding the color_map to the image
                cv2.rectangle(current_img_array, (bbox_x1, bbox_y1), (bbox_x2, bbox_y2), color_map[int(current_labels_class)], 2)

                #add the label text to the image including the class name
                cv2.putText(current_img_array, f"{class_names[int(current_labels_class)]}", (bbox_x1, bbox_y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_map[int(current_labels_class)], 1, cv2.LINE_AA)    
            
        
        #write the project name with light blue on left corner
        cv2.putText(current_img_array, f"{project_name}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1, cv2.LINE_AA)
        

        # #save the annotated image
        # cv2.imwrite(SAVE_PATH_OPENCV + "/" + absolute_img_name + "_annotated" + "." + ext_name, current_img_array)
        # print("Saved image: " + absolute_img_name + "_annotated_opencv" + "." + ext_name)

        #save with PIL
        im_pil = Image.fromarray(cv2.cvtColor(current_img_array, cv2.COLOR_BGR2RGB))
        im_pil.save(SAVE_PATH_PIL + "/" + absolute_img_name + "_annotated" + "." + ext_name)
        print("Saved image: " + absolute_img_name + "_annotated" + "." + ext_name)


# cv2.imread()







# for box in results["boxes"]:
#     box = [round(i, 2) for i in box.tolist()]


#     cv2.rectangle(imagecv, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), color_map[label.item()], 1)

#     cv2.putText(imagecv, f"FPS: {round(1/ (end-start))}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#     cv2.putText(imagecv, f"{model.config.id2label[label.item()]} {round(score.item(), 3)}", (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, color_map[label.item()], 2, cv2.LINE_AA)



