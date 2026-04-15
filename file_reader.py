"""
Reads the JSON and CSV files to create 
the dictionaries that will be used
to insert the employee data and their 
workdays in the database.
"""

import csv

'''
Key values for the dictionares
Matches the name of the respective database column
'''
_employee_id_sql = "employee_id"
_first_name_sql = "first_name"
_last_name_sql = "last_name"
_clock_in_date_sql = "clock_in_date"
_total_hours_sql = "total_hours"
_job_code_sql = "job_code"
_pay_code_sql = "pay_code"
 

def create_timestamps():
    """
    Filters out the created dictionary list and
    appends each instance of the 
    agency employee timestamps to a new list

    Returns:
        list[dict]: List of agency timestamp dictionaries
        containing employee id, work date, and total hours 
    """

    employee_dict = _create_dictionary()

    filtered_list = [{_employee_id_sql: employee.get(_employee_id_sql),
                     _clock_in_date_sql: employee.get(_clock_in_date_sql),
                     _total_hours_sql: employee.get(_total_hours_sql),
                     _job_code_sql: employee.get(_job_code_sql),
                     _pay_code_sql: employee.get(_pay_code_sql)} 
                     for employee in employee_dict]
    
    return filtered_list


def _create_dictionary():
    """
    Reads the CSV file containing the agency employee data
    and workdays and appends the data to a dictionary list.

    Returns:
        list[dict]: List of dictionaries containing the employee data
    """

    user_id_column = "employeeId"
    clock_in_date_column = "date"
    total_hours_column = "hours"
    jobe_tite_code_column = "jobTitleCode"
    pay_type_code_column = "payTypeCode"
    
    dict_list = []

    with open("PBJ Report.csv", "r") as excel_file:
        csv_file = csv.DictReader(excel_file)

        for line in csv_file:
            id = line.get(user_id_column)
            clock_in_date = line.get(clock_in_date_column)
            total_hours = float(line.get(total_hours_column))
            job_title_code = line.get(jobe_tite_code_column)
            pay_type_code = line.get(pay_type_code_column)

            dict_data = {_employee_id_sql: id, _clock_in_date_sql: clock_in_date,
                         _first_name_sql: None, _last_name_sql: None,
                         _total_hours_sql: total_hours, 
                         _job_code_sql: job_title_code, _pay_code_sql: pay_type_code}

            dict_list.append(dict_data)

    return dict_list