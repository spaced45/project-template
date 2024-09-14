import os

def should_ignore(path, ignore_dirs):
    """Check if the directory or file should be ignored based on ignore directories."""
    for ignore_dir in ignore_dirs:
        if os.path.commonpath([path, ignore_dir]) == ignore_dir:
            return True
    return False

def scan_directory(base_path, ignore_dirs):
    """Scan the directory and return the folder structure while ignoring specified directories."""
    folder_structure = []

    for root, dirs, files in os.walk(base_path):
        # Ignore specified directories
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_dirs)]

        # Handle directories
        for name in dirs:
            dir_path = os.path.relpath(os.path.join(root, name), base_path)
            folder_structure.append(dir_path + '/')

        # Handle files
        for name in files:
            file_path = os.path.relpath(os.path.join(root, name), base_path)
            folder_structure.append(file_path)

    return folder_structure

def export_folder_structure(output_file, folder_structure):
    """Export the folder structure to a text file."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        for line in folder_structure:
            f.write(line + '\n')

def main():
    # Change this to your project folder
    project_folder = 'C:/Users/ville/OneDrive/Documents/VSCode/project-template'
    output_file = 'C:/Users/ville/OneDrive/Documents/VSCode/project-template/utils/folder_structure.txt'

    # Define directories to ignore
    ignore_dirs = [
        #os.path.join(project_folder, 'venv'),
        os.path.join(project_folder, '.git')
    ]

    # Scan directory and get folder structure
    folder_structure = scan_directory(project_folder, ignore_dirs)

    # Export folder structure to a text file
    export_folder_structure(output_file, folder_structure)
    print(f"Folder structure exported to {output_file}")

