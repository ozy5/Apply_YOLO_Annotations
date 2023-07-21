import os
import numpy as np
import time
import shutil

ROOT_PATH = "annotated_images"

sub_dirs = os.listdir(ROOT_PATH)

all_paths = []

for dir in sub_dirs:
    current_files = os.listdir(os.path.join(ROOT_PATH, dir))
    all_paths += current_files
    break

all_paths = np.array(all_paths)

get_name = np.vectorize(lambda x: x.split(".rf")[0])

all_paths = get_name(all_paths)

print(len(all_paths))
print(len(np.unique(all_paths)))
print(np.unique(all_paths))



start = time.time()


#O(n)

saved_names = dict()
saved_names_full_path = []
for dir in sub_dirs:
    current_files = os.listdir(os.path.join(ROOT_PATH, dir))
    for current_name in current_files:
        current_name_actual = current_name.split(".rf")[0]
        try:
            x = saved_names[current_name_actual]
        except:
            saved_names[current_name_actual] = 1
            saved_names_full_path.append(os.path.join(ROOT_PATH, dir, current_name))

os.makedirs("annotated_images_no_duplicates", exist_ok=True)

for current_path in saved_names_full_path:
    shutil.copy(current_path, "annotated_images_no_duplicates")

print(f"Time taken: {time.time() - start}")


#O(n^2)
# saved_names = []
# saved_names_full_path = []


# for dir in sub_dirs:
#     current_files = os.listdir(os.path.join(ROOT_PATH, dir))
#     for current_name in current_files:
#         current_name_actual = current_name.split(".rf")[0]
#         if(not(current_name_actual in saved_names)):
#             saved_names.append(current_name_actual)
#             saved_names_full_path.append(os.path.join(ROOT_PATH, dir, current_name))

# print(f"Time taken: {time.time() - start}")













