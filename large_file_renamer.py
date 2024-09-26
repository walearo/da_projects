import os

def rename_files(directory_path, pattern):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            print("The specified directory does not exist.")
            return

        # List all the files in the directory
        files = os.listdir(directory_path)
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]  # Filter out directories

        # Sort files to rename them
        files.sort()

        # Check for the sequence placeholder in the pattern (e.g., ###)
        if "###" not in pattern:
            print("Please include '###' in the pattern to represent sequence numbers.")
            return

        # Rename each file
        for i, file_name in enumerate(files):
            # Extract the file extension
            file_extension = os.path.splitext(file_name)[1]

            # Create the new name by replacing ### with the sequence number
            new_name = pattern.replace("###", f"{i+1:03}") + file_extension

            # Get full file paths
            old_file_path = os.path.join(directory_path, file_name)
            new_file_path = os.path.join(directory_path, new_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# usage
if __name__ == "__main__":
    # Directory path where files are located
    directory_path = input("Enter the directory path: ")

    # Pattern for renaming files (e.g., 'image_###' where ### is the sequence number)
    pattern = input("Enter the renaming pattern (use ### for sequence numbers): ")

    # Call to the function to rename the files
    rename_files(directory_path, pattern)