import cv2
import pytesseract
import numpy as np

# If Tesseract is not in your PATH, specify the full path

def extract_text_from_image(image_path):
    """
    Load an image, preprocess it, and extract text using Tesseract OCR.
    """
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image at path '{image_path}' cannot be loaded.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply some preprocessing: (optional: adjust as needed)
    # Use a median blur to reduce noise
    gray = cv2.medianBlur(gray, 3)
    
    # Optionally, apply adaptive thresholding to improve OCR accuracy
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    
    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(thresh)
    return text

if __name__ == '__main__':
    # Path to a sample ID image stored in the 'data' folder
    image_path = 'data/id_sample.jpg'  # Make sure you have an image here
    try:
        extracted_text = extract_text_from_image(image_path)
        print("Extracted Text:")
        print("----------------")
        print(extracted_text)
    except Exception as e:
        print("Error:", e)
