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
