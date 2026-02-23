"""
Manages the connection to the MySQL database for inserting
and retrieving data.
"""

import mysql.connector
import credentials
import file_reader

from mysql.connector import Error

def insert_employees():
    """
    Inserts the following employee data into the employees database.

        employee_id (str): The employee's id as recognized by CMS
        first_name (str): The employee's first name if available
        last_name (str): The employee's last name if available
        job_code (int): The job code that specifies the employee's job title
        pay_code (int): Specifies whether the employee's pay was exempt,
            non-exempt, or contract
    """

    insert_command = """
        INSERT INTO employees (employee_id, first_name, last_name, job_code, pay_code) 
        VALUES (%(employee_id)s, %(first_name)s, %(last_name)s, %(job_code)s, %(pay_code)s)
    """

    dictionary = file_reader.create_knopp_employees() + file_reader.create_agency_employees()

    _insert_into_table(query=insert_command, dictionary_list=dictionary)    

def insert_work_days():
    """
    Inserts the following workday data into the employee_work_days database

        employee_id (str): The employee's id as recognized by CMS
        clock_in_date (datetime): The date the employee clocked in
            to work
        total_hours (float): The total number of hours the employee
            worked    
    """

    insert_command = """
        INSERT INTO employee_work_days (employee_id, clock_in_date, total_hours) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(total_hours)s)
    """

    dictionary = file_reader.create_admin_timestamps() + file_reader.create_agency_timestamps()

    _insert_into_table(query=insert_command, dictionary_list=dictionary)

def get_work_days():
    """
    Retreives all of the employee timestamps from the employee_work_days database.

    Returns:
        list[tuple]: The employee timestamps associated with the employee id

    Raises:
        Error: if error occurs when connecting to or performing operations on the database.    
    """

    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:

            with connection.cursor() as cursor:

                select_query = """
                SELECT employee_work_days.employee_id, employee_work_days.clock_in_date, 
                employee_work_days.total_hours, employees.job_code, employees.pay_code
                FROM employee_work_days
                RIGHT JOIN employees ON employee_work_days.employee_id = employees.employee_id
                ORDER BY employee_work_days.employee_id, employee_work_days.clock_in_date
                """

                cursor.execute(select_query)

                return cursor.fetchall()
            
    except Error as error:
        print(error)            

def _insert_into_table(query, dictionary_list):
    """
    Inserts data contained in a list of dictionaries into a database.

    Parameters:
        query (str): the INSERT query to send to the database.
        dictionary_list (list[dict]): The list of dictionaries.
    
    Raises:
        Error: if error occurs when connecting to or performing operations on the database.
    """
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:

            with connection.cursor() as cursor:
                    
                cursor.executemany(query, dictionary_list)

                connection.commit()
    except Error as error:
        print(error) 