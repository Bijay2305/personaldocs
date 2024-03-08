from PIL import Image
import os

# Function to convert AVIF to JPG
def convert_avif_to_jpg(input_path, output_path):
    try:
        img = Image.open(input_path)
        if img.format == 'AVIF':
            img = img.convert('RGB')
            output_path_jpg = output_path[:-5] + '.jpg'  # Changing the extension
            img.save(output_path_jpg)
            print(f"Converted {input_path} to {output_path_jpg}")
        else:
            print(f"Skipping {input_path}, not an AVIF image.")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

# Function to iterate through files in a directory
def convert_avif_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".avif"):
            input_path = os.path.join(directory, filename)
            convert_avif_to_jpg(input_path, input_path)

# Example usage:
if __name__ == "__main__":
    directory = "./"  # Specify the directory containing AVIF images
    convert_avif_images_in_directory(directory)
++++++++++++++++++++
from PIL import Image
import os

# Function to convert JFIF to JPG
def convert_jfif_to_jpg(input_path, output_path):
    try:
        img = Image.open(input_path)
        if img.format == 'JPEG':
            img.save(output_path, 'JPEG')
            print(f"Converted {input_path} to {output_path}")
        else:
            print(f"Skipping {input_path}, not a JFIF image.")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

# Function to iterate through files in a directory
def convert_jfif_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename[:-5] + '_converted.jpg')  # Changing the extension
            convert_jfif_to_jpg(input_path, output_path)

# Example usage:
if __name__ == "__main__":
    directory = "./"  # Specify the directory containing JFIF images
    convert_jfif_images_in_directory(directory)
++++++++++++++++++++++
from PIL import Image
import os

def convert_jfif_to_jpg_in_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jfif"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename[:-5] + ".jpg")  # Change extension to .jpg
            convert_jfif_to_jpg(input_path, output_path)

def convert_jfif_to_jpg(input_path, output_path):
    try:
        # Open the JFIF image
        with Image.open(input_path) as img:
            # Check if the image format is JFIF
            if img.format == 'JPEG':
                # Save the image in JPG format
                img.save(output_path)
                print(f"Converted {input_path} to {output_path}")
            else:
                print(f"Skipping {input_path}, not a JFIF image.")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

# Example usage:
if __name__ == "__main__":
    input_folder = "input_folder"  # Folder containing JFIF images
    output_folder = "output_folder"  # Folder to save JPG images
    convert_jfif_to_jpg_in_folder(input_folder, output_folder)
