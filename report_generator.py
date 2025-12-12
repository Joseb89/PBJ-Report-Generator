import xml.etree.ElementTree as ET
import header

def main():
    data = ET.Element('nursingHomeData')

    header.create_header(data)

    tree = ET.ElementTree(data)

    ET.indent(tree, '  ')

    tree.write("report.xml", encoding="us-ascii", xml_declaration=True)

if __name__ == "__main__":
    main()    