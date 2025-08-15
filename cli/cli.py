import argparse
import sys
import os
# add parent to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functionalities import merge_pdfs, split_pdf, rotate_pdf, compress_pdf

def check_range(value: str) -> int:
    """Validate that input is an integer between 1 and 100."""
    ivalue = int(value)
    if ivalue is None or ivalue < 1 or ivalue > 100:
        raise argparse.ArgumentTypeError(f"{value} is not in range 1–100")
    return ivalue

def convert_to_page_ranges(value: str) -> list:
    return value.split(";")

def main():
    parser = argparse.ArgumentParser(description="PDF manipulation CLI tool")
    parser.add_argument("action", help="Action to perform on the PDF(s)")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", help="Output PDF file")
    parser.add_argument("--page_ranges", type=convert_to_page_ranges, help="Page ranges to split the PDF (e.g., '1-3;5;7-9')")
    parser.add_argument("--rotation_angle", type=int, choices=[90, 180, 270], help="Angle to rotate the PDF (e.g., 90, 180, 270)")
    parser.add_argument("--quality_level", type=check_range, help="Quality level (1-100)")

    args = parser.parse_args()

    try:
        if args.action == "merge":
            merge_pdfs(args.input, args.output)
        elif args.action == "split":
            split_pdf(args.input, args.output, args.page_ranges)
        elif args.action == "rotate":
            rotate_pdf(args.input, args.output, args.rotation_angle)
        elif args.action == "compress":
            compress_pdf(args.input, args.output, args.quality_level)
        else:
            print("Invalid action. Please choose from: merge, split, rotate, compress.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
