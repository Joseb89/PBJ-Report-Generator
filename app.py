from flask import Flask, render_template

import mysql_connection

app = Flask(__name__)

@app.route('/api/get_work_days')
def get_work_days():
    work_days = mysql_connection.get_work_days()
    return render_template("index.html", work_days=work_days)

if __name__ == '__main__':
    app.run()