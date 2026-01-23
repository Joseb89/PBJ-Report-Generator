CREATE TABLE IF NOT EXISTS knopp_employees(
    employee_id VARCHAR(12) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    job_code TINYINT,
    pay_code TINYINT
);

CREATE TABLE IF NOT EXISTS agency_employees(
    employee_id VARCHAR(12) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    job_code TINYINT,
    pay_code TINYINT
);

CREATE TABLE IF NOT EXISTS knopp_work_days (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id VARCHAR(12) NOT NULL,
    clock_in_date DATE NOT NULL,
    total_hours FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS agency_work_days (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id VARCHAR(12) NOT NULL,
    clock_in_date DATE NOT NULL,
    clock_in_time TIME NOT NULL,
    clock_out_date DATE NOT NULL,
    clock_out_time TIME NOT NULL,
    total_hours FLOAT NOT NULL
)