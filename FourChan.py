from __future__ import print_function
import sys

import basc_py4chan
import html2text
h = html2text.HTML2Text()

class Board:

    def __init__(self,Name):
        self.name = Name
        self.thread_list = []
        self.post_list = []
        self.brd = basc_py4chan.Board(self.name)
        self.thread_ids = self.brd.get_all_thread_ids()
        self.board_length = len(self.thread_ids)


    def comment_clean_up(self,comment):
        return (h.handle(comment).replace('\n', ' ').encode('ascii','ignore').decode("utf-8"))

    def thread_data(self):
        for x in range(3):
            current_thread = self.thread_ids[x]
            thread = self.brd.get_thread(current_thread)
            sticky = thread.sticky
            if sticky == True:
                continue
            else:
                topic = thread.topic
                self.thread_list.append([self.brd,topic.post_number,self.comment_clean_up(topic.comment),
                                            topic.subject,str(len(thread.replies)),topic.datetime])
                try:
                    for c in thread.all_posts:
                        comment = self.comment_clean_up(c.comment)
                        self.post_list.append([c.post_id,c.poster_id,c.is_op,topic.post_number,self.comment_clean_up(c.text_comment)
                                                ,c.datetime,c.file_url,c.thumbnail_fname])
                except:
                    print(sys.exc_info())
                    continue


        return self.thread_list,self.post_list
