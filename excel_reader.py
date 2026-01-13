import csv
from datetime import datetime

_employee_id_sql = "employee_id"
_first_name_sql = "first_name"
_last_name_sql = "last_name"
_clock_in_date_sql = "clock_in_date"
_clock_in_time_sql = "clock_in_time"
_clock_out_date_sql = "clock_out_date"
_clock_out_time_sql = "clock_out_time"
_job_code_sql = "job_code"
_pay_code_sql = "pay_code"

def create_employees():
    employee_dict = create_employee_dictionary()

    id_set = set()       

    for employee in employee_dict:
        id_set.add(employee[_employee_id_sql])

    filtered_list = []
    current = ''   

    while id_set:
        top = id_set.pop()

        if top == current:
            continue

        first_occurence = next((dic for dic in employee_dict if dic[_employee_id_sql] == top), None)

        filtered_dict = {_employee_id_sql: first_occurence.get(_employee_id_sql), 
                         _first_name_sql: first_occurence.get(_first_name_sql),
                         _last_name_sql: first_occurence.get(_last_name_sql),
                         _job_code_sql: first_occurence.get(_job_code_sql),
                         _pay_code_sql: first_occurence.get(_pay_code_sql)} 

        filtered_list.append(filtered_dict)

        current = top

    return filtered_list

def create_employee_timestamps():
    employee_dict = create_employee_dictionary()

    filtered_list = [{_employee_id_sql: employee.get(_employee_id_sql),
                     _clock_in_date_sql: employee.get(_clock_in_date_sql),
                     _clock_in_time_sql: employee.get(_clock_in_time_sql),
                     _clock_out_date_sql: employee.get(_clock_out_date_sql),
                     _clock_out_time_sql: employee.get(_clock_out_time_sql)} 
                     for employee in employee_dict]
    
    return filtered_list

def create_employee_dictionary():
    user_id_column = "User ID"
    nurse_name_column = "Provider"
    job_title_column = "Certification"
    clock_in_date_column = "Clock In Date"
    clock_out_date_column = "Clock Out Date"

    with open("PBJ Report.csv", "r") as file:
        csv_File = csv.DictReader(file)
        dict_list= []

        for line in csv_File:
            if line.get(nurse_name_column) == '':
                continue

            id = line.get(user_id_column)

            nurse_name = _set_name(line.get(nurse_name_column))
            first_name = nurse_name[1].strip()
            last_name = nurse_name[0].strip()

            clock_in_timestamp = _format_date(line.get(clock_in_date_column))
            clock_out_timestamp = _format_date(line.get(clock_out_date_column))
            
            clock_in_date = clock_in_timestamp[0].strip()
            clock_in_time = clock_in_timestamp[1].strip()

            clock_out_date = clock_out_timestamp[0].strip()
            clock_out_time = clock_out_timestamp[1].strip()

            job_tite_code = _set_job_title_code(line.get(job_title_column))
            
            dict_data = {_employee_id_sql: id, _first_name_sql: first_name, _last_name_sql: last_name,
                         _clock_in_date_sql: clock_in_date, _clock_out_date_sql: clock_out_date,
                         _clock_in_time_sql: clock_in_time, _clock_out_time_sql: clock_out_time,
                         _job_code_sql: job_tite_code, _pay_code_sql: 2}   

            dict_list.append(dict_data)

    return dict_list   

def _set_name(name):
    full_name = name.split(",")

    return full_name

def _set_job_title_code(job_title):
    job_titles = {"CNA": 10, "LVN": 9, "Medication Aide": 12}

    return job_titles.get(job_title)

def _format_date(date_string):
    format_string = "%m/%d/%Y, %I:%M %p"
    employee_timestamp = datetime.strptime(date_string, format_string)

    return employee_timestamp.strftime("%Y-%m-%d %H:%M").split()