import cv2
import numpy as np

import imutils
import imageio
from skimage.filters import threshold_local

import argparse
from autocorrect import spell
import os


# Add a new post_process_text function to correct common OCR errors
def post_process_text(detected_text):
    # Implement rules to correct common mistakes, e.g., "5TOP" -> "STOP"
    # This is just a placeholder for your actual post-processing logic
    corrections = {
        "5TOP": "STOP",
        "51OP": "STOP",
        # Add more as needed
    }
    return corrections.get(detected_text, detected_text)

def find_red_regions(image):
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for red color and apply color thresholding for two different ranges of red
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # Combine masks for both red ranges
    mask = cv2.bitwise_or(mask1, mask2)
    
    # Apply morphological operations
    # Close operation (dilation followed by erosion) to close small holes inside the foreground
    kernel_close = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)

    # Open operation (erosion followed by dilation) to remove noise
    kernel_open = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
    
    # Find contours on the cleaned mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return mask, contours



def  filter_contours_based_on_area_and_shape(contours):
        # Filter contours based on the area and shape
    min_area = 100  # Minimum area of the contour to be considered
    max_area = 1000  # Maximum area of the contour to be considered

    filtered_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if min_area < area < max_area:
            # Further shape checks can be added here
            filtered_contours.append(cnt)

def crop_and_group_contours(contours, preprocessed_image, grouping_threshold=10):
    # Crop regions based on contours
    cropped_regions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped_region = preprocessed_image[y:y+h, x:x+w]
        cropped_regions.append((x, y, w, h, cropped_region))
    
    # Sort regions by x coordinate
    cropped_regions.sort(key=lambda b: b[0])

    # Grouping close contours
    grouped_regions = []
    group = [cropped_regions[0]]
    for i in range(1, len(cropped_regions)):
        prev_x, prev_y, prev_w, prev_h, _ = group[-1]
        cur_x, cur_y, cur_w, cur_h, cur_img = cropped_regions[i]
        
        # Check if current contour is close enough to the previous to be considered in the same group
        if cur_x - (prev_x + prev_w) < grouping_threshold:
            group.append(cropped_regions[i])
        else:
            # If not close, start a new group
            grouped_regions.append(group)
            group = [cropped_regions[i]]
    # Add the last group
    if group not in grouped_regions:
        grouped_regions.append(group)

    # Now we can process the groups to combine them into single images
    # But for now, we return individual cropped regions
    # To be replaced with actual logic for combining groups into single images
    processed_groups = [group[-1][-1] for group in grouped_regions]  # Placeholder for actual group processing

    return processed_groups





def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    #print s
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    print (rect)

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped





class SimpleOCR:
    def __init__(self, templates_dir="karakterek"):
        self.templates = self.load_templates(templates_dir)

    def load_templates(self, directory):
        templates = {}
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                path = os.path.join(directory, filename)
                char = filename.split('.')[0]  # Assuming filename is 'A.jpg' for 'A'
                templates[char] = cv2.imread(path, 0)
        return templates

    def preprocess_image(self, image_path):
        # Apply adaptive thresholding instead of global thresholding
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.medianBlur(img, 5)
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 11, 2)
        return thresh
    
    
    def find_contours(self, preprocessed_image):
        contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    
    def match_template(self, character_image):
        best_match = '?'
        min_val = float('inf')
        
        # Get the dimensions of the character image
        h, w = character_image.shape[:2]
        
        for char, template in self.templates.items():
            # Ensure the template size is not larger than the character image size
            if template.shape[0] > h or template.shape[1] > w:
                # Resize template to match the character image size
                template_resized = cv2.resize(template, (w, h))
            else:
                template_resized = template
            
            res = cv2.matchTemplate(character_image, template_resized, cv2.TM_SQDIFF_NORMED)
            min_val_temp = np.min(res)
            if min_val_temp < min_val:
                min_val = min_val_temp
                best_match = char

        return best_match


    def identify_characters(self, preprocessed_image):
        detected_characters = ''
        # Here you need to call self.find_contours(preprocessed_image) to get the contours
        contours = self.find_contours(preprocessed_image)
        # Now sort the contours
        contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
        
        visualization_image = preprocessed_image.copy()  # For visualization
        
        for cnt in contours:
            # Assuming a very basic method to bound rectangles around contours
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = w / float(h)
            if aspect_ratio < 0.2 or aspect_ratio > 1.0 or w < min_width or h < min_height:
                continue
            
            cv2.rectangle(visualization_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Extract the character image from the preprocessed image
            character_image = preprocessed_image[y:y+h, x:x+w]
            # Match the extracted image against templates
            character = self.match_template(character_image)
            detected_characters += character
        
        cv2.imwrite('6_character_regions.png', visualization_image)
    
        return detected_characters

    def perform_ocr(self, image_path):
        preprocessed = self.preprocess_image(image_path)
        text = self.identify_characters(preprocessed)
        return text

def main(image_path):
    # Initialize the OCR class with the path to your character templates
    ocr = SimpleOCR(templates_dir="karakterek")

    # Load the image and resize it
    image = cv2.imread(image_path)
    image = imutils.resize(image, height=500)

    # Red region detection
    mask, contours = find_red_regions(image)

    # Save the red mask image for debugging purposes
    cv2.imwrite('red_mask.png', mask)


    # Check if contours are found
    if contours is not None:
        filtered_contours = filter_contours_based_on_area_and_shape(contours)
        preprocessed_image = ocr.preprocess_image(image_path)

        if filtered_contours:  # Check if filtering was successful
            cropped_regions = crop_and_group_contours(filtered_contours, preprocessed_image)
                    
            # Perform OCR on each cropped region and concatenate results
            recognized_text = ''
            for region in cropped_regions:
                text = ocr.identify_characters(region)
                recognized_text += text + ' '

            # Post-process the recognized text to correct common OCR mistakes
            processed_text = post_process_text(recognized_text.strip())

            # Print the final recognized text
            print("Recognized Text:", processed_text)

        else:
            print("No contours passed the filtering criteria.")
    else:
        print("No contours were found in the image.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    image_path = "utjelzotablak/20.png"  # Directly specify the path to the image

    main(image_path)
