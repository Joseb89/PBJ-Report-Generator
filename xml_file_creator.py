import xml.etree.ElementTree as ET
import datetime
import mysql_connection
import credentials

from datetime import timedelta

_user_ids = mysql_connection.get_employee_ids()

def create_header(root):
    header = ET.SubElement(root, 'header')
    header.set('fileSpecVersion', '4.00.0')

    facility_id = ET.SubElement(header, 'facilityId')
    facility_id.text = credentials.facility_id

    state_code = ET.SubElement(header, 'stateCode')
    state_code.text = 'TX'

    report_quarter = ET.SubElement(header, 'reportQuarter')
    report_quarter.text = '4'

    federal_fiscal_year = ET.SubElement(header, 'federalFiscalYear')
    federal_fiscal_year.text = str(datetime.date.today().year)

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

        employee_work_days = ET.SubElement(staff_hours, "workDays") 

        work_days = mysql_connection.get_employee_work_days(id)

        for work_day in work_days:

            clock_in_date = str(work_day[2])
            clock_in_time = work_day[3]
            clock_out_date = str(work_day[4])
            clock_out_time = work_day[5]

            new_work_day = ET.SubElement(employee_work_days, "workDay")

            new_work_date = ET.SubElement(new_work_day, "date")
            new_work_date.text = clock_in_date

            hour_entries = ET.SubElement(new_work_day, "hourEntries")

            if clock_out_date == clock_in_date:
                total_hours = (clock_out_time.total_seconds() / 3600 - (clock_in_time.total_seconds() / 3600))

                hour_entry = ET.SubElement(hour_entries, "hourEntry")
                
                hour = ET.SubElement(hour_entry, "hours")
                hour.text = f"{total_hours: .2f}"

            else:
                new_work_date2 = ET.SubElement(new_work_day, "date")
                new_work_date2.text = clock_out_date          
