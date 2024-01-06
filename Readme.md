# Image EXIF Date Setter

## Overview
This Python script is designed to automatically update the EXIF date metadata of image files. It is particularly useful for organizing photos based on the year and month specified in the names of their containing folders. For instance, images in a folder named `1997_March` will have their EXIF date set to `01/03/1997 12:00:00`.

## Prerequisites
- Python 3
- Pillow (Python Imaging Library)
- Piexif

## Installation
Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Your Images:**
   - Organize your images into folders named in the `Year_Month` format (e.g., `1997_March`).
   - Ensure the images are in a format that supports EXIF data (e.g., JPEG).

2. **Run the Script:**
   - Execute the script by providing the path to the parent directory containing the image folders.

   ```bash
   python script.py path/to/your/image/folder
   ```
   - Replace path/to/your/image/folder with the actual path to your image folders.

3. **Check the results:**
   - After running the script, images in each folder will have their EXIF date set to the 1st of the respective month at 12:00:00.

## Notes

- The script sets the time to 12:00:00 for all images. If a different time is required, modify the script accordingly.
- The script currently only processes .jpg and .jpeg files. To include other formats, update the file extension checks in the script.
- This script assumes that the folders are named accurately and in the correct format. Misnamed folders might not be processed correctly.

## Troubleshooting
- If you encounter errors related to file formats or permissions, ensure that the image files are not corrupted and that you have the necessary permissions to modify them.
- For any UnidentifiedImageError, the script will skip the problematic file and continue with the next one.
