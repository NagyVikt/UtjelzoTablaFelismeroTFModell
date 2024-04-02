import cv2
import numpy as np

import imutils
import imageio
from skimage.filters import threshold_local

import argparse
from autocorrect import spell
import os

def find_red_regions(image):
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for red color and apply color thresholding
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = cv2.bitwise_or(mask1, mask2)
    
    # Find contours on the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Optionally filter contours by shape...
    
    return mask, contours




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
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
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
        contours = self.find_contours(preprocessed_image)
        visualization_image = preprocessed_image.copy()  # For visualization

        for cnt in contours:
            # Assuming a very basic method to bound rectangles around contours
            x, y, w, h = cv2.boundingRect(cnt)

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

    # Load the image, resize it, and convert it to grayscale
    image = cv2.imread(image_path)
    image = imutils.resize(image, height=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 50, 200)

    cv2.imwrite('1_resized_and_gray.png', gray)

    cv2.imwrite('2_edges.png', edged)

    # Find contours and apply the four-point transform to obtain a top-down view
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    contour_image = image.copy()
    cv2.drawContours(contour_image, cnts, -1, (0, 255, 0), 3)
    cv2.imwrite('3_contours.png', contour_image)




    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break

    # Ensure the contours have been found before proceeding
    if 'screenCnt' in locals():
        warped = four_point_transform(image, screenCnt.reshape(4, 2))
        cv2.imwrite('4_warped.png', warped)

    else:
        print("Document boundary not detected, skipping perspective transform.")
        warped = gray  # Use the grayscale image if contour detection fails

    # Thresholding the warped image to prepare for OCR
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255



    # Perform OCR on the processed image
    text_detected = ocr.identify_characters(warped)

    cv2.imwrite('5_thresholded.png', warped)

    print("Recognized Text:", text_detected)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    image_path = "utjelzotablak/20.png"  # Directly specify the path to the image

    main(image_path)
