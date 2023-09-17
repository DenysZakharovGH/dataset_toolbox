#Dataset_toolbox
Dataset_toolbox is a versatile toolkit designed to aid in the adjustment and management of datasets, 
especially focused on image and label data. 
This toolkit streamlines various dataset-related tasks, enhancing your workflow efficiency.
##
###Table of Contents
- Introduction
- Usage
- Setting Up Variables
- Cropping Labeled Data
- Debug Visualization
- Cleaning Unlabeled Images
- Usage
 -Set Up Variables
##
####
Before using Dataset_toolbox, you need to configure certain variables to align with your dataset structure. 

These variables can be found in the main script, and their definitions are as follows:

    folder_with_txt_and_img: 
This variable should point to the folder containing the original image and label data.

    destination_folder: 
Specify the directory where all the processed data will be saved.

    img_format: 
Set the image format you are using, such as .jpg.

    label_format: 
Define the format of your label data files, for example, .txt.

###Cropping Labeled Data
If you need to crop already labeled data while maintaining label consistency, 
you can use the crop_YOLO_img.py script. This script reads both the data and label files, 
performs image cropping, and updates the label positions accordingly.

Debug Visualization
During the cropping process, you might want to verify the accuracy of the updated labels. 
To facilitate this, you can enable the option in the script. 

    DEBUG_VISUALIZE 
  
##  
###Cropping Not Labeled Data
If you need to crop non labeled data while maintaining label consistency, 
you can use the crop_img.py script. This script, performs image cropping and save to destination folder.


##
###Cleaning Unlabeled Images
To clean up your dataset directory by removing images that are not labeled, 
the 
    
    delete_all_not_labeled.py 

script can be employed. This is particularly useful for maintaining a clean and organized dataset.

Conclusion
Dataset_toolbox offers a collection of powerful tools that simplify dataset 
adjustments and enhance the management of image and label data. 
Whether you need to crop labeled data or remove unlabeled images, 
this toolkit is designed to enhance your dataset management process.