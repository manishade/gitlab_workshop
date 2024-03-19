import os
from lxml import etree
filename = "input.xml"


def parse_xml(input_file_name: str = filename, output_file: str = "unit_tests/output.txt"):
    """
    Function that parses a xml input file and prints out an output
    :param input_file_name: name of the file to parse (optional)
    :type input_file_name: str
    :param output_file: name of the output file
    :type output_file: str
    """
    parser = etree.XMLParser()
    tree = etree.parse(input_file_name, parser)
    name_servers = tree.xpath("/config/epg/pgw/apn/name-server/name/text()")

    absolute_path = os.path.join(os.path.dirname(__file__), output_file)
    with open(absolute_path, "w+") as file:
        for name_server in name_servers:
            print(f"writing {name_server} to file")
            file.write(name_server+"\n")


if __name__ == '__main__':
    parse_xml(filename)
