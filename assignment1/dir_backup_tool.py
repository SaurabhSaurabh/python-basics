# In DevOps, performing regular backups of important files is crucial:

# REQUIREMENTS:
# ● Implement a Python script called backup.py that takes a source directory and a destination 
# directory as command-line arguments.

# ● The script should copy all files from the source directory to the destination directory.

# ● Before copying, check if the destination directory already contains a file with the same name. 
# If so, append a timestamp to the file name to ensure uniqueness.

# ● Handle errors gracefully, such as when the source directory or destination directory does not exist.

# Sample Command:
# python backup.py /path/to/source /path/to/destination
# By running the script with the appropriate source and destination directories, 
# it should create backups of the files in the source directory, ensuring unique file names 
# in the destination directory.


import os #Interact with the file system (check paths, list files, join paths).
import shutil #Copy files and directories.
import sys #Access command-line arguments.
from datetime import datetime #Generate timestamps for unique file names.

def backup_files(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it.")
        os.makedirs(destination_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        # If file already exists in destination, append timestamp
        if os.path.exists(destination_file):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Split the filename into name and extension
            name, ext = os.path.splitext(filename)
            destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}")

        # Copy the file to the destination directory
        shutil.copy2(source_file, destination_file)
        print(f"Copied '{source_file}' to '{destination_file}'")


source_directory = input("Enter the source directory path: ")
destination_directory = input("Enter the destination directory path: ")
backup_files(source_directory, destination_directory)