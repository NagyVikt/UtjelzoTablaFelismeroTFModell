import cv2
import csv
import os
from data import csv_data 

# The input image path and the base directory for saving images
# Paths to your images
image_paths = ['/path/to/image1.png', '/path/to/image2.png', '/path/to/image3.png',  # ...and so on until image11
]


base_save_dir = '/path/to/your/base/directory'  # Replace with your base directory path



# Class ID is assumed to be '20' for all entries
class_id = '20'
output_csv_path = 'output.csv'  # The CSV file where the information will be saved

# Create the base save directory if it doesn't exist
if not os.path.exists(base_save_dir):
    os.makedirs(base_save_dir)

# CSV file writing setup
with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Width', 'Height', 'Roi.X1', 'Roi.Y1', 'Roi.X2', 'Roi.Y2', 'ClassId', 'Path'])

    # Image and set counters
    image_counter = 0  # Counter for each image in a set of 29
    set_counter = 2  # Starts from 2 based on your example, adjust as needed

    # Loop through your 11 images, adjusting the path as needed
    for img_number in range(11):  # Assuming you have a mechanism to load these images
        input_image_path = f'/path/to/your/input_image_{img_number}.png'
        input_image = cv2.imread(input_image_path)

        for idx, (width, height, roi_x1, roi_y1, roi_x2, roi_y2, _) in enumerate(csv_data):
            # Resize and process image
            resized_image = cv2.resize(input_image, (width, height))

            # Construct the file path based on counters
            filename = f"{class_id}_{set_counter:05d}_{image_counter:05d}.png"
            relative_path = os.path.join("Train", class_id, filename)
            save_path = os.path.join(base_save_dir, relative_path)

            # Ensure the save directory exists
            if not os.path.exists(os.path.dirname(save_path)):
                os.makedirs(os.path.dirname(save_path))

            cv2.imwrite(save_path, resized_image)

            # Write to CSV
            writer.writerow([width, height, roi_x1, roi_y1, roi_x2, roi_y2, class_id, relative_path])

            # Update counters
            image_counter += 1
            if image_counter >= 29:  # Reset after every 29 images
                image_counter = 0
                set_counter += 1
