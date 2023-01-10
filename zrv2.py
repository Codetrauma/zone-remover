import os
import tkinter as tk
from tkinter import filedialog, messagebox


def remove_zone_identifier(directory):
    counter = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".Identifier" in file:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    counter += 1
                except:
                    pass
    return counter


# Create the main window
root = tk.Tk()
root.title("Remove Zone Identifiers")
root.geometry("500x100")

# Create a label
label = tk.Label(
    root, text="Select a directory to remove all .Identifier files from")
label.pack()


def select_directory():
    directory = filedialog.askdirectory()
    if not directory:
        return
    deleted_files = remove_zone_identifier(directory)
    messagebox.showinfo("Info", f'Deleted {deleted_files} files.')


# Create a button that opens a file dialog
select_directory_button = tk.Button(
    root, text="Select Directory", command=select_directory)
select_directory_button.pack()

# Start the main loop
root.mainloop()
