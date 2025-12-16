import json
import mysql.connector

from mysql.connector import Error

def create_database():

    try:
        with open("employee.json", "r") as file:
            employees = json.load(file) 
    except FileNotFoundError:
        print("File Not Found.")       

    try:
        with mysql.connector.connect(host="localhost", user="jose", password="Kn0pp!", database="khrc") as connection:

            with connection.cursor() as cursor:
                table_name = "employees"

                cursor.execute("CREATE DATABASE khrc")
                cursor.execute(f"{"CREATE TABLE "}{table_name}")

                insert_command = f"{"INSERT INTO "}{table_name}{" (id, first_name, last_name, job_title_code) "}{"VALUES (%s, %s, %s, %s)"}"

                for employee in employees:
                    cursor.execute(insert_command, tuple(employee.values()))

                connection.commit()
    except Error as error:
        print(error)            
