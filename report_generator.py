"""
The main class for exectuting the script to create the XML file.
"""

import xml.etree.ElementTree as ET
from zipfile import ZipFile

import xml_file_creator


def main():
    data = ET.Element('nursingHomeData')

    # xml_file_creator.create_databases()
    xml_file_creator.create_header(data)
    xml_file_creator.create_body(data)

    tree = ET.ElementTree(data)

    ET.indent(tree, '  ')

    file_name = "report.xml"

    tree.write(file_name, encoding="ASCII", xml_declaration=True)

    with ZipFile("PBJ_Report_Generator.zip", "w") as zip_file:
        zip_file.write(file_name)


if __name__ == "__main__":
    main()
