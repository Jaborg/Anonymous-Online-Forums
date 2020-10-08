import os
import time
import datetime

import mysql.connector

user = os.environ.get("MYSQL_USER", None)
password = os.environ.get("MYSQL_PASSWORD", None)
# host = "localhost"
# database = "forums_test"


cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='forums_test')
cursor = cnx.cursor()


tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)
print('lol')
#
# add_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
#
# delete_employee = ("DELETE FROM employee WHERE first_name = %s AND last_name = %s")
#
# data_employee = [('Geert', 'Vanderkelen', tomorrow, 'M', datetime.date(1977, 6, 14)),
# ('Jacob', 'Lappin', tomorrow, 'M', datetime.date(1978, 2, 8))]
#
# # Insert new employee
# def insert_employees(employee_info):
#     for employee in employee_info:
#         cursor.execute(add_employee, employee)
#         emp_no = cursor.lastrowid
#         data_salary = {
#           'emp_no': emp_no,
#           'salary': 50000,
#           'from_date': tomorrow,
#           'to_date': datetime.date(9999, 1, 1),
#         }
#         cursor.execute(add_salary, data_salary)
#     return
#
# def delete_table_info(table):
#     cursor.execute("TRUNCATE TABLE {}".format(table))
#     return
#
# insert_employees(data_employee)

#cursor.execute(add_employee, data_employee)

# Insert salary information

#cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
