import os
import time
import datetime

import FourChan


import mysql.connector

user = os.environ.get("MYSQL_USER", None)
password = os.environ.get("MYSQL_PASSWORD", None)
# host = "localhost"
# database = "forums_test"



Board = FourChan.Board('pol')

x,y = Board.thread_data()

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='forums_test',auth_plugin='caching_sha2_password')
cursor = cnx.cursor()



#
add_thread = ("INSERT INTO thread   "
                "(board_name, thread_number, thread_comment, subject, No_of_replies,Date)"
                "VALUES (%s, %s, %s, %s, %s,%s) "
                "ON DUPLICATE KEY UPDATE No_of_replies = VALUES(No_of_replies) ")

add_comment = ("INSERT INTO comments   "
                "(post_id, poster_id, is_op, thread_number, comment,date,file_url,thumbnail)"
                "VALUES (%s, %s, %s, %s, %s,%s,%s,%s) ")


def insert_thread(thread_list):
     for thread in thread_list:
        cursor.execute(add_thread, thread)

     return


def insert_comments(comment_list):
    for comment in comment_list:
        cursor.execute(add_comment,comment)

    return


def insert_data(thread_list,comment_list):
    insert_thread(thread_list)
    insert_comments(comment_list)
    print(f'Succesful insertion of latest 4chan ; {Board}')
    return

insert_data(x,y)
cnx.commit()
#
cursor.close()
cnx.close()
