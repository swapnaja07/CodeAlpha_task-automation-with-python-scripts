import os
import shutil

def organize_files(source_dir, dest_dir):
    # Create destination directories if they don't exist
    for folder_name in ['Images', 'Documents', 'Videos']:
        os.makedirs(os.path.join(dest_dir, folder_name), exist_ok=True)

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            # Determine file type and move to appropriate directory
            file_type = filename.split('.')[-1].lower()
            if file_type in ['jpg', 'png', 'gif' , 'jpeg']:
                shutil.move(source_path, os.path.join(dest_dir, 'Images', filename))
            elif file_type in ['pdf', 'doc', 'txt']:
                shutil.move(source_path, os.path.join(dest_dir, 'Documents', filename))
            elif file_type in ['mp4', 'avi', 'mov']:
                shutil.move(source_path, os.path.join(dest_dir, 'Videos', filename))

# Example usage
source_directory = 'D:\problem'
destination_directory = 'D:/OrganizedFiles'
organize_files(source_directory, destination_directory)
