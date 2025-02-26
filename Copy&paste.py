import os
import shutil
import time

# Define paths
path1 = r"C:/Production2/Hallmark/Build"
path2 = r"C:/Production_release/NewBuild_13022025/NewBuild"

def update_timestamp(path):
    """Update the last modified timestamp of a file or folder to the current time."""
    current_time = time.time()
    os.utime(path, (current_time, current_time))

def clean_directory(path1):
    """Delete all folders and files in path1 except MailContent folder and Web.config file."""
    # Ensure the path exists
    if not os.path.exists(path1):
        print(f"The path {path1} does not exist.")
        return

    # Iterate over all items in the directory
    for item in os.listdir(path1):
        item_path = os.path.join(path1, item)
        
        # Skip the MailContent folder and Web.config file
        if item == "MailContent" or item == "Web.config":
            print(f"Skipping {item}")
            continue
        
        # Remove the item
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"Deleted file: {item}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item}")
        except Exception as e:
            print(f"Failed to delete {item}. Reason: {e}")

def copy_except_excluded(path2, path1):
    """Copy all folders and files from path2 to path1 except MailContent folder and Web.config file."""
    # Ensure both paths exist
    if not os.path.exists(path2):
        print(f"Source path {path2} does not exist.")
        return
    if not os.path.exists(path1):
        print(f"Destination path {path1} does not exist.")
        return

    # Iterate over all items in the source directory (path2)
    for item in os.listdir(path2):
        source_item_path = os.path.join(path2, item)
        destination_item_path = os.path.join(path1, item)

        # Skip the MailContent folder and Web.config file
        if item == "MailContent" or item == "Web.config":
            print(f"Skipping {item}")
            continue

        # Copy the item
        try:
            if os.path.isfile(source_item_path):
                shutil.copy2(source_item_path, destination_item_path)
                print(f"Copied file: {item}")
            elif os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, destination_item_path)
                print(f"Copied folder: {item}")

            # Update the last modified timestamp to the current time
            update_timestamp(destination_item_path)
            print(f"Updated timestamp for: {item}")
        except Exception as e:
            print(f"Failed to copy {item}. Reason: {e}")

# Step 1: Clean path1 (delete all except MailContent and Web.config)
print("Step 1: Cleaning path1...")
clean_directory(path1)

# Step 2: Copy from path2 to path1 (except MailContent and Web.config)
print("\nStep 2: Copying from path2 to path1...")
copy_except_excluded(path2, path1)

print("\nProcess completed!")