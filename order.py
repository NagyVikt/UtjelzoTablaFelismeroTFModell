import os
import glob

def rename_images(directory, extension="png"):
    # Change the directory to the folder containing images
    os.chdir(directory)
    
    # List all image files with the specified extension
    image_files = glob.glob(f"*.{extension}")
    
    # Sort the files to maintain any existing order
    image_files.sort()
    
    # Loop through the files and rename them
    for i, file in enumerate(image_files, start=1):
        # Create new file name with leading zeros
        new_name = f"image{str(i).zfill(2)}.{extension}"
        
        # Rename the file
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")

# Example usage:
directory_path = 'Trainer/45'
rename_images(directory_path)
