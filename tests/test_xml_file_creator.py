import xml.etree.ElementTree as ET

def test_create_header():
    xml_data = """
    <header fileSpecVersion="4.10.0">
        <facilityId>2222</facilityId>
        <stateCode>TX</stateCode>
        <reportQuarter>2</reportQuarter>
        <federalFiscalYear>2026</federalFiscalYear>
    </header>
    """
   
    root = ET.fromstring(xml_data)

    assert root.find("facilityId").text == "2222"
    assert root.find("stateCode").text == "TX"

def test_create_body(test_data):
    ids = set()

    data = ET.Element("nursingHomeData")

    employees = ET.SubElement(data, "employees")

    for id in test_data:
        ids.add(id)

    for set_id in ids:
        employee = ET.SubElement(employees, "employee")

        employee_id = ET.SubElement(employee, "employeeId")
        employee_id.text = set_id

    staffing_hours = ET.SubElement(data, "staffingHours")

    for test_id, work_day, total_hours, job_code, pay_code in test_data:
        staff_hours = ET.SubElement(staffing_hours, "staffHours")

        staff_employee_id = ET.SubElement(staff_hours, "employeeId")
        staff_employee_id.text = test_id

        staff_work_days = ET.SubElement(staff_hours, "workDays")

        staff_work_day = ET.SubElement(staff_work_days, "workDay") 

        staff_date = ET.SubElement(staff_work_day, "date")
        staff_date.text = str(work_day)

        staff_hour_entries = ET.SubElement(staff_work_day, "hourEntries")

        staff_hour_entry = ET.SubElement(staff_hour_entries, "hourEntry")

        staff_total_hours = ET.SubElement(staff_hour_entry, "hours")
        staff_total_hours.text = f"{total_hours:.2f}"

        staff_job_title_code = ET.SubElement(staff_hour_entry, "jobTitleCode")
        staff_job_title_code.text = str(job_code)

        staff_pay_type_code = ET.SubElement(staff_hour_entry, "payTypeCode")
        staff_pay_type_code.text = str(pay_code)

    root = data.find(".//staffHours")
    assert root.find("employeeId").text == "Elendil"

    test_date = root.find(".//workDays").find(".//workDay")
    assert test_date.find("date").text == "2026-01-02"      
