import requests
import zipfile
import os

# API URL for the ZIP file
api_url = "https://zenodo.org/api/records/13854938/files-archive"

# Paths to store ZIP and extracted data
zip_path = "data/dataset.zip"
extract_path = "data/"

# Ensure data directory exists
os.makedirs(extract_path, exist_ok=True)

# Step 1: Download the ZIP file
response = requests.get(api_url)

if response.status_code == 200:
    # Save the ZIP file
    with open(zip_path, "wb") as file:
        file.write(response.content)
    print(f"ZIP file saved at {zip_path}")

    # Step 2: Extract the ZIP file
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extracted contents to {extract_path}")

    # Step 3: Find the first image file
    image_path = None
    for file_name in os.listdir(extract_path):
        if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(extract_path, file_name)
            print(f"Using image: {image_path}")
            break

    if image_path:
        print(f"Image saved for OCR processing: {image_path}")
    else:
        print("No image found in the extracted files.")

else:
    print(f"Failed to download ZIP. Status Code: {response.status_code}")
