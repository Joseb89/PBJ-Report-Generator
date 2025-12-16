CREATE TABLE IF NOT EXISTS employees(
    employee_id VARCHAR(12) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    job_code BIT(2)
    pay_code BIT(2)
):

CREATE TABLE IF NOT EXISTS work_days (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    clock_in_date DATE NOT NULL,
    clock_in_time TIME NOT NULL,
    clock_out_date DATE NOT NULL,
    clock_out_time TIME NOT NULL
)