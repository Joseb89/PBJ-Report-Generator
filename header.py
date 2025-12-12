import xml.etree.ElementTree as ET

def create_header(root):
    header = ET.SubElement(root, 'header')
    header.set('fileSpecVersion', '4.00.0')

    facilityId = ET.SubElement(header, 'facilityId')
    facilityId.text = '5025'

    stateCode = ET.SubElement(header, 'stateCode')
    stateCode.text = 'TX'

    reportQuarter = ET.SubElement(header, 'reportQuarter')
    reportQuarter.text = '4'

    federalFiscalYear = ET.SubElement(header, 'federalFiscalYear')
    federalFiscalYear.text = '2025'