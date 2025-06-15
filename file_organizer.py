import shutil
from pathlib import Path

# T1.2: Setup Source and Destination Directories
# Define the base paths for source and destination folders.
SOURCE_DIR = Path.cwd() / "source_files"
DEST_DIR = Path.cwd() / "organized_files"

# T1.1: Define Nested File Category Mappings
# This dictionary maps file extensions to their primary category folder.
# The sub-folder will be the extension name in uppercase.
FILE_TYPE_MAPPINGS = {
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Music
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".bmp": "Images",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    # Ebooks
    ".epub": "Ebooks",
    ".mobi": "Ebooks",
    
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}

DEFAULT_CATEGORY = "Others"

def get_destination_path(file_path):
    """
    Determines the nested destination path for a given file.
    
    Args:
        file_path (Path): The path object of the file to categorize.
        
    Returns:
        Path: The full destination path for the file.
    """
    file_extension = file_path.suffix.lower()
    primary_category = FILE_TYPE_MAPPINGS.get(file_extension, DEFAULT_CATEGORY)
    
    if primary_category == DEFAULT_CATEGORY:
        return DEST_DIR / primary_category
    
    extension_subfolder = file_extension[1:].upper()
    return DEST_DIR / primary_category / extension_subfolder


def move_file(source_path, destination_folder):
    """
    Moves a file to its destination folder with error handling.
    
    Args:
        source_path (Path): The path of the file to move.
        destination_folder (Path): The folder to move the file into.
    """
    try:
        # Create the destination folder if it doesn't exist
        destination_folder.mkdir(parents=True, exist_ok=True)
        
        print(f"Moving '{source_path.name}' to '{destination_folder}'...")
        shutil.move(str(source_path), str(destination_folder / source_path.name))
    except shutil.Error as e:
        print(f"⚠️  Warning: Could not move '{source_path.name}'. A file with that name may already exist. Error: {e}")
    except Exception as e:
        print(f"❌ Error: Failed to move '{source_path.name}'. Reason: {e}")


def main():
    """
    Main function to orchestrate the recursive file organization process.
    """
    print("Starting recursive file organization...")
    print(f"Source directory: {SOURCE_DIR}")
    print(f"Destination directory: {DEST_DIR}")
    print()
    
    # Use rglob('*') for a recursive search of all files in all subdirectories
    for source_path in SOURCE_DIR.rglob('*'):
        if source_path.is_file():
            destination_folder = get_destination_path(source_path)
            move_file(source_path, destination_folder)
            
    print("\n✅ File organization complete.")


if __name__ == "__main__":
    if not SOURCE_DIR.is_dir():
        print(f"❌ Error: Source directory not found at '{SOURCE_DIR}'")
    elif not DEST_DIR.is_dir():
        print(f"❌ Error: Destination directory not found at '{DEST_DIR}'")
    else:
        main()