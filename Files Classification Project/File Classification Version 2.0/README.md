# File Modifier (Version 2)

## Overview
The File Modifier (Version 2) is an improved version of a Python script designed to organize files based on their extensions into categorized folders. This version introduces a graphical user interface (GUI) using the Tkinter library, allowing users to input the folder path directly and initiate the file sorting process with ease.

## Functionality
The script performs the following tasks:
1. **GUI Interface**: It provides a simple GUI where users can input the folder path.
2. **File Classification**: The script categorizes files based on their extensions into predefined categories such as Word, HTML, PDF, Excel, Other, PPT, and Text.
3. **Folder Creation**: It creates folders for each category if files with corresponding extensions are found.
4. **File Movement**: Files are then moved from the original folder to their respective categorized folders.

## Features
- **Graphical User Interface**: Users interact with the script through a user-friendly GUI, eliminating the need for command-line inputs.
- **Customizable Extensions**: Users can customize the file extensions and their corresponding categories to suit their specific needs.
- **Efficient File Handling**: The script efficiently handles file movement and organization, simplifying the process of file sorting.

## Usage
1. **Run Script**: Execute the Python script, and the GUI window will appear.
2. **Input Folder Path**: Enter the folder path containing the files to be classified in the provided entry box.
3. **Submit**: Click the "Submit" button to initiate the file sorting process.
4. **View Results**: Check the folder structure to see files organized into respective categories.

## Code Explanation
- The script utilizes the Tkinter library to create a GUI window with a label, an entry box for inputting the folder path, and a submit button.
- Upon clicking the submit button, the script attempts to change the current working directory to the specified path and then initiates the file sorting process.
- The `file_modifier` function iterates through each file in the directory, categorizes files based on their extensions, creates folders if necessary, and moves the files into their respective folders.

## Example
Suppose you have a folder containing various files like `document.docx`, `code.py`, `presentation.pptx`, and `image.jpg`. After running the script and specifying the folder path, it will organize these files into separate folders named `Word_files`, `Other_files`, `PPT_files`, and `text_files`, respectively.

## Note
- Ensure to review and customize the `extension` dictionary according to your specific file categorization requirements.

## Contributors
- Darshan Patil
- https://www.linkedin.com/in/patil-darshan/