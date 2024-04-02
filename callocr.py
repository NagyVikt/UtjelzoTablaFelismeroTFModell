import cv2, Image
import numpy as np

import imutils
from scipy.misc import imsave
from skimage.filters import threshold_adaptive
import argparse
from autocorrect import spell
import os


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
    def __init__(self):
        # Dummy templates for illustration purposes
        # In practice, you would have a dictionary with character templates
        # For simplicity, this is just a placeholder
        self.templates = {
            # Character: Image template
        }
    
    def preprocess_image(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresh
    
    def find_contours(self, preprocessed_image):
        contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    
    def match_template(self, character_image):
        # This is a placeholder for template matching logic
        # You would compare character_image to each template and find the best match
        # Returning '?' as a placeholder for unmatched characters
        return '?'

    def identify_characters(self, preprocessed_image):
        detected_characters = ''
        contours = self.find_contours(preprocessed_image)

        for cnt in contours:
            # Assuming a very basic method to bound rectangles around contours
            x, y, w, h = cv2.boundingRect(cnt)
            # Extract the character image from the preprocessed image
            character_image = preprocessed_image[y:y+h, x:x+w]
            # Match the extracted image against templates
            character = self.match_template(character_image)
            detected_characters += character
        
        return detected_characters

    def perform_ocr(self, image_path):
        preprocessed = self.preprocess_image(image_path)
        text = self.identify_characters(preprocessed)
        return text

# # Example usage
# ocr = SimpleOCR()
# text_detected = ocr.perform_ocr("path_to_your_image.jpg")
# print(text_detected)

def main(image_path):
    # Load the image, resize it, and convert it to grayscale
    image = cv2.imread(image_path)
    image = imutils.resize(image, height=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 50, 200)

    # Find contours and apply the four-point transform to obtain a top-down view
    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    warped = four_point_transform(image, screenCnt.reshape(4, 2))

    # Convert the warped image to grayscale, then threshold it
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255

    # Save the processed image temporarily (consider processing directly if possible)
    imwrite('temp_processed.jpg', warped)

    # Initialize OCR and process the image
    ocr = SimpleOCR()
    text_detected = ocr.perform_ocr('temp_processed.jpg')
    print(text_detected)

    # Cleanup temporary files
    os.remove('temp_processed.jpg')

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
    args = vars(ap.parse_args())
    main(args["image"])