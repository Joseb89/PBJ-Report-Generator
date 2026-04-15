"""
Manages the connection to the MySQL database for inserting
and retrieving data.
"""

import mysql.connector
import credentials
import file_reader

from mysql.connector import Error


def insert_work_days_from_form(employee_id, clock_in_date, work_hours):
    """
    Inserts workday data from the HTML form into the employee_work_days database

    Parameters:
        employee_id (str): The employee's id as recognized by CMS
        clock_in_date (datetime): The date the employee clocked in
            to work
        total_hours (float): The total number of hours the employee
            worked

    Raises:
        Error: if error occurs when connecting to or performing operations on the database.            
    """
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:
            
            with connection.cursor() as cursor:
                
                insert_command = """
                    INSERT INTO employee_work_days (employee_id, clock_in_date, total_hours) 
                    VALUES (%s, %s, %s)
                """

                values = (employee_id, clock_in_date, work_hours)

                cursor.execute(insert_command, values)

                connection.commit()

    except Error as error:
        print(error)        


def insert_work_days_from_csv():
    """
    Inserts the following workday data from the .csv file into the employee_work_days database

        employee_id (str): The employee's id as recognized by CMS
        clock_in_date (datetime): The date the employee clocked in
            to work
        total_hours (float): The total number of hours the employee
            worked    
    """

    insert_command = """
        INSERT INTO employee_work_days (employee_id, clock_in_date, total_hours, job_code, pay_code) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(total_hours)s, %(job_code)s, %(pay_code)s)
    """

    dictionary = file_reader.create_timestamps()

    _insert_into_table(query=insert_command, dictionary_list=dictionary)

def get_all_work_days():
    """
    Retreives all of the employee timestamps from the employee_work_days database.

    Returns:
        list[tuple]: The employee timestamps

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
                    SELECT employee_id, clock_in_date, total_hours, job_code, pay_code
                    FROM employee_work_days
                    ORDER BY employee_id, clock_in_date
                """

                cursor.execute(select_query)

                return cursor.fetchall()

    except Error as error:
        print(error)

def get_employee_work_days(id):
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:
            
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM employee_work_days WHERE employee_id = %s"

                cursor.execute(select_query, (id,))

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