"""
Reads the .csv file to create 
the list of dictionaries that will be used
to insert the employee workdays in the database.
"""

import csv

def create_timestamps(file="./PBJ-Report.csv"):
    """
    Reads the .csv file and stores the data in a dictionary list.

    Returns:
        list[dict]: List of timestamp dictionaries
        containing employee id, work date, total hours,
        job code, and pay code. 

        Raises:
            FileNotFoundError: if the .csv file cannot be located or loaded.
            ValueError: if hours, job code, or pay code have invalid input.     
    """
    
    dict_list = []

    try:
        with open(file, "r") as csv_file:
            data = csv.DictReader(csv_file)

            for line in data:
                id = line.get("employeeId")
                clock_in_date = line.get("date")
                total_hours = float(line.get("hours"))
                job_title_code = int(line.get("jobTitleCode"))
                pay_type_code = int(line.get("payTypeCode"))

                if(job_title_code <= 0 or job_title_code > 40):
                    raise ValueError("Job Code must be between 1 and 40.")
                
                if(pay_type_code <= 0 or pay_type_code > 3):
                    raise ValueError("Pay Code must be between 1 and 3.")

                dict_data = {"employee_id": id, "clock_in_date": clock_in_date,
                            "total_hours": total_hours, 
                            "job_code": job_title_code, "pay_code": pay_type_code}

                dict_list.append(dict_data)
    except FileNotFoundError:
        print("CSV file is not found.")             

    return dict_list