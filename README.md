# Magic PDF

This is a simple GUI application to manipulate PDF files using `tkinter`, `pypdf`, and `Pillow` libraries.

![Python CI](https://github.com/silvos590/magicpdf/actions/workflows/python-ci.yml/badge.svg)

## Features

- **PDF Compression**: Compress PDF files by resizing images within the PDF and compressing the text.
- **PDF Merging**: Merge multiple PDF files into a single PDF.
- **PDF Rotation**: Rotate a PDF by 90, 180, or 270 degrees.

## Requirements

- Python 3.x
- `pypdf` library
- `Pillow` library
- `tkinter` library (usually included with Python installations)

## Installation

1. Clone the repository or download the `MagicPDF.py` script.
2. Install the required libraries using pip:

```bash
pip install pypdf Pillow
```

## Usage

Run the script using Python:

```bash
python MagicPDF.py
```

### PDF Compression

1. Select the "Compress PDF" option from the File menu.
2. Browse and select the input PDF file.
3. Specify the output PDF file name.
4. Enter the compression level (1-100, where 100 is the highest compression -> less quality).
5. Click the "Compress PDF" button.

### PDF Merging

1. Select the "Merge PDFs" option from the File menu.
2. Browse and select the input PDF files. You can select multiple files by holding the Ctrl key (Cmd key on macOS) while selecting.
3. Specify the output PDF file name.
4. Click the "Merge PDFs" button.

### PDF Rotation

1. Select the "Rotate PDF" option from the File menu.
2. Browse and select the input PDF file.
3. Specify the output PDF file name.
4. Enter the degrees level (90, 180, or 270 - default 90).
5. Click the "Rotate PDF" button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Distribution

Is it possible to use Pyinstaller to distribute MagicPDF as an .exe:

```bash
python -m PyInstaller --onefile --windowed --icon=assets/logo.png --add-data "assets;assets" MagicPDF.py
```

## Acknowledgments

- [pypdf](https://pypi.org/project/pypdf/) - A library to manipulate PDF files.
- [Pillow](https://pypi.org/project/Pillow/) - A library for image processing.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit.
- [PyInstaller](https://pypi.org/project/pyinstaller/) - PyInstaller bundles a Python application and all its dependencies into a single package.
