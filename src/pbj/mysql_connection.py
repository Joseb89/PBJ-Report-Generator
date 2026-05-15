"""
Manages the connection to the MySQL database for inserting
and retrieving data.
"""

import mysql.connector
import os
import pbj.file_reader as file_reader

from mysql.connector import Error

_name = os.getenv("MYSQL_HOST")
_user = os.getenv("MYSQL_USERNAME")
_password = os.getenv("MYSQL_PASSWORD")
_database = os.getenv("MYSQL_DATABASE")     


def insert_work_days():
    """
    Inserts the following workday data from the .csv file into the employee_work_days database

        employee_id (str): The employee's id as recognized by CMS
        clock_in_date (datetime): The date the employee clocked in
            to work
        total_hours (float): The total number of hours the employee
            worked
        job_code (int): The code that represents the employee's job title
        pay_code (int): Specifies whether the work wa       
    """

    insert_command = """
        INSERT INTO employee_work_days (employee_id, clock_in_date, total_hours, job_code, pay_code) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(total_hours)s, %(job_code)s, %(pay_code)s)
    """

    try:
        with mysql.connector.connect(host=_name, 
                                    user=_user, 
                                    password=_password, 
                                    database=_database) as connection:

            with connection.cursor() as cursor:
                    
                cursor.executemany(insert_command, file_reader.create_timestamps())

                connection.commit()
    except Error as error:
        print(error) 


def get_all_work_days():
    """
    Retreives all of the employee timestamps from the employee_work_days database.

    Returns:
        list[tuple]: The employee timestamps

    Raises:
        Error: if error occurs when connecting to or performing operations on the database.    
    """
    try:
        with mysql.connector.connect(host=_name, 
                                    user=_user, 
                                    password=_password, 
                                    database=_database) as connection:

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
        with mysql.connector.connect(host=_name, 
                                    user=_user, 
                                    password=_password, 
                                    database=_database) as connection:
            
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM employee_work_days WHERE employee_id = %s"

                cursor.execute(select_query, (id,))

                return cursor.fetchall()

    except Error as error:
        print(error)