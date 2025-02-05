import requests
import zipfile
import os
from io import BytesIO

# API URL for the ZIP file
api_url = "https://zenodo.org/api/records/13854938/files-archive"

# Paths to store ZIP and extracted data
zip_path = "data/dataset.zip"
extract_path = "data/"

# Step 1: Download the ZIP file
response = requests.get(api_url)

if response.status_code == 200:
    # Save the ZIP file
    with open(zip_path, "wb") as file:
        file.write(response.content)
    print(f"ZIP file saved at {zip_path}")

    # Step 2: Extract the ZIP file
    with zipfile.ZipFile(zip_