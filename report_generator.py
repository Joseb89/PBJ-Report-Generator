import xml.etree.ElementTree as ET
from zipfile import ZipFile

import header
import mysql_connection
import excel


def main():
    data = ET.Element('nursingHomeData')

    header.create_header(data)

    tree = ET.ElementTree(data)

    ET.indent(tree, '  ')

    file_name = "report.xml"
    excel.create_json_file()

    # tree.write(file_name, encoding="us-ascii", xml_declaration=True)

    # with ZipFile("PBJ_Report_Generator.zip", "w") as zip_file:
    #     zip_file.write(file_name)


if __name__ == "__main__":
    main()
