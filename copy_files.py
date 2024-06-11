import os
import shutil

def copy_files(file_list_path, source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Read the list of files
    with open(file_list_path, 'r') as file_list:
        files = [line.strip() for line in file_list if line.strip()]
    
    # Copy each file from source to destination
    for file_name in files:
        src_file = os.path.join(source_folder, file_name)
        dest_file = os.path.join(destination_folder, file_name)
        
        # Ensure the source file exists before attempting to copy
        if os.path.exists(src_file):
            # Create any necessary directories in the destination folder
            dest_folder = os.path.dirname(dest_file)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            # Copy the file
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} to {dest_file}")
        else:
            print(f"File not found: {src_file}")

# Example usage
file_list_path = 'file_list.txt'
source_folder = '/path/to/source/folder'
destination_folder = '/path/to/destination/folder'

copy_files(file_list_path, source_folder, destination_folder)
