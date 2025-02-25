import os
import glob
import subprocess

# Specify the full path to the WinRAR executable
WINRAR_PATH = r"C:\Program Files\WinRAR\WinRAR.exe"

# Function to delete buildX.rar files except build.rar (case-insensitive)
def delete_buildx_rar_files(folder_path):
    try:
        # Use glob to find all files matching the pattern "build*.rar" (case-insensitive)
        rar_files = glob.glob(os.path.join(folder_path, "[bB]uild*.rar"))
        
        # Iterate through the matched files
        for rar_file in rar_files:
            # Extract the file name from the full path
            file_name = os.path.basename(rar_file)
            
            # Skip "build.rar" (case-insensitive) and delete all other "buildX.rar" files
            if file_name.lower() != "build.rar":
                os.remove(rar_file)
                print(f"Deleted: {file_name}")
            else:
                print(f"Skipped: {file_name} (protected)")
    except Exception as e:
        print(f"An error occurred in delete_buildx_rar_files: {e}")

# Main function to process the folder
def process_folder(folder_path):
    # Step 1: Check for .rar files starting with "build" (case-insensitive)
    rar_files = [f for f in os.listdir(folder_path) if f.lower().startswith("build") and f.endswith(".rar")]

    if rar_files:
        print(f"Found .rar files: {rar_files}")

        # Step 2: Delete all buildX.rar files except build.rar
        delete_buildx_rar_files(folder_path)

        # Step 3: Rename build.rar to build1.rar if it exists (case-insensitive)
        build_rar_path = None
        for rar_file in rar_files:
            if rar_file.lower() == "build.rar":
                build_rar_path = os.path.join(folder_path, rar_file)
                break

        if build_rar_path:
            new_name = os.path.join(folder_path, "build1.rar")
            os.rename(build_rar_path, new_name)
            print(f"Renamed {os.path.basename(build_rar_path)} to build1.rar")
        else:
            print("build.rar not found.")

        # Step 4: Add Build folder to build1.rar
        build_folder = os.path.join(folder_path, "Build")
        if os.path.exists(build_folder):
            subprocess.run([WINRAR_PATH, "a", "-r", os.path.join(folder_path, "build.rar"), build_folder])
            print(f"Added Build folder to build1.rar")
        else:
            print("Build folder not found.")
    else:
        # If no .rar files starting with "build", directly add Build folder to build.rar
        build_folder = os.path.join(folder_path, "Build")
        if os.path.exists(build_folder):
            subprocess.run([WINRAR_PATH, "a", "-r", os.path.join(folder_path, "build.rar"), build_folder])
            print(f"Added Build folder to build.rar")
        else:
            print("Build folder not found.")

# Example usage
folder_path = r"C:\Production1\hallmark"  # Replace with the actual path to your folder
process_folder(folder_path)