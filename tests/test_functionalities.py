import unittest
import sys
import os
# add parent to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from unittest.mock import patch
from pypdf import PdfWriter, PdfReader
from functionalities import rotate_pdf, compress_pdf, merge_pdfs

class TestFunctionalities(unittest.TestCase):
    """ Test cases for functionalities.py """

    def setUp(self):
        """ Set up test environment """
        # test PDF file
        path = "./"
        self.test_pdf = os.path.join(path, "test.pdf")
        self.sample_pdf1 = os.path.join(path, "sample1.pdf")
        self.sample_pdf2 = os.path.join(path, "sample2.pdf")
        self.merged_pdf = os.path.join(path, "merged.pdf")
        self.rotated_pdf = os.path.join(path, "rotated.pdf")
        self.compressed_pdf = os.path.join(path, "compressed.pdf")
        self.compressed_pdf_2 = os.path.join(path, "compressed_2.pdf")

        writer1 = PdfWriter(clone_from=self.test_pdf)
        with open(self.sample_pdf1, "wb") as f:
            writer1.write(f)

        writer2 = PdfWriter(clone_from=self.test_pdf)
        with open(self.sample_pdf2, "wb") as f:
            writer2.write(f)

        writer1.close()
        writer2.close()

    def tearDown(self):
        # Remove generated files
        for f in [self.sample_pdf1,
                  self.sample_pdf2,
                  self.merged_pdf,
                  self.rotated_pdf,
                  self.compressed_pdf,
                  self.compressed_pdf_2]:
            if os.path.exists(f):
                os.remove(f)

    def test_merge_empty_list(self):
        with self.assertRaises(Exception):
            merge_pdfs([], self.merged_pdf)

    def test_merge_pdfs(self):
        try:
            merge_pdfs([self.sample_pdf1, self.sample_pdf2], self.merged_pdf)
        except Exception as e:
            self.fail(f"Merge failed: {e}")
        reader = PdfReader(self.merged_pdf)
        self.assertEqual(len(reader.pages), 2)
        reader.close()
        reader.stream.close()

    def test_rotate_pdf_invalid_file(self):
        with self.assertRaises(Exception):
            rotate_pdf("nonexistent.pdf", self.rotated_pdf)

    def test_rotate_pdf_all_pages(self):
        desired_rotation = 90
        rotate_pdf(self.sample_pdf1, self.rotated_pdf, rotation=desired_rotation)
        reader = PdfReader(self.rotated_pdf)
        # Check if page rotation is applied (rotation attribute exists)
        self.assertEqual(reader.pages[0]['/Rotate'], desired_rotation)

    def test_rotate_pdf_specific_page(self):
        desired_rotation = 180
        merge_pdfs([self.sample_pdf1, self.sample_pdf2], self.merged_pdf)
        rotate_pdf(self.merged_pdf, self.rotated_pdf, rotation=desired_rotation, page_numbers=[1])
        reader = PdfReader(self.rotated_pdf)
        # Only second page should be rotated
        self.assertEqual(reader.pages[0]['/Rotate'], 0)
        self.assertEqual(reader.pages[1]['/Rotate'], desired_rotation)

    def test_compress_pdf_invalid_file(self):
        with self.assertRaises(Exception):
            compress_pdf("nonexistent.pdf", self.compressed_pdf, quality_level=50)

    def test_compress_pdf_invalid_quality(self):
        with self.assertRaises(ValueError):
            compress_pdf(self.sample_pdf1, self.compressed_pdf, quality_level=0)
        with self.assertRaises(ValueError):
            compress_pdf(self.sample_pdf1, self.compressed_pdf, quality_level=101)

    def test_compress_pdf(self):
        compress_pdf(self.sample_pdf1, self.compressed_pdf, quality_level=10)
        self.assertTrue(os.path.exists(self.compressed_pdf))

        print(f"Sample PDF size: {os.path.getsize(self.sample_pdf1)} bytes")
        print(f"Compressed PDF size: {os.path.getsize(self.compressed_pdf)} bytes")
        # Check that compressed PDF is smaller than original
        self.assertTrue(os.path.getsize(self.compressed_pdf) < os.path.getsize(self.sample_pdf1))

        # Less compression
        compress_pdf(self.sample_pdf1, self.compressed_pdf_2, quality_level=50)
        self.assertTrue(os.path.exists(self.compressed_pdf_2))

        print(f"Sample PDF size: {os.path.getsize(self.sample_pdf1)} bytes")
        print(f"Compressed PDF size: {os.path.getsize(self.compressed_pdf_2)} bytes")
        # Check that compressed PDF is greater than the first compressed PDF
        self.assertTrue(os.path.getsize(self.compressed_pdf_2) > os.path.getsize(self.compressed_pdf))

if __name__ == "__main__":
    unittest.main()
