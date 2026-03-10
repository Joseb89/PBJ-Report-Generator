from flask import Flask, render_template

import mysql_connection

app = Flask(__name__)

@app.route('/')
def report_generator():
    return render_template("index.html")

@app.route('/api/get_work_days', methods=['GET'])
def get_work_days():
    work_days = mysql_connection.get_all_work_days()
    return render_template("timestamps.html", work_days=work_days)

@app.route('/api/get_employee_timestamps/<employee_id>', methods=['GET'])
def get_employee_work_days(employee_id):
    timestamps = mysql_connection.get_employee_work_days(employee_id)
    return render_template("employee-timestamps.html", employee_id=employee_id, timestamps=timestamps)

if __name__ == '__main__':
    app.run()