
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import nltk
chachedWords = stopwords.words('english')

import html2text
h = html2text.HTML2Text()

import pandas as pd
import matplotlib.pyplot as plt

import FourChan
import Text_CUP
import WordFreq



if __name__ == "__main__":
    Board = FourChan.Board('pol')
    length,ids,brd = Board.board_status()
    comments = Board.comment_gather(length,ids,brd)

    Clean = Text_CUP.Text_CUP(comments)
    lemmatized = Clean.lemmatizer(Clean.tokenizer_())


    plt.figure(figsize=(20,5))
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords = stopwords,max_font_size=75,background_color="white").generate(lemmatized)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
