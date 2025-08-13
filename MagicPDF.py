import os
import sys
import tkinter as tk
from tkinter import messagebox, Menu
from utils import browse_file, browse_files
from functionalities import rotate_pdf, compress_pdf, merge_pdfs

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and PyInstaller) """
    try:
        base_path = sys._MEIPASS  # when packaged
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def rotate():
    input_rotate_file = input_rotate_entry.get()
    output_rotate_file = output_rotate_entry.get()
    rotation = None if not rotation_entry.get() else int(rotation_entry.get())

    if not input_rotate_file or not output_rotate_file or not rotation:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    try:
        rotate_pdf(input_rotate_file, output_rotate_file, rotation, page_numbers=None)
        messagebox.showinfo("Success", f"Rotated PDF saved as {output_rotate_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def compress():
    input_file = input_entry.get()
    output_file = output_entry.get()
    quality_level = 100 if not compression_entry.get() else int(compression_entry.get())

    if not input_file or not output_file or not quality_level:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    try:
        compress_pdf(input_file, output_file, quality_level)
        messagebox.showinfo("Success", f"Compressed PDF saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def merge():
    input_files = input_files_entry.get().split(";")
    output_file = output_merge_entry.get()

    if not input_files or not output_file:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    try:
        merge_pdfs(input_files, output_file)
        messagebox.showinfo("Success", f"Merged PDF saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_compress_frame():
    compress_frame.pack(fill='both', expand=True)
    forget_all_frames(root, compress_frame)

def show_rotate_frame():
    rotate_frame.pack(fill='both', expand=True)
    forget_all_frames(root, rotate_frame)

def show_merge_frame():
    merge_frame.pack(fill='both', expand=True)
    forget_all_frames(root, merge_frame)

def forget_all_frames(parent, current):
    for widget in parent.winfo_children():
        if  widget != current:
            widget.pack_forget()   # or widget.grid_forget(), widget.place_forget()

# Create the main window
root = tk.Tk()
root.title("Magic PDF")
root.iconphoto(False, tk.PhotoImage(file=resource_path("assets/logo.png")))

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Compress PDF", command=show_compress_frame)
file_menu.add_command(label="Rotate PDF", command=show_rotate_frame)
file_menu.add_command(label="Merge PDFs", command=show_merge_frame)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Add Credits
menu_bar.add_command(label="Credits",
                     command=lambda:
                     messagebox.showinfo(title="Credits", message="Coded by Aldo Mollica: https://github.com/silvos590"))

# Create frames
compress_frame = tk.Frame(root)
rotate_frame = tk.Frame(root)
merge_frame = tk.Frame(root)

# Compression Frame Components
tk.Label(compress_frame, text="Input PDF File:").grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(compress_frame, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
browse_button = tk.Button(compress_frame, text="Browse", command=lambda: browse_file(input_entry))
browse_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(compress_frame, text="Output PDF File:").grid(row=1, column=0, padx=10, pady=5)
output_entry = tk.Entry(compress_frame, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(compress_frame, text="Compression Level (1-100):").grid(row=2, column=0, padx=10, pady=5)
compression_entry = tk.Entry(compress_frame, width=10)
compression_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

compress_button = tk.Button(compress_frame, text="Compress PDF", command=compress)
compress_button.grid(row=3, columnspan=3, pady=10)

# Rotate Frame Components
tk.Label(rotate_frame, text="Input PDF File:").grid(row=0, column=0, padx=10, pady=5)
input_rotate_entry = tk.Entry(rotate_frame, width=50)
input_rotate_entry.grid(row=0, column=1, padx=10, pady=5)
browse_rotate_button = tk.Button(rotate_frame, text="Browse", command=lambda: browse_file(input_rotate_entry))
browse_rotate_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(rotate_frame, text="Output PDF File:").grid(row=1, column=0, padx=10, pady=5)
output_rotate_entry = tk.Entry(rotate_frame, width=50)
output_rotate_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(rotate_frame, text="Rotation (90, 180, or 270 degrees):").grid(row=2, column=0, padx=10, pady=5)
rotation_entry = tk.Entry(rotate_frame, width=10)
rotation_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
rotation_entry.insert(0, "90")

rotate_button = tk.Button(rotate_frame, text="Rotate PDF", command=rotate)
rotate_button.grid(row=2, columnspan=3, pady=10)

# Merge Frame Components
tk.Label(merge_frame, text="Input PDF Files:").grid(row=0, column=0, padx=10, pady=5)
input_files_entry = tk.Entry(merge_frame, width=50)
input_files_entry.grid(row=0, column=1, padx=10, pady=5)
browse_files_button = tk.Button(merge_frame, text="Browse", command=lambda: browse_files(input_files_entry))
browse_files_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(merge_frame, text="Output PDF File:").grid(row=1, column=0, padx=10, pady=5)
output_merge_entry = tk.Entry(merge_frame, width=50)
output_merge_entry.grid(row=1, column=1, padx=10, pady=5)

merge_button = tk.Button(merge_frame, text="Merge PDFs", command=merge)
merge_button.grid(row=2, columnspan=3, pady=10)

# Show compress frame by default
show_compress_frame()

# Run the Tkinter event loop
root.mainloop()
