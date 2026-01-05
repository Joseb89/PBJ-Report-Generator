import xml.etree.ElementTree as ET
import mysql_connection

def create_employees(root):
    user_ids = mysql_connection.get_employee_ids()

    employees = ET.SubElement(root, 'employees')

    for id in user_ids:
        employee = ET.SubElement(employees, 'employee')

        employeeId = ET.SubElement(employee, 'employeeId')
        employeeId.text = str(id)