
from pypdf import PdfWriter, PdfReader
import io
import tkinter as tk
from tkinter import filedialog, messagebox, Menu

def compress_pdf(input_file, output_file, quality_level):
    try:
        pdf_writer = PdfWriter(clone_from=input_file)
        
        # apply quality
        for page in pdf_writer.pages:
            # This is for text PDF
            page.compress_content_streams()
            # This is for image PDF
            for img in page.images:
                img.replace(img.image, quality=quality_level)

        # Write the compressed PDF to the output file
        with open(output_file, "wb") as f_out:
            pdf_writer.write(f_out)

        messagebox.showinfo("Success", f"Compressed PDF saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def merge_pdfs(input_files, output_file):
    try:
        pdf_writer = PdfWriter()
        
        for input_file in input_files:
            pdf_reader = PdfReader(open(input_file, "rb"))
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

        with open(output_file, "wb") as f_out:
            pdf_writer.write(f_out)
        
        messagebox.showinfo("Success", f"Merged PDF saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    input_files_entry.delete(0, tk.END)
    input_files_entry.insert(0, ";".join(files))

def compress():
    input_file = input_entry.get()
    output_file = output_entry.get()
    quality_level = 100 if not quality_entry.get() else int(quality_entry.get()) 
    
    if not input_file or not output_file or not quality_level:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return
    
    compress_pdf(input_file, output_file, quality_level)

def merge():
    input_files = input_files_entry.get().split(";")
    output_file = output_merge_entry.get()
    
    if not input_files or not output_file:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return
    
    merge_pdfs(input_files, output_file)

def show_compress_frame():
    compress_frame.pack(fill='both', expand=True)
    merge_frame.pack_forget()

def show_merge_frame():
    merge_frame.pack(fill='both', expand=True)
    compress_frame.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Magic PDF")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Compress PDF", command=show_compress_frame)
file_menu.add_command(label="Merge PDFs", command=show_merge_frame)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create frames
compress_frame = tk.Frame(root)
merge_frame = tk.Frame(root)

# Compression Frame Components
tk.Label(compress_frame, text="Input PDF File:").grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(compress_frame, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
browse_button = tk.Button(compress_frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(compress_frame, text="Output PDF File:").grid(row=1, column=0, padx=10, pady=5)
output_entry = tk.Entry(compress_frame, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(compress_frame, text="Compression Level (1-10):").grid(row=2, column=0, padx=10, pady=5)
compression_entry = tk.Entry(compress_frame, width=10)
compression_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

compress_button = tk.Button(compress_frame, text="Compress PDF", command=compress)
compress_button.grid(row=3, columnspan=3, pady=10)

# Merge Frame Components
tk.Label(merge_frame, text="Input PDF Files:").grid(row=0, column=0, padx=10, pady=5)
input_files_entry = tk.Entry(merge_frame, width=50)
input_files_entry.grid(row=0, column=1, padx=10, pady=5)
browse_files_button = tk.Button(merge_frame, text="Browse", command=browse_files)
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