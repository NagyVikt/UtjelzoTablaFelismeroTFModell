import cv2
import csv
import os
from data import csv_data

class_id = '43'
output_csv_path = 'output.csv'

# Use forward slashes in paths, and Python will handle it correctly on Windows as well.
base_save_dir = f'Train/{class_id}'

trainer_dir = 'Trainer'
num_images = 11
image_paths = [f'{trainer_dir}/{class_id}/image{i+1}.png' for i in range(num_images)]

if not os.path.exists(base_save_dir):
    os.makedirs(base_save_dir)

with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Width', 'Height', 'Roi.X1', 'Roi.Y1', 'Roi.X2', 'Roi.Y2', 'ClassId', 'Path'])

    image_counter = 0
    set_counter = 2

    for image_path in image_paths:
        input_image = cv2.imread(image_path)
        if input_image is None:
            print(f"Failed to load image: {image_path}")
            continue

        for idx, (width, height, roi_x1, roi_y1, roi_x2, roi_y2, _) in enumerate(csv_data):
            resized_image = cv2.resize(input_image, (width, height))

            # Manually construct path with forward slashes
            filename = f"{class_id}_{set_counter:05d}_{image_counter:05d}.png"
            relative_path = f"Train/{class_id}/{filename}"
            save_path = os.path.join(base_save_dir, relative_path.replace('\\', '/'))

            if not os.path.exists(os.path.dirname(save_path)):
                os.makedirs(os.path.dirname(save_path))

            cv2.imwrite(save_path, resized_image)
            writer.writerow([width, height, roi_x1, roi_y1, roi_x2, roi_y2, class_id, relative_path])

            image_counter += 1
            if image_counter >= 29:
                image_counter = 0
                set_counter += 1
