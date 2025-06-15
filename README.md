# Smart File Organizer & Archiver

Automatically organize and categorize files based on their types/extensions into dedicated, nested folders.

## Project Overview

This project focuses on the initial categorization of common media and document files into type-specific and extension-specific sub-folders. The file organizer scans a specified source directory and moves files into subdirectories based on their primary category (e.g., 'Images', 'Videos') and then further into sub-folders based on their exact file extensions (e.g., 'Images/JPG/', 'Videos/MP4/').

## Features

### Nested File Categorization
- Scan source directory and move files into categorized subdirectories
- Primary categories: Videos, Music, Images, Documents, Ebooks, Archives
- Extension-specific sub-folders (e.g., JPG, MP4, PDF)
- Automatic creation of destination folders as needed
- Error handling for permission issues and duplicate files

## File Structure

- `file_organizer.py` - Main file organization script
- `project.yaml` - Project configuration and roadmap
- `oop-001.py` - Basic OOP example
- `diamond_problem.py` - Diamond inheritance problem demonstration

## Usage

1. Create a `source_files` directory in the project root
2. Place files to be organized in the `source_files` directory
3. Run the organizer:
   ```bash
   python file_organizer.py
   ```
4. Files will be organized into the `organized_files` directory

## Supported File Types

- **Videos**: .mp4, .mkv, .avi, .mov
- **Music**: .mp3, .wav, .flac
- **Images**: .jpg, .jpeg, .png, .gif, .webp, .bmp
- **Documents**: .pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx
- **Ebooks**: .epub, .mobi
- **Archives**: .zip, .rar, .7z
- **Others**: Files with unrecognized extensions

## Future Enhancements

- Enhanced logging system
- Configuration file support
- Scheduling capabilities
- Advanced duplicate handling
- Graphical user interface
- Command line arguments support

## Python Concepts Demonstrated

- File system interaction with `pathlib` and `shutil`
- Dictionary mappings for file categorization
- Control flow with loops and conditionals
- Error handling with try-except blocks
- Function organization and modularity
- Object-oriented programming concepts