import xml.etree.ElementTree as ET
import mysql_connection

def create_employees(root):
    user_ids = mysql_connection.get_employee_ids()

    employees = ET.SubElement(root, 'employees')

    for id in user_ids:
        employee = ET.SubElement(employees, 'employee')

        employeeId = ET.SubElement(employee, 'employeeId')
        employeeId.text = str(id)

def create_work_days():
    user_ids = mysql_connection.get_employee_ids()

    user_id_list = []

    for id in user_ids:
        work_days = mysql_connection.get_employee_work_days(id)

        user_id_list.append(work_days)

    return user_id_list    