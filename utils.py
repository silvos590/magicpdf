from tkinter import filedialog
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and PyInstaller) """
    try:
        base_path = sys._MEIPASS  # when packaged
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def browse_file(input_entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_files(input_files_entry):
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    input_files_entry.delete(0, tk.END)
    input_files_entry.insert(0, ";".join(files))