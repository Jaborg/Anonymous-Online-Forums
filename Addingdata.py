import os
import time
import datetime



import mysql.connector
user = os.environ.get("MYSQL_USER", None)
password = os.environ.get("MYSQL_PASSWORD", None)
# host = "localhost"
# database = "forums_test"


class SQL_connection:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Baghdad1258',
                                      host='127.0.0.1',
                                      database='forums_test',auth_plugin='caching_sha2_password')
        self.cursor = self.cnx.cursor()



        #
        self.add_thread = ("INSERT INTO thread   "
                        "(board_name, thread_number, thread_comment, subject, No_of_replies,Date,Timestamp)"
                        "VALUES (%s, %s, %s, %s, %s,%s,%s) "
                        "ON DUPLICATE KEY UPDATE No_of_replies = VALUES(No_of_replies) ")

        self.add_comment = ("INSERT INTO comments   "
                        "(post_id, poster_id, is_op, thread_number, comment,date,file_url,thumbnail,Timestamp)"
                        "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s) ")

        return





    def insert_data(self,thread_list,comment_list):

        for thread in thread_list:
            self.cursor.execute(self.add_thread, thread)
        for comment in comment_list:
            self.cursor.execute(self.add_comment,comment)

        print(f'Succesful insertion of latest version of {thread[0]}')

        return


    def close_connection(self):
        self.cnx.commit()
        #
        self.cursor.close()
        self.cnx.close()
