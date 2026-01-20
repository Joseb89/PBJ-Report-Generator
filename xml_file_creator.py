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

        current_date = ''
        total_hours = 0

        for work_day in work_days:
            clock_in_date = str(work_day[2])
            clock_in_time = work_day[3].total_seconds() / 3600
            clock_out_date = str(work_day[4])
            clock_out_time = work_day[5].total_seconds() / 3600

            additional_hours = 0
            work_hours = 0

            if current_date != '' and current_date != clock_in_date:
                _create_hour_entries(employee_work_days, current_date, total_hours)

                current_date = clock_in_date
                total_hours = 0

            if clock_out_date == clock_in_date:
                work_hours = (clock_out_time - clock_in_time) - 0.3
                total_hours += work_hours

                current_date = clock_in_date

            else:
                additional_hours = 24 - clock_in_time
                total_hours += additional_hours

                _create_hour_entries(employee_work_days, clock_in_date, total_hours)

                total_hours = clock_out_time
                current_date = clock_out_date

        _create_hour_entries(employee_work_days, current_date, total_hours)

def _create_hour_entries(root, date, hours):
    new_work_day = ET.SubElement(root, "workDay")

    new_work_date = ET.SubElement(new_work_day, "date")
    new_work_date.text = date

    hour_entries = ET.SubElement(new_work_day, "hourEntries")

    hour_entry = ET.SubElement(hour_entries, "hourEntry")

    hour = ET.SubElement(hour_entry, "hours")
    hour.text = f"{hours:.2f}"
