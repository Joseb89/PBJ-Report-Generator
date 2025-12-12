import xml.etree.ElementTree as ET
import excel


def define_staffing_hours(root):
    staffing_hours = ET.SubElement(root, 'staffingHours')
    staffing_hours.set('processType', 'merge')

    employee_ids = excel.user_ids_list

    current_user_id = employee_ids.get(0)

    employee_staffing_hours(current_user_id, staffing_hours)

    while employee_ids:
        user_id = employee_ids.pop(0)
        
        if(current_user_id != user_id):
            current_user_id = user_id

def employee_staffing_hours(user_id, root):
        staff_hours = ET.SubElement(root, 'staffHours')

        employee_id = ET.SubElement(staff_hours, 'employeeId')
        employee_id.text = str(user_id)
                   