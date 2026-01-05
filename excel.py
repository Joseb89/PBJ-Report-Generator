import csv
from datetime import datetime

def create_employee_dictionary():

    with open("PBJ Report.csv", "r") as file:
        csv_File = csv.DictReader(file)
        dict_list= []

        for line in csv_File:
            if line.get("Provider") == '':
                continue

            id = line.get("User ID")
            first_name = _set_name(line.get("Provider"))[1].strip()
            last_name = _set_name(line.get("Provider"))[0]
            job_tite_code = _set_job_title_code(line.get("Certification"))
            
            clock_in_date = _format_date(line.get("Clock In Date"))
            clock_out_date = _format_date(line.get("Clock Out Date"))
            
            dict_data = {"employee_id": id, "first_name": first_name, "last_name": last_name,
                         "job_code": job_tite_code, "pay_code": 2}   

            dict_list.append(dict_data)

    id_set = set()       

    for x in dict_list:
        id_set.add(x["employee_id"])

    filtered_list = []
    current = ''   

    while id_set:
        top = id_set.pop()

        if top == current:
            continue

        first_occurence = next((dic for dic in dict_list if dic["employee_id"] == top), None)  

        filtered_list.append(first_occurence)

        current = top

    return filtered_list     

def _set_name(name):
    full_name = name.split(",")

    return full_name

def _set_job_title_code(job_title):
    job_titles = {"CNA": 10, "LVN": 9, "Medication Aide": 12}

    return job_titles.get(job_title)

def _format_date(date_string):
    format_string = "%Y-%m-%d %H:%M:%S"

    return datetime.strptime(date_string, format_string)