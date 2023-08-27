# TO delete images which doesnt belongs to any of labels
import glob
import os
import shutil

# Drop here a path to a folder where unsorted data located
folder_with_txt_and_img = glob.glob(fr'D:\\path_to_folder\*.txt')

# Drop there a folder path where to save a sorted data
destination_folder = fr'D:\path_to_folder\\destination_folder'

img_format = ".jpg"
label_format = ".txt"

success_files = []
fail_files = []

print("START")
print("-"*50)
for lbl_path in folder_with_txt_and_img:
    print("working with: ", lbl_path)

    head, tail = os.path.split(lbl_path)
    file_name_str = str(tail.split(label_format)[0])

    path_to_img = lbl_path.replace(label_format, img_format)

    path_to_full_box_plot_jpg = f"{destination_folder}\{file_name_str}.{img_format}"
    path_to_full_box_plot_txt = f"{destination_folder}\{file_name_str}.{label_format}"

    if os.path.exists(path_to_img):
        shutil.copy(lbl_path, path_to_full_box_plot_txt)
        shutil.copy(path_to_img, path_to_full_box_plot_jpg)
        success_files.append(lbl_path)
    else:
        fail_files.append(lbl_path)

print("-"*50)
print("DONE")
print("-"*50)
print("Success with:", len(success_files))
print("Fail with:", len(fail_files))
for name in fail_files:
    print(f"\tfail -> {name}", " ?Maybe releted img is not exist?")
print("-"*50)



