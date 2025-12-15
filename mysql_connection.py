import json
import mysql.connector


def create_database():

    employees = json.loads("employee.json")

    with mysql.connector.connect(host="localhost", user="jose", password="Kn0pp!") as connection:

        with connection.cursor() as cursor:
            table_name = "employees"

            cursor.execute("CREATE DATABASE khrc")
            cursor.execute(f"{"CREATE TABLE "}{table_name}")

            insert_command = f"{"INSERT INTO "}{table_name}{" (id, first_name, last_name, job_title_code) "}{"VALUES (%s, %s, %s, %s)"}"

            for employee in employees:
                cursor.execute(insert_command, tuple(employee.values()))

            connection.commit()
