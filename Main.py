

#import WordFreq
#import Reddit_
import FourChan

import Addingdata



if __name__ == "__main__":

    bad_practice_variable = '4chan'
    if bad_practice_variable == '4chan':
        Board = FourChan.Board('pol')

        x,y = Board.thread_data()

        Addingdata.initiate()
        Addingdata.insert_data(x,y)
        Addingdata.close_connection()
