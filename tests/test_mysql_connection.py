import datetime

def test_insert_work_days(test_connection):
    count = test_connection[1].rowcount
    
    assert count == 3

def test_get_all_work_days(test_connection):
    test_cursor = test_connection[1]

    query = "SELECT * FROM employee_work_days"

    test_cursor.execute(query)

    test_data = test_cursor.fetchall()

    assert test_data[0][1] == "Taverin"
    assert test_data[1][3] == 8.00
    assert test_data[2][4] == 10

def test_get_employee_work_days(test_connection):
    test_cursor = test_connection[1]

    query = "SELECT * FROM employee_work_days WHERE employee_id = 'Elendil'"

    test_cursor.execute(query)

    test_data = test_cursor.fetchone()

    assert test_data[1] == "Elendil"
    assert test_data[2] == datetime.date(2026, 4, 30)
    assert test_data[3] == 7.95