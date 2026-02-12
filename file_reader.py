import csv
import json
import credentials

from datetime import datetime, timedelta

_employee_id_sql = "employee_id"
_first_name_sql = "first_name"
_last_name_sql = "last_name"
_clock_in_date_sql = "clock_in_date"
_total_hours_sql = "total_hours"
_job_code_sql = "job_code"
_pay_code_sql = "pay_code"

def create_knopp_employees():
    employee_dict_list = []

    with open("employee.json", "r") as json_file:
        json_dict = json.load(json_file)
        
        for employee_json in json_dict:
            modified_json_dict = {_employee_id_sql: employee_json.get("id"),
                                  _first_name_sql: employee_json.get("firstName"),
                                  _last_name_sql: employee_json.get("lastName"),
                                  _job_code_sql: employee_json.get("jobTitleCode"),
                                  _pay_code_sql: 2}
            
            employee_dict_list.append(modified_json_dict)

    return employee_dict_list         


def create_agency_employees():
    employee_dict_list = []

    employee_dict = _create_agency_dictionary()

    id_set = set()       

    for employee in employee_dict:
        id_set.add(employee[_employee_id_sql])

    current = ''   

    while id_set:
        top = id_set.pop()

        if top == current:
            continue

        first_occurence = next((dic for dic in employee_dict if dic[_employee_id_sql] == top), None)

        filtered_dict = {_employee_id_sql: first_occurence.get(_employee_id_sql),
                         _first_name_sql: first_occurence.get(_first_name_sql),
                         _last_name_sql: first_occurence.get(_last_name_sql), 
                         _total_hours_sql: first_occurence.get(_total_hours_sql),
                         _job_code_sql: first_occurence.get(_job_code_sql),
                         _pay_code_sql: first_occurence.get(_pay_code_sql)} 

        employee_dict_list.append(filtered_dict)

        current = top

    return employee_dict_list


def create_admin_timestamps():
    admin_timestamps = []

    start_date = datetime(2025, 10, 1)
    end_date = datetime(2026, 1, 1)

    current_date = start_date

    while current_date != end_date:
        if current_date.weekday()  == 5 or current_date.weekday() == 6:
            current_date += timedelta(days=1)

            continue

        timepstamp_dict = {_employee_id_sql: credentials.admin_id, 
                           _clock_in_date_sql: current_date,
                           _total_hours_sql: 8.00}
        
        admin_timestamps.append(timepstamp_dict)

        current_date += timedelta(days=1)

    return admin_timestamps   

def create_agency_timestamps():
    employee_dict = _create_agency_dictionary()

    filtered_list = [{_employee_id_sql: employee.get(_employee_id_sql),
                     _clock_in_date_sql: employee.get(_clock_in_date_sql),
                     _total_hours_sql: employee.get(_total_hours_sql)} 
                     for employee in employee_dict]
    
    return filtered_list


def _create_agency_dictionary():
    user_id_column = "employeeId"
    clock_in_date_column = "date"
    total_hours_column = "hours"
    jobe_tite_code_column = "jobTitleCode"
    
    dict_list = []

    with open("PBJ Report.csv", "r") as excel_file:
        csv_file = csv.DictReader(excel_file)

        for line in csv_file:
            id = line.get(user_id_column)
            clock_in_date = line.get(clock_in_date_column)
            total_hours = float(line.get(total_hours_column))
            job_title_code = line.get(jobe_tite_code_column)

            dict_data = {_employee_id_sql: id, _clock_in_date_sql: clock_in_date,
                         _first_name_sql: None, _last_name_sql: None,
                         _total_hours_sql: total_hours, _job_code_sql: job_title_code, _pay_code_sql: 3}

            dict_list.append(dict_data)

    return dict_list