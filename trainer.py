import cv2
import csv
import os
from data import csv_data
from settings import class_id, num_images

# Additional function to collect existing image paths from Train.csv
def get_existing_image_paths(csv_file_path):
    existing_paths = set()
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_paths.add(row['Path'])
    except FileNotFoundError:
        pass  # If Train.csv does not exist, just return an empty set
    return existing_paths

def find_last_processed_image(csv_file_path, class_id):
    max_set_counter = -1
    max_image_counter = -1
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if class_id in row['Path']:
                    parts = row['Path'].split('_')
                    set_counter, image_counter = int(parts[-2]), int(parts[-1].split('.')[0])
                    if set_counter > max_set_counter or (set_counter == max_set_counter and image_counter > max_image_counter):
                        max_set_counter, max_image_counter = set_counter, image_counter
    except FileNotFoundError:
        pass  # If Train.csv does not exist, start from the beginning
    return max_set_counter, max_image_counter


# Function to validate if image paths exist before processing
def validate_image_paths(image_paths):
    missing_images = [img for img in image_paths if not os.path.exists(img)]
    if missing_images:
        print("The following images are missing and will be skipped:")
        for missing in missing_images:
            print(missing)
    return [img for img in image_paths if os.path.exists(img)]


# MAXIMUM 22 IMAGES FOR INPUT
class_id_padded = f"{int(class_id):05d}"

output_csv_path = 'output.csv'
train_csv_path = 'Train.csv'  # Path to your existing Train.csv file

base_save_dir = f'Train/{class_id}'
trainer_dir = 'Trainer'

# Generate image paths for both naming conventions
image_paths = [f'{trainer_dir}/{class_id}/image{i+1}.png' for i in range(num_images)]
image_paths += [f'{trainer_dir}/{class_id}/image{i:02d}.png' for i in range(1, num_images+1)]
valid_image_paths = validate_image_paths(image_paths)  # Validate paths before processing

last_set_counter, last_image_counter = find_last_processed_image(output_csv_path, class_id)

total_processed_images = last_set_counter * 29 + last_image_counter + 1
num_existing_images = len([img for img in valid_image_paths if os.path.exists(img)])
starting_image_index = total_processed_images - num_existing_images

existing_image_paths = get_existing_image_paths(train_csv_path)

if not os.path.exists(base_save_dir):
    os.makedirs(base_save_dir)

with open(output_csv_path, mode='w', newline='') as output_file, open(train_csv_path, mode='a', newline='') as train_file:
    output_writer = csv.writer(output_file)
    train_writer = csv.writer(train_file)
    output_writer.writerow(['Width', 'Height', 'Roi.X1', 'Roi.Y1', 'Roi.X2', 'Roi.Y2', 'ClassId', 'Path'])

    # Find the last image and set numbers
    set_counter, image_counter = (total_processed_images // 29, total_processed_images % 29) if total_processed_images > 0 else (0, 0)

    # If images already exist, start from the next set and image numbers
    if image_counter >= 0:
        image_counter += 1
        if image_counter >= 29:  # Assuming 29 is the limit within a set
            image_counter = 0
            set_counter += 1
    else:  # No images found, start from the first image in the first set
        image_counter = 0
        set_counter = 0 if set_counter == 0 else set_counter + 1

    for idx, image_path in enumerate(valid_image_paths):
        if idx < starting_image_index:
            continue
        
        input_image = cv2.imread(image_path)
        if input_image is None:
            print(f"Failed to load image: {image_path}")
            continue

        for width, height, roi_x1, roi_y1, roi_x2, roi_y2, _ in csv_data:
            resized_image = cv2.resize(input_image, (width, height))
            filename = f"{class_id_padded}_{set_counter:05d}_{image_counter:05d}.png"
            relative_path = f"Train/{class_id}/{filename}"
            save_path = os.path.join(base_save_dir, filename)

            # Check if the image's path is already in Train.csv
            if relative_path in existing_image_paths:
                continue  # Skip this image as its data is already in Train.csv

            if not os.path.exists(os.path.dirname(save_path)):
                os.makedirs(os.path.dirname(save_path))

            cv2.imwrite(save_path, resized_image)
            output_writer.writerow([width, height, roi_x1, roi_y1, roi_x2, roi_y2, class_id, relative_path])
            train_writer.writerow([width, height, roi_x1, roi_y1, roi_x2, roi_y2, class_id, relative_path])

            image_counter += 1
            if image_counter >= 29:  # Reset counter and increase set number after reaching limit
                image_counter = 0
                set_counter += 1
