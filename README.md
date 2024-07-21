# Magic PDF

This is a simple GUI application to compress and merge PDF files using `tkinter`, `PyPDF2`, and `Pillow` libraries.

## Features

- **PDF Compression**: Compress PDF files by resizing images within the PDF.
- **PDF Merging**: Merge multiple PDF files into a single PDF.

## Requirements

- Python 3.x
- `PyPDF2` library
- `Pillow` library
- `tkinter` library (usually included with Python installations)

## Installation

1. Clone the repository or download the `MagicPDF.py` script.
2. Install the required libraries using pip:

```bash
pip install PyPDF2 Pillow
```

## Usage

Run the script using Python:

```bash
python pdf_utility_ui.py
```

### PDF Compression

1. Select the "Compress PDF" option from the File menu.
2. Browse and select the input PDF file.
3. Specify the output PDF file name.
4. Enter the compression level (1-10, where 10 is the highest compression).
5. Click the "Compress PDF" button.

### PDF Merging

1. Select the "Merge PDFs" option from the File menu.
2. Browse and select the input PDF files. You can select multiple files by holding the Ctrl key (Cmd key on macOS) while selecting.
3. Specify the output PDF file name.
4. Click the "Merge PDFs" button.

## Screenshots

### Main Window
![Main Window](screenshots/main_window.png)

### PDF Compression
![PDF Compression](screenshots/compress_window.png)

### PDF Merging
![PDF Merging](screenshots/merge_window.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

- [PyPDF2](https://pypi.org/project/PyPDF2/) - A library to manipulate PDF files.
- [Pillow](https://pypi.org/project/Pillow/) - A library for image processing.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit.

### Additional Notes

- You can create a `screenshots` directory and add images of your application's UI to enhance the README file. Update the paths in the `Screenshots` section accordingly.
- Ensure that the license mentioned matches the actual license used in your project. The above example assumes an MIT License.

Save the above content into a file named `README.md` in the same directory as your script.
