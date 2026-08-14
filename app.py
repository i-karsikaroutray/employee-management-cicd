from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

employees = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["employee_name"]
        email = request.form["email"]

        sql = "INSERT INTO employees (name, email) VALUES (%s, %s)"
        values = (name, email)

        cursor.execute(sql, values)
        db.commit()

        return redirect("/view-employees")

    return render_template("add_employee.html")

@app.route("/view-employees")
def view_employees():

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    return render_template(
        "view_employees.html",
        employees=employees
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

