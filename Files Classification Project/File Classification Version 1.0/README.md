# File Classification Project

## Overview
The File Classification project is a Python script designed to organize files based on their extensions into categorized folders. It helps in maintaining a structured file system by sorting files into specific folders according to their types such as audio, video, images, documents, and software.

## Functionality
The script performs the following tasks:
1. **User Input**: It prompts the user to input the folder path containing the files to be classified.
2. **File Classification**: The script categorizes files based on their extensions into predefined categories such as audio, video, images, documents, and software.
3. **Folder Creation**: It creates folders for each category if files with corresponding extensions are found.
4. **File Movement**: Files are then moved from the original folder to their respective categorized folders.

## Features
- **Customizable Extensions**: Users can customize the file extensions and their corresponding categories in the `dict_extensions` dictionary.
- **Dynamic Folder Creation**: The script dynamically creates folders for categories only if files with corresponding extensions are found.
- **Efficient File Handling**: It efficiently handles file movement and organization, reducing manual effort in organizing files.

## Usage
1. **Setup**: Ensure you have Python installed on your system.
2. **Run Script**: Execute the Python script and provide the folder path containing the files to be classified.
3. **View Results**: Check the folder structure to see files organized into respective categories.

## Code Explanation
- The script defines a dictionary `dict_extensions` where each key represents a file category and its corresponding tuple contains file extensions associated with that category.
- It prompts the user to input the folder path containing the files to be classified.
- The `file_finder` function is responsible for finding files with specified extensions within the given folder path.
- It iterates through each category in `dict_extensions`, finds files with corresponding extensions, creates folders if necessary, and moves the files into their respective folders.

## Example
Suppose you have a folder containing various files like `music.mp3`, `video.mp4`, `image.png`, `document.pdf`, and `software.exe`. After running the script, it will organize these files into separate folders named `AudioFiles`, `VideoFiles`, `ImagesFiles`, `DocumentFiles`, and `SoftwareFiles`, respectively.

## Note
- Ensure to review and customize the `dict_extensions` dictionary according to your specific file categorization requirements.

## Contributors
- Darshan Patil
- https://www.linkedin.com/in/patil-darshan/

