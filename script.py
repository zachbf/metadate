import os
import sys
from PIL import Image, ExifTags
from datetime import datetime
import calendar
import piexif

def apply_exif_date(folder_path):
    for subdir, _, files in os.walk(folder_path):
        folder_name = os.path.basename(subdir)
        parts = folder_name.split('_')
        updated_count = 0  # Counter for successfully updated photos

        if len(parts) == 2 and parts[0].isdigit():
            year = int(parts[0])
            month_str = parts[1]
            try:
                month = list(calendar.month_name).index(month_str)
                for file in files:
                    # Skip hidden files like .DS_Store
                    if file.startswith('.'):
                        continue

                    file_path = os.path.join(subdir, file)
                    try:
                        image = Image.open(file_path)
                        exif_dict = piexif.load(image.info["exif"])

                        # Set the 'DateTimeOriginal' to the 1st of the month at 12:00:00
                        # Set the 'DateTimeDigitized' to the current datetime
                        exif_date_original = datetime(year, month, 1, 12, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
                        exif_date_digitized = datetime.now().strftime("%Y:%m:%d %H:%M:%S")

                        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_date_original
                        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_date_digitized

                        exif_bytes = piexif.dump(exif_dict)

                        # Save the image with new EXIF data
                        image.save(file_path, "jpeg", exif=exif_bytes)
                        updated_count += 1  # Increment the counter
                    except (IOError, SyntaxError, ValueError) as e:
                        print(f"Skipping file (not a valid image or corrupted): {file_path}")
                        continue

                # After processing all files in the folder, report the count
                print(f"Updated {updated_count} photos in folder: {subdir}")
                
            except ValueError:
                print(f"Invalid folder name, skipping: {subdir}")
                continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [parent_folder_path]")
        sys.exit(1)
    
    parent_folder_path = sys.argv[1]
    apply_exif_date(parent_folder_path)
