import mysql.connector
import credentials
import file_reader

from mysql.connector import Error

def insert_knopp_employees():
    insert_command = """
        INSERT INTO knopp_employees (employee_id, first_name, last_name, job_code, pay_code) 
        VALUES (%(employee_id)s, %(first_name)s, %(last_name)s, %(job_code)s, %(pay_code)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=file_reader.create_knopp_employees())

def insert_agency_employees():
    insert_command = """
        INSERT INTO agency_employees (employee_id, first_name, last_name, job_code, pay_code) 
        VALUES (%(employee_id)s, %(first_name)s, %(last_name)s, %(job_code)s, %(pay_code)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=file_reader.create_agency_employees())

def insert_admin_work_days():
    insert_command = """
        INSERT INTO knopp_work_days (employee_id, clock_in_date, total_hours) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(total_hours)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=file_reader.create_admin_timestamps())      

def insert_agency_work_days():
    insert_command = """
        INSERT INTO agency_work_days (employee_id, clock_in_date, clock_in_time, clock_out_date, clock_out_time, total_hours) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(clock_in_time)s, %(clock_out_date)s, %(clock_out_time)s, %(total_hours)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=file_reader.create_agency_timestamps())

def get_knopp_employees():
    knopp_select_query = "SELECT employee_id, job_code, pay_code FROM knopp_employees"

    return _get_employee_info(knopp_select_query)   


def get_agency_employees():
    agency_select_query = "SELECT employee_id, job_code, pay_code FROM agency_employees"

    return _get_employee_info(agency_select_query)

def get_knopp_work_days(user_id):
    select_query = "SELECT * FROM knopp_work_days WHERE employee_id = %s"

    return _get_employee_work_days(select_query, user_id)  

def get_agency_work_days(user_id):
    select_query = "SELECT * FROM agency_work_days WHERE employee_id = %s"

    return _get_employee_work_days(select_query, user_id)             

def _insert_into_table(query, dictionary_list):
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

def _get_employee_info(query):
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:

            with connection.cursor() as cursor:

                cursor.execute(query)

                return cursor.fetchall()
    except Error as error:
        print(error)        

def _get_employee_work_days(query, user_id):
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:

            with connection.cursor() as cursor:

                cursor.execute(query, (user_id,))

                return cursor.fetchall()
    except Error as error:
        print(error)      