import glob

def find_the_dataset_of_the_name(name: str, ROOT_PATH: str) -> str:
    """
    This function is used to find the dataset of the given name.
    """

    #find all the paths that has the name
    all_paths = glob.glob(f"{ROOT_PATH}/**/{name}.txt", recursive=True)

    #if there is no path, raise an exception
    if(len(all_paths) == 0):
        raise Exception(f"In the directory {ROOT_PATH}, nopath found for the name: {name}")

    #get the first path, split it by "/", remove the last two elements to get rid of the image name and sub-folder(labels), join them with "/" and return
    return_string = "/".join(all_paths[0].split("/")[:-2])

    #return the string
    return return_string




