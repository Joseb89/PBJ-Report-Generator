CREATE TABLE IF NOT EXISTS employees(
    employee_id VARCHAR(30) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    job_code TINYINT NOT NULL,
    pay_code TINYINT NOT NULL
);

CREATE TABLE IF NOT EXISTS employee_work_days (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id VARCHAR(30) NOT NULL,
    clock_in_date DATE NOT NULL,
    total_hours FLOAT(2) DEFAULT 0.00
)