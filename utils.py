from tkinter import filedialog
import tkinter as tk

def browse_file(input_entry):
    """Open a file dialog to select a PDF file"""
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_files(input_files_entry):
    """ Open a file dialog to select multiple PDF files"""
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    input_files_entry.delete(0, tk.END)
    input_files_entry.insert(0, ";".join(files))
