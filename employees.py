import xml.etree.ElementTree as ET
import excel
import math

def create_employees(root):
    user_ids_set = set()

    for x in excel.user_ids_list:
        if math.isnan(x):
            continue

        user_ids_set.add(str(int(x)))

    employees = ET.SubElement(root, 'employees')

    for x in user_ids_set:
        employee = ET.SubElement(employees, 'employee')

        employeeId = ET.SubElement(employee, 'employeeId')
        employeeId.text = x