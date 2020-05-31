from __future__ import print_function

import basc_py4chan
import html2text
h = html2text.HTML2Text()

class Board:

    def __init__(self,Name):
        self.Name = Name
        self.Comments = []

    def board_status(self):
        brd = basc_py4chan.Board(self.Name)
        thread_ids = brd.get_all_thread_ids()
        str_thread_ids = [str(id) for id in thread_ids]
        board_length = len(str_thread_ids)
        return board_length,thread_ids,brd

    def comment_clean_up(self,comment):
        return (h.handle(comment)).replace('\n', ' ')

    def comment_gather(self,board_length,thread_ids,brd):
        for x in range(board_length-1):
            current_thread = thread_ids[x]
            thread = brd.get_thread(current_thread)
            try:
                for c in thread.replies:
                    comment = self.comment_clean_up(c.comment)
                    self.Comments.append((comment.encode('ascii','ignore')).decode("utf-8") )
            except:
                continue
        return ' '.join(self.Comments).lower()
