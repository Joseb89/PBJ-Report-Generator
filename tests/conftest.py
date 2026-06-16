import pytest
import pymysql

from src.file_reader import create_timestamps
from testcontainers.mysql import MySqlContainer

@pytest.fixture(scope="session")
def test_database():
    with MySqlContainer("mysql:8.4.9") as mysql:
        yield mysql

@pytest.fixture(scope="session")
def test_connection(test_database):
    connection = pymysql.connect(host=test_database.get_container_host_ip(),
                                 port=int(test_database.get_exposed_port(3306)),
                                 user=test_database.username,
                                 password=test_database.password,
                                 database=test_database.dbname,
                                 autocommit=False)
    
    with connection.cursor() as cursor:
        query = """CREATE TABLE IF NOT EXISTS employee_work_days (
                id INT PRIMARY KEY AUTO_INCREMENT,
                employee_id VARCHAR(30) NOT NULL,
                clock_in_date DATE NOT NULL,
                total_hours FLOAT(2) DEFAULT 0.00,
                job_code TINYINT NOT NULL,
                pay_code TINYINT NOT NULL
            )"""
        
        cursor.execute(query)

        insert_command = """
        INSERT INTO employee_work_days (employee_id, clock_in_date, total_hours, job_code, pay_code) 
        VALUES (%(employee_id)s, %(clock_in_date)s, %(total_hours)s, %(job_code)s, %(pay_code)s)
    """
        test_data = create_timestamps("tests\\PBJ-Report-Test.csv")
        
        cursor.executemany(insert_command, test_data)

        connection.commit()
        
        yield connection, cursor

@pytest.fixture(scope="session")
def test_data(test_connection):
    test_cursor = test_connection[1]

    query = """
        SELECT employee_id, clock_in_date, total_hours, job_code, pay_code
        FROM employee_work_days
        ORDER BY employee_id, clock_in_date
        """

    test_cursor.execute(query)

    test_data = test_cursor.fetchall()

    yield test_data