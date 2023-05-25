from PyPDF4 import PdfFileMerger
import tkinter as tk
from tkinter import filedialog
import os

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt the user to select multiple PDF files
file_paths = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF Files", "*.pdf")])

# Create a PdfFileMerger instance
merger = PdfFileMerger()

# Merge the selected PDF files
for file_path in file_paths:
    merger.append(file_path)

# Prompt the user to specify the output file name
output_file = filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

# Write the merged PDF to the output file
merger.write(output_file)
merger.close()

# Prompt the user to decide whether to remove the original files or not
remove_originals = input("Do you want to remove the original files? (y/n): ")

if remove_originals.lower() == "y":
    # Remove the individual PDF files
    for file_path in file_paths:
        os.remove(file_path)
    print("Original files removed.")
else:
    print("Original files not removed.")

print("Merging complete. Output file: {}".format(output_file))
