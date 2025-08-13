from tkinter import messagebox
from pypdf import PdfWriter, PdfReader

def rotate_pdf(input_file, output_file, rotation=90, page_numbers=None):
    """
    Rotate pages in a PDF file.

    Parameters:
        input_path (str): Path to the input PDF.
        output_path (str): Path for the output (rotated) PDF.
        rotation (int): Degrees to rotate (90, 180, 270).
        page_numbers (list): Page numbers to rotate (0-indexed). Rotate all if None.
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        if page_numbers is None or i in page_numbers:
            rotated_page = page.rotate(rotation)
            writer.add_page(rotated_page)
        else:
            writer.add_page(page)

    with open(output_file, "wb") as f_out:
        writer.write(f_out)

def compress_pdf(input_file, output_file, quality_level):
    """ Compress input_file with quality_level into output_file"""
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
    """ Merge input_files into output_file"""
    if not input_files or not output_file:
        raise ValueError("Invalid input files or output file")

    pdf_writer = PdfWriter()

    for input_file in input_files:
        with open(input_file,'rb') as file:
            for page in PdfReader(file).pages:
                pdf_writer.add_page(page)

    with open(output_file, "wb") as f_out:
        pdf_writer.write(f_out)
