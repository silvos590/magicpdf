import sys, os

# add parent to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils

import unittest
import sys
import os
from unittest import mock

class TestUtils(unittest.TestCase):

    # @mock.patch('sys._MEIPASS', new='/tmp/fake_meipass')
    # def test_resource_path_pyinstaller(self):
    #     # Simulate running in PyInstaller bundle
    #     rel_path = 'data/file.txt'
    #     expected = os.path.join('/tmp/fake_meipass', rel_path)
    #     self.assertEqual(resource_path(rel_path), expected)

    # @mock.patch('os.path.abspath')
    # def test_resource_path_dev(self, mock_abspath):
    #     # Simulate running in dev mode
    #     mock_abspath.return_value = '/home/user/project'
    #     rel_path = 'assets/img.png'
    #     expected = os.path.join('/home/user/project', rel_path)
    #     # Remove _MEIPASS if present
    #     if hasattr(sys, '_MEIPASS'):
    #         del sys._MEIPASS
    #     self.assertEqual(resource_path(rel_path), expected)

    @mock.patch('tkinter.filedialog.askopenfilename')
    def test_browse_file(self, mock_askopenfilename):
        mock_askopenfilename.return_value = '/path/to/file.pdf'
        mock_entry = mock.Mock()
        utils.browse_file(mock_entry)
        mock_entry.delete.assert_called_once_with(0, mock.ANY)
        mock_entry.insert.assert_called_once_with(0, '/path/to/file.pdf')

    @mock.patch('tkinter.filedialog.askopenfilenames')
    def test_browse_files(self, mock_askopenfilenames):
        mock_askopenfilenames.return_value = ['/file1.pdf', '/file2.pdf']
        mock_entry = mock.Mock()
        utils.browse_files(mock_entry)
        mock_entry.delete.assert_called_once_with(0, mock.ANY)
        mock_entry.insert.assert_called_once_with(0, '/file1.pdf;/file2.pdf')

if __name__ == '__main__':
    unittest.main()