import datetime

def test_insert_work_days(test_connection):
    count = test_connection[1].rowcount
    
    assert count == 3

def test_get_all_work_days(test_data):
    assert test_data[0][0] == "Taverin"
    assert test_data[1][2] == 5.7
    assert test_data[2][3] == 9

def test_get_employee_work_days(test_connection):
    test_cursor = test_connection[1]

    query = "SELECT * FROM employee_work_days WHERE employee_id = 'Elendil'"

    test_cursor.execute(query)

    test_data = test_cursor.fetchone()

    assert test_data[0] == "Elendil"
    assert test_data[1] == datetime.date(2026, 1, 2)
    assert test_data[2] == 1.88