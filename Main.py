

#import WordFreq
#import Reddit_
import FourChan

import Addingdata



if __name__ == "__main__":

    bad_practice_variable = '4chan'
    if bad_practice_variable == '4chan':
        Board = FourChan.Board('pol')

        thread_list,comment_list = Board.thread_data()



        SQL_connection = Addingdata.SQL_connection()


        SQL_connection.insert_data(thread_list,comment_list)
        SQL_connection.close_connection()
