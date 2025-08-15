import os
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
    if not input_file or not output_file:
        raise ValueError("Invalid input or output file")

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

    if quality_level is None or quality_level < 1 or quality_level > 100:
        raise ValueError("Invalid quality level. Please choose a value between 1 and 100.")

    pdf_writer = PdfWriter(clone_from=input_file)

    # apply quality
    for page in pdf_writer.pages:
        # Map quality level input [1-100] to [1-10]
        text_quality = (quality_level // 10) + 1
        # This is for text PDF
        page.compress_content_streams(level=text_quality)
        # This is for image PDF
        for img in page.images:
            img.replace(img.image, quality=quality_level)

    # Write the compressed PDF to the output file
    with open(output_file, "wb") as f_out:
        pdf_writer.write(f_out)

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

def split_pdf(input_file, output_folder, page_ranges=None):
    """ Split input_file into multiple PDFs based on page_ranges"""
    if not input_file or not output_folder:
        raise ValueError("Invalid input file or output folder")

    reader = PdfReader(input_file)

    if page_ranges is None or not page_ranges:
        # If no page ranges are specified, split by individual pages
        page_ranges = [f"{i+1}-{i+1}" for i in range(len(reader.pages))]
        # print(f"Splitting into individual pages: {page_ranges}")

    for r in page_ranges:
        writer = PdfWriter()
        # if r is made by only one number, start and end are set to the same value
        if '-' not in r:
            r = f"{r}-{r}"

        start, end = map(int, r.split('-'))
        # print(f"Splitting pages {start} to {end} from {input_file} into {output_folder}")
        for num in range(start, end + 1):
            writer.add_page(reader.pages[num - 1])
        output_file = os.path.join(output_folder, f"page_{start}_to_{end}.pdf")
        with open(output_file, "wb") as f_out:
            writer.write(f_out)
