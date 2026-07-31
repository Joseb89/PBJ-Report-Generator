from flask import Flask, render_template
from timestamps import Database

import xml.etree.ElementTree as ET

import xml_file_creator as xml_file_creator

app = Flask(__name__)

_db = Database()

@app.route('/')
def report_generator() -> str:
    """
    The home page where the report is generated.
    """

    xml_file_creator.create_databases()

    data = ET.Element('nursingHomeData')

    xml_file_creator.create_header(data)
    xml_file_creator.create_body(data)

    tree = ET.ElementTree(data)

    ET.indent(tree, '  ')

    file_name = "report.xml"

    tree.write(file_name, encoding="ASCII", xml_declaration=True)

    return "Report successfuly generated."

@app.route('/api/get_employee_timestamps', methods=['GET'])
def get_work_days():
    """
    Retrieves all of the timestamps from the database.
    """
    work_days = _db.select_all_timestamps()
    return render_template("timestamps.html", work_days=work_days)

@app.route('/api/get_employee_timestamps/<employee_id>', methods=['GET'])
def get_employee_work_days(employee_id):
    """
    Retrieves the timestamps for a specific employee based on their employee id.

    Parameters:
        employee_id (str): The employee's id as recognized by CMS
    """
    timestamps = _db.select_timestamps_by_employee_id(employee_id)
    return render_template("employee-timestamps.html", employee_id=employee_id, timestamps=timestamps)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)