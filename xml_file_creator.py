import xml.etree.ElementTree as ET
import datetime
import mysql_connection
import credentials

def create_databases():
    mysql_connection.insert_knopp_employees()
    mysql_connection.insert_agency_employees()
    mysql_connection.insert_admin_work_days()
    mysql_connection.insert_agency_work_days()

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

def create_employee_ids(root):
    employees = ET.SubElement(root, 'employees')

    all_employees = mysql_connection.get_knopp_employees() + mysql_connection.get_agency_employees()

    for emp in all_employees:
        user_id = emp[0]

        employee = ET.SubElement(employees, 'employee')

        employee_id = ET.SubElement(employee, 'employeeId')
        employee_id.text = str(user_id)

def create_agency_work_days(root):
    staffing_hours = ET.SubElement(root, 'staffingHours')
    staffing_hours.set("processType", "merge")

    agency_employees = mysql_connection.get_agency_employees()

    for emp in agency_employees:
        user_id = emp[0]
        job_code = emp[1]
        pay_code = emp[2]

        staff_hours = ET.SubElement(staffing_hours, "staffHours")

        employee_id = ET.SubElement(staff_hours, "employeeId")
        employee_id.text = str(user_id)

        employee_work_days = ET.SubElement(staff_hours, "workDays")

        work_days = mysql_connection.get_agency_work_days(user_id)

        current_date = ''
        work_hours = 0.00

        for work_day in work_days:
            clock_in_date = str(work_day[2])
            clock_in_time = work_day[3].total_seconds() / 3600
            clock_out_date = str(work_day[4])
            total_hours = work_day[6]

            print(total_hours)

            if current_date != '' and current_date != clock_in_date:
                _create_hour_entries(employee_work_days, current_date, work_hours, job_code, pay_code)

                current_date = clock_in_date
                work_hours = 0.00

            if clock_out_date == clock_in_date:
                work_hours += total_hours

                current_date = clock_in_date

            else:
                pm_hours = 24 - clock_in_time

                work_hours += pm_hours

                _create_hour_entries(employee_work_days, current_date, work_hours, job_code, pay_code)

                current_date = clock_out_date

                work_hours = total_hours - pm_hours

        _create_hour_entries(employee_work_days, current_date, work_hours, job_code, pay_code)


def _create_hour_entries(root, date, hours, job_code, pay_code):
    new_work_day = ET.SubElement(root, "workDay")

    new_work_date = ET.SubElement(new_work_day, "date")
    new_work_date.text = date

    hour_entries = ET.SubElement(new_work_day, "hourEntries")

    hour_entry = ET.SubElement(hour_entries, "hourEntry")

    hour = ET.SubElement(hour_entry, "hours")
    hour.text = f"{hours:.2f}"

    job_title_code = ET.SubElement(hour_entry, "jobTitleCode")
    job_title_code.text = str(job_code)

    pay_type_code = ET.SubElement(hour_entry, "payTypeCode")
    pay_type_code.text = str(pay_code)