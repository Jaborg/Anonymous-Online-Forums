import os
import time
import datetime

import FourChan


import mysql.connector

user = os.environ.get("MYSQL_USER", None)
password = os.environ.get("MYSQL_PASSWORD", None)
# host = "localhost"
# database = "forums_test"

print(user)
print(password)

Board = FourChan.Board('pol')

x,y = Board.thread_data()

cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='forums_test',auth_plugin='caching_sha2_password')
cursor = cnx.cursor()


tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)

#
add_thread = ("INSERT INTO thread "
                "(board_name, thread_number, thread_comment, subject, No_of_replies,Date)"
                "VALUES (%s, %s, %s, %s, %s,%s)")




#
# delete_employee = ("DELETE FROM employee WHERE first_name = %s AND last_name = %s")
#
threads = ('pol', 2230303, 'Really this', 'hello', 21 ,datetime.date(1977, 6, 14))




def insert_thread(thread_list):
     for thread in thread_list:
        print(thread)
        cursor.execute(add_thread, thread)


     return

insert_thread(x)

#cursor.execute(add_thread, thread)


# ('Jacob', 'Lappin', tomorrow, 'M', datetime.date(1978, 2, 8))]
#
# # Insert new employee
# def insert_employees(employee_info):
#     for employee in employee_info:
#         cursor.execute(add_employee, employee)
#
#
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
