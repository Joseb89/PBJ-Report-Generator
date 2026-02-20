import xml.etree.ElementTree as ET
import datetime
import mysql_connection
import credentials


def create_databases():
    mysql_connection.insert_employees()
    mysql_connection.insert_work_days()

def create_header(root):
    header = ET.SubElement(root, 'header')
    header.set('fileSpecVersion', '4.00.0')

    facility_id = ET.SubElement(header, 'facilityId')
    facility_id.text = credentials.facility_id

    state_code = ET.SubElement(header, 'stateCode')
    state_code.text = 'TX'

    report_quarter = ET.SubElement(header, 'reportQuarter')
    report_quarter.text = '1'

    federal_fiscal_year = ET.SubElement(header, 'federalFiscalYear')
    federal_fiscal_year.text = str(datetime.date.today().year)

def create_body(root):
    employees = ET.SubElement(root, 'employees')
    
    staffing_hours = ET.SubElement(root, 'staffingHours')
    staffing_hours.set("processType", "merge")

    user_work_days = mysql_connection.get_work_days()

    current_id = ''

    staff_hours = None
    staff_hour_entries = None
    work_days = None

    previous_date = ''

    for id, work_day, total_hours, job_code, pay_code in user_work_days:
        if id == None:
            continue

        if id != current_id:
            current_id = id

            employee = ET.SubElement(employees, "employee")

            employee_id = ET.SubElement(employee, "employeeId")
            employee_id.text = current_id

            staff_hours = ET.SubElement(staffing_hours, "staffHours")

            staff_employee_id = ET.SubElement(staff_hours, "employeeId")
            staff_employee_id.text = current_id

            work_days = ET.SubElement(staff_hours, "workDays")   

        staff_work_day = ET.SubElement(work_days, "workDay")

        if previous_date != '' and previous_date == work_day:
            _create_hour_entry(staff_hour_entries, total_hours, job_code, pay_code)

            continue 

        staff_date = ET.SubElement(staff_work_day, "date")
        staff_date.text = str(work_day)

        staff_hour_entries = ET.SubElement(staff_work_day, "hourEntries")

        _create_hour_entry(staff_hour_entries, total_hours, job_code, pay_code)

        previous_date = work_day

def _create_hour_entry(root, total_hours, job_code, pay_code):
    staff_hour_entry = ET.SubElement(root, "hourEntry")

    staff_total_hours = ET.SubElement(staff_hour_entry, "hours")
    staff_total_hours.text = f"{total_hours:.2f}"

    staff_job_title_code = ET.SubElement(staff_hour_entry, "jobTitleCode")
    staff_job_title_code.text = str(job_code)

    staff_pay_type_code = ET.SubElement(staff_hour_entry, "payTypeCode")
    staff_pay_type_code.text = str(pay_code)      