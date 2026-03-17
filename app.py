from flask import Flask, render_template, request
from zipfile import ZipFile

import xml.etree.ElementTree as ET

import xml_file_creator
import mysql_connection

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def report_generator():
    """
    The home page where the report can be generated.
    """
    data = ET.Element('nursingHomeData')

    xml_file_creator.create_header(data)
    xml_file_creator.create_body(data)

    tree = ET.ElementTree(data)

    ET.indent(tree, '  ')

    file_name = "report.xml"

    tree.write(file_name, encoding="ASCII", xml_declaration=True)

    with ZipFile("PBJ_Report_Generator.zip", "w") as zip_file:
        zip_file.write(file_name)

    return render_template("index.html")

@app.route('/api/insert_timestamp', methods=['GET', 'POST'])
def insert_timestamp():
    """
    Inserts new timestamp into the database

    Raises:
        ValueError: if invalid data type is retrieved from the form
    """
    if request.method == "POST":

        try:
            employee_id = request.form['employee_ids']
            clock_in_date = request.form['workday']
            work_hours = float(request.form['hours'])

            mysql_connection.insert_work_days_from_form(employee_id, clock_in_date, work_hours)
        except ValueError as error:
            return str(error)    

    return render_template("insert-timestamp.html")

@app.route('/api/get_employee_timestamps', methods=['GET'])
def get_work_days():
    """
    Retrieves all of the timestamps from the database.
    """
    work_days = mysql_connection.get_all_work_days()
    return render_template("timestamps.html", work_days=work_days)

@app.route('/api/get_employee_timestamps/<employee_id>', methods=['GET'])
def get_employee_work_days(employee_id):
    """
    Retrieves the timestamps for a specific employee based on their employee id.

    Parameters:
        employee_id (str): The employee's id as recognized by CMS
    """
    timestamps = mysql_connection.get_employee_work_days(employee_id)
    return render_template("employee-timestamps.html", employee_id=employee_id, timestamps=timestamps)

if __name__ == '__main__':
    app.run()