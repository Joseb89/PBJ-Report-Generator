import xml.etree.ElementTree as ET
import mysql_connection

_user_ids = mysql_connection.get_employee_ids()

def create_employees(root):
    employees = ET.SubElement(root, 'employees')

    for id in _user_ids:
        employee = ET.SubElement(employees, 'employee')

        employeeId = ET.SubElement(employee, 'employeeId')
        employeeId.text = str(id)

def create_work_days(root):
    staffing_hours = ET.SubElement(root, 'staffingHours')
    staffing_hours.set("processType", "merge")

    for id in _user_ids:
        staff_hours = ET.SubElement(staffing_hours, "staffHours")

        employee_id = ET.SubElement(staff_hours, "employeeId")
        employee_id.text = str(id)

        #work_days = mysql_connection.get_employee_work_days(id)   