import mysql.connector
import credentials
import excel

from mysql.connector import Error

def insert_employees():
    try:
        with mysql.connector.connect(host="localhost", 
                                     user=credentials.user, 
                                     password=credentials.password, 
                                     database=credentials.database) as connection:

            with connection.cursor() as cursor:
                
                insert_command = """
                    INSERT INTO employees (employee_id, first_name, last_name, job_code, pay_code) 
                    VALUES (%(employee_id)s, %(first_name)s, %(last_name)s, %(job_code)s, %(pay_code)s)
                """

                employees = excel.create_employee_dictionary()
                
                cursor.executemany(insert_command, employees)

                connection.commit()
    except Error as error:
        print(error)

def insert_work_days():
    try:
        with mysql.connector.connect(host="localhost", 
                                     user=credentials.user, 
                                     password=credentials.password, 
                                     database=credentials.database) as connection:

            with connection.cursor() as cursor:

                insert_command = """
                    INSERT INTO work_days (employee_id, clock_in_date, clock_in_time, clock_out_date, clock_out_time) 
                    VALUES (%(employee_id)s, %(clock_in_date)s, %(clock_in_time)s, %(clock_out_date)s, %(clock_out_time)s)
                """

                work_days = excel.create_employee_timestamps()

                cursor.executemany(insert_command, work_days)

                connection.commit()

    except Error as error:
        print(error)            

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

                     id_list = []

                     for id in user_ids:
                          id_list.append(id[0])

                     return id_list        
        except Error as error:
             print(error)             