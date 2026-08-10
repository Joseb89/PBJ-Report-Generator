import pytest

from src.file_reader import create_timestamps
from src.timestamps import Timestamp

@pytest.fixture(scope="session")
def test_csv_data():
    return create_timestamps("tests\\PBJ-Report-Test.csv")

@pytest.fixture(scope="session")
def test_timestamps(test_csv_data):
    timestamps = test_csv_data

    new_timestamps = []

    for timestamp in timestamps:
        employee_id = timestamp.get("employee_id")
        clock_in_date = timestamp.get("clock_in_date")
        total_hours = timestamp.get("total_hours")
        job_code = timestamp.get("job_code")
        pay_code = timestamp.get("pay_code")

        new_timestamps.append(Timestamp(employee_id=employee_id, clock_in_date=clock_in_date, 
                                              total_hours=total_hours, job_code=job_code, 
                                              pay_code=pay_code))

    return new_timestamps