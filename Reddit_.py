import pandas as pd
import sys
import praw
from praw.models import MoreComments




reddit = praw.Reddit(client_id = 'vDfkx-DyLlgD_A', #  The API link
                     client_secret = 'ejSVE3RhbhkSNxV6s0NukXphH5M',
                     username = 'nebuch_babl95',
                     password = 'Chelsea95',
                     user_agent = 'political_quoter')




def find_threads():
    ids = []
    for submission in reddit.subreddit('politics').hot(limit=5):
        if not submission.stickied:
            ids.append(submission.id)
    return ids


def gather_comments(ids):
    comment_list = []
    for id in ids:
        print(id)
        try:
            submission = reddit.submission(id=id)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                if comment.author != 'AutoModerator':
                    comment_list.append((comment.body).lower())
        except:
            print('Sorry ;)')
    return ' '.join(comment_list)
