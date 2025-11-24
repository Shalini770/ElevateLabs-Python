import os
from PIL import Image

# -------- CONFIGURATION --------
INPUT_FOLDER = "input_images"       # Folder that contains original images
OUTPUT_FOLDER = "resized_images"    # Folder to save resized images
TARGET_SIZE = (200, 200)            # Resize dimensions (width, height)
CONVERT_TO_FORMAT = None            # Set to "JPEG" or "PNG" to convert format (Optional)
# Example: CONVERT_TO_FORMAT = "JPEG"
# --------------------------------


def resize_images():
    # Create output folder if it does not exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Valid image extensions supported
    valid_extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")

    # List files in the input directory
    files = os.listdir(INPUT_FOLDER)

    processed_count = 0

    for file in files:
        file_path = os.path.join(INPUT_FOLDER, file)

        # Skip non-image files
        if not file.lower().endswith(valid_extensions):
            print(f"Skipping non-image file: {file}")
            continue

        try:
            with Image.open(file_path) as img:
                # Resize image
                resized_img = img.resize(TARGET_SIZE)

                # Determine output filename
                base_name, ext = os.path.splitext(file)
                new_filename = base_name

                # Apply format conversion if needed
                if CONVERT_TO_FORMAT:
                    new_filename += "." + CONVERT_TO_FORMAT.lower()
                else:
                    new_filename += ext

                output_path = os.path.join(OUTPUT_FOLDER, new_filename)

                # Save output
                if CONVERT_TO_FORMAT:
                    resized_img = resized_img.convert("RGB")  # Prevent PNG → JPEG errors
                    resized_img.save(output_path, format=CONVERT_TO_FORMAT)
                else:
                    resized_img.save(output_path)

                processed_count += 1
                print(f"Processed: {file} → {new_filename}")

        except Exception as e:
            print(f"❌ Error processing file '{file}': {e}")

    print("\nBatch Resize Completed!")
    print(f"Total images processed: {processed_count}")


if __name__ == "__main__":
    resize_images()
