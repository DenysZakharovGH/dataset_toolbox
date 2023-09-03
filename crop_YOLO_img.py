# Use that file if after labelling appear that you need to crop the image for ROI
import glob
import os
import cv2


DEBUG_VISUALIZE = True  # use debug to visualize your label, WARNING make False before use it data


# Drop here a path to a folder where unsorted data located
folder_with_txt_and_img = glob.glob(r"D:\\path_to_folder\*.jpg")

# Drop there a folder path where to save a sorted data
destination_folder = fr'C:\path_to_folder\\destination_folder'

original_img_format = ".jpg"
img_format_to_save = ".jpg"
label_format = ".txt"

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

    cropped_shape = image_cropped.shape  # h, w format

    image_height, image_width, _ = cropped_shape

    path_to_txt = img_path.replace(original_img_format, label_format)
    if not os.path.exists(path_to_txt):
        continue

    with open(path_to_txt, "r+") as file:
        file_content = file.readlines()

    str_annotation = ""
    for line in file_content:
        list_of_content = list(map(float, line.split(" ")))  # USE FOR YOLO DATA as SEPARATOR

        label, \
            center_x, \
            center_y, \
            rect_w, \
            rect_h = \
            list_of_content[0], \
            list_of_content[1] *original_shape[1], \
            list_of_content[2] *original_shape[0], \
            list_of_content[3] *original_shape[1], \
            list_of_content[4] *original_shape[0]

        center_x_roi = center_x - crop_x_from
        center_y_roi = center_y - crop_y_from

        if DEBUG_VISUALIZE:
            color = (255, 255, 0)
            cv2.rectangle(image_cropped, (int(center_x_roi - rect_w // 2), int(center_y_roi - rect_h // 2)),
                          (int(center_x_roi + rect_w // 2), int(center_y_roi + rect_h // 2)), color, 2)

        str_annotation += f"0 {round(center_x_roi / rect_w, 6)} {round(center_y_roi / rect_h, 6)} {round(rect_w / rect_w, 6)} {round(rect_h / rect_h, 6)}\n0"

    path_to_full_box_plot_png = f"{destination_folder}/{file_name_str}.{img_format_to_save}"
    path_to_full_box_plot_txt = f"{destination_folder}/{file_name_str}.{label_format}"

    cv2.imwrite(path_to_full_box_plot_png, image_cropped)

    with open(path_to_full_box_plot_txt, 'w') as f:
        f.write(str_annotation)

print("DONE")
