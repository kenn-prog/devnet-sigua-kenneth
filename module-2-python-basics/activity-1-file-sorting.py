"""
Module 2 — Activity: File Sorting with os and shutil
Student: Kenneth Sigua
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a file sorting script that organizes files
in a specific folder into subfolders based on their file extensions.
The file are moved based on their type like images, documents,
videos, audio, and others. If a file doesnt match of any type,
it will move to the "others" folder. The script uses the os and shutil modules
to handle file and directory operations, making it easy to automatic 
organize the files in a folder.



============================================
KEY VOCABULARY
============================================
- os module: It is used to work with files, folders, and file paths. 
- shutil module: It is used to move and copy a files and folders.
- file path: Its a folder or file that where it locate in the computer.
- directory: Its a folder that contains files and other folders.
- file extension: It tells the type of the file by looking at the last part of 
the file name after the dot like .jpg, .pdf, .mp3, and others.


============================================
YOUR SCRIPT
============================================

"""

import os
import shutil

source_folder = "files"

folders = {
    "images": ["jpg", "jpeg", "png", "gif"],
    "documents": ["pdf", "docx", "txt"],
    "videos": ["mp4", "avi", "mov"],
    "audio": ["mp3", "wav"],
    "others": [],
}

for folder in folders:
    folder_path = os.path.join(source_folder, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(source_folder):
    file_path =os.path.join(source_folder, filename )
    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()

    moved = False

    for folder, extensions in folders.items():
        if extension in extensions:
            destination = os.path.join(source_folder, folder)
            shutil.move(file_path, destination)

            print(f"Moved {filename} to {folder}")
            moved = True
            break

    if not moved:
        destination = os.path.join(source_folder, "others", filename)
        shutil.move(file_path, destination)

        print(f"Moved {filename} to others")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake i done is not checking the folder path before moving the files.
if the folder path is incorrect or not exits the srcipt will show and error  and
will not move the files.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects to a real automation because like this script or program that use
os module and shutil module able to automatically organize files in a folder without
manually moving them. This can be useful for organizing files in a computer or server.
"""
