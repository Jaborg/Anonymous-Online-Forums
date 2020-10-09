from __future__ import print_function
import sys

import basc_py4chan
import html2text
h = html2text.HTML2Text()

class Board:

    def __init__(self,Name):
        self.name = Name
        self.thread_list = []
        self.joined_Comments = []
        self.stored_Comments = []
        self.brd = basc_py4chan.Board(self.name)
        self.thread_ids = self.brd.get_all_thread_ids()
        self.board_length = len(self.thread_ids)


    def comment_clean_up(self,comment):
        return (h.handle(comment).replace('\n', ' ').encode('ascii','ignore').decode("utf-8"))

    def thread_data(self):
        for x in range(self.board_length - 1):
            current_thread = self.thread_ids[x]
            thread = self.brd.get_thread(current_thread)
            sticky = thread.sticky
            if sticky == True:
                continue
            else:
                topic = thread.topic
                self.thread_list.append([self.brd,topic.post_number,self.comment_clean_up(topic.comment),topic.subject,str(len(thread.replies)),topic.datetime])


        return self.thread_list

    def comment_data(self):
            comment_list = []
            for x in range(self.board_length - 1):
                current_thread = self.thread_ids[x]
                thread = self.brd.get_thread(current_thread)
                sticky = thread.sticky
                if sticky == True:
                    continue
                else:
                    topic = thread.topic
                    print(basc_py4chan.Post(thread))
                    try:
                        for c in thread.replies:
                            #print((c.datetime,c.comment))
                            comment = self.comment_clean_up(c.comment)
                            d_comments = [self.comment_clean_up(),topic.post_number]
                            print(d_comments)
                            self.Joined_Comments.append((comment))
                    except:
                        print(sys.exc_info())
                        continue
            return ' '.join(self.Joined_Comments).lower()


    #
    # def comment_data_store(self,board_length,thread_ids,brd):
