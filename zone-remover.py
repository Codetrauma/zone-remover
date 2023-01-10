import os
import tkinter as tk
from tkinter import filedialog


def remove_zone_identifier(directory):
    counter = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".Identifier" in file:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    counter += 1
                except:
                    print(f"File not found: {file_path}")
    return counter


# Create the GUI
root = tk.Tk()
root.withdraw()

# Ask the user to select a directory
directory = filedialog.askdirectory()

# Test the function
deleted_files = remove_zone_identifier(directory)
print(f'Deleted {deleted_files} files.')
