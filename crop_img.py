# Use that file if after labelling appear that you need to crop the image for ROI
import glob
import os
import cv2

original_img_format = ".jpg"
img_format_to_save = ".jpg"

# Drop there a folder path where to save a sorted data
destination_folder = fr'C:\path_to_folder\\destination_folder'

# Drop here a path to a folder where unsorted data located
folder_with_txt_and_img = glob.glob(r"D:\\path_to_folder\*.jpg")

# Cropping settings,
# if you dont need to crop -> put full image resolution
crop_x_from = 0
crop_x_to = 1500

crop_y_from = 0
crop_y_to = 1203
# Cropping settings

for img_path in folder_with_txt_and_img:
    print("working with: ", img_path)
    image = cv2.imread(img_path)
    original_shape = image.shape  # h, w format

    head, tail = os.path.split(img_path)
    file_name_str = str(tail.split(original_img_format)[0])

    image_cropped = image[crop_y_from:crop_y_to, crop_x_from:crop_x_to].copy()

    path_to_full_box_plot_png = f"{destination_folder}\{file_name_str}.{img_format_to_save}"
    cv2.imwrite(path_to_full_box_plot_png, image_cropped)

print("DONE")