import yaml
from yaml.loader import SafeLoader
import os


def find_the_id_of_class_in_dataset(DATASET_PATH: str,
                                 class_name: str) -> int:
    
    '''
    This function is used to find the label id of the given class name in the dataset.
    '''

    # Open the data.yaml file in the dataset path
    with open(os.path.join(DATASET_PATH, "data.yaml")) as f:
        data = yaml.load(f, Loader=SafeLoader)

    # Get the class names
    class_names = data["names"]


    if(type(class_names) == list):
        class_index = class_names.index(class_name)
    elif(type(class_names) == dict):
        class_index = class_names[class_name]

    # Find the index of the class name
    
    # Return the class index
    return class_index

