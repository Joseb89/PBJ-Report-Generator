from src.timestamps import Database

_db = Database(f"mysql+pymysql://test:test@localhost:{3307}/pbj-test")

def test_insert_timestamps():
       _db.create_tables()

       _db.insert_timestamps("tests\\PBJ-Report-Test.csv")

       timestamp = _db.select_all_timestamps().first()

       assert timestamp.employee_id == "Elendil"
       assert timestamp.job_code == 9