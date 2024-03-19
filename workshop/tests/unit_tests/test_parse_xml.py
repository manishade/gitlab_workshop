import os
import pytest
import unittest
from tests import parse_xml


class TestParseXml(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_parse_xml(self):
        try:
            input_file_name = os.path.join(os.path.dirname(__file__), "../input.xml")
            parse_xml.parse_xml(input_file_name)
        except Exception as e:
            self.fail(f"parse_xml() raised an Exception {e}")

    @pytest.mark.run(order=2)
    def test_output_xml_file(self):
        # Check if output file exists
        absolute_path = os.path.join(os.path.dirname(__file__), "output.txt")
        self.assertTrue(os.path.isfile(absolute_path),
                        f"Output File don't Exist. Execution Path: {absolute_path}")

    @pytest.mark.run(order=3)
    def test_output_xml_content(self):
        # Checking the content of the file
        absolute_path = os.path.join(os.path.dirname(__file__), "output.txt")
        with open(absolute_path, "r") as f:
            lines = f.read().splitlines()
        self.assertTrue("99.134.125.44" in lines,
                        f"Output File not correctly writen. Execution Path: {absolute_path}")


if __name__ == '__main__':
    unittest.main()
