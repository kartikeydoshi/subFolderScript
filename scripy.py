import os
import shutil


source_folder = r"path_to_source_folder"
target_folder = r"path_to_sink_folder"

# Create the target folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Function to recursively copy all files from source to target
def copy_files_recursively(src_folder, tgt_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            src_file_path = os.path.join(root, file)
            shutil.copy(src_file_path, tgt_folder)


copy_files_recursively(source_folder, target_folder)

print("All files have been copied successfully.")
