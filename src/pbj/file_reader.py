"""
Reads the .csv file to create 
the dictionaries that will be used
to insert the employee workdays in the database.
"""

import csv

def create_timestamps():
    """
    Reads the .csv file and stores the data in a dictionary list.

    Returns:
        list[dict]: List of timestamp dictionaries
        containing employee id, work date, total hours,
        job code, and pay code. 
    """
    
    dict_list = []

    with open("./PBJ-Report.csv", "r") as excel_file:
        csv_file = csv.DictReader(excel_file)

        for line in csv_file:
            id = line.get("employeeId")
            clock_in_date = line.get("date")
            total_hours = float(line.get("hours"))
            job_title_code = line.get("jobTitleCode")
            pay_type_code = line.get("payTypeCode")

            dict_data = {"employee_id": id, "clock_in_date": clock_in_date,
                         "total_hours": total_hours, 
                        "job_code": job_title_code, "pay_code": pay_type_code}

            dict_list.append(dict_data)

    return dict_list