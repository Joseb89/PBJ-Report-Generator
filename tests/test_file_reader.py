import pytest
from src.file_reader import create_timestamps

def test_create_timestamps():
    test_data = create_timestamps("tests\\PBJ-Report-Test.csv")

    assert test_data

    assert test_data[0].get("employee_id") == "Taverin"

    assert test_data[1].get("job_code") == 10

def test_create_timestamps_exception():   
    with pytest.raises(ValueError, match="Job Code must be between 1 and 40."):
        create_timestamps("tests\\PBJ-Report-Except.csv")