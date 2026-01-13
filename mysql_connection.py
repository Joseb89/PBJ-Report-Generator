import mysql.connector
import credentials
import excel_reader

from mysql.connector import Error

def insert_employees():
    insert_command = """
        INSERT INTO employees (employee_id, first_name, last_name, job_code, pay_code) 
        VALUES (%(employee_id)s, %(first_name)s, %(last_name)s, %(job_code)s, %(pay_code)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=excel_reader.create_employees())

def insert_work_days():
    insert_command = """
        INSERT INTO work_days (employee_id, clock_in_date, clock_in_time, clock_out_date, clock_out_time) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(clock_in_time)s, %(clock_out_date)s, %(clock_out_time)s)
    """

    _insert_into_table(query=insert_command, dictionary_list=excel_reader.create_employee_timestamps())            

def get_employee_ids():
        try:
            with mysql.connector.connect(host="localhost", 
                                        user=credentials.user, 
                                        password=credentials.password, 
                                        database=credentials.database) as connection:

                with connection.cursor() as cursor:
                     select_query = "SELECT employee_id FROM employees"

                     cursor.execute(select_query)

                     user_ids = cursor.fetchall()

                     return [id[0] for id in user_ids]    
        except Error as error:
             print(error)

def get_employee_work_days(user_id):
    try:
        with mysql.connector.connect(host="localhost", 
                                    user=credentials.user, 
                                    password=credentials.password, 
                                    database=credentials.database) as connection:

            with connection.cursor() as cursor:
                select_query = "SELECT * FROM work_days WHERE employee_id = %s"

                cursor.execute(select_query, (user_id,))

                return cursor.fetchall()
    except Error as error:
        print(error)              

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