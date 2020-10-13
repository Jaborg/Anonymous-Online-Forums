

from nltk.corpus import stopwords
import nltk
chachedWords = stopwords.words('english')




import matplotlib.pyplot as plt
import FourChan
import Text_CUP
import WordFreq
import Reddit_



if __name__ == "__main__":

    bad_practice_variable = '4chan'
    if bad_practice_variable == '4chan':
        Board = FourChan.Board('pol')

        x,y = Board.thread_data()




        # Clean = Text_CUP.Text_CUP(comments)
        # lemmatized = Clean.lemmatizer(Clean.tokenizer_())
        #
        #
        # plt.figure(figsize=(20,5))
        # stopwords = set(STOPWORDS)
        # wordcloud = WordCloud(stopwords = stopwords,max_font_size=75,background_color="white").generate(lemmatized)
        # plt.imshow(wordcloud, interpolation='bilinear')
        # plt.axis("off")
        # plt.show()
        # print(lemmatized)
    #
    # else:
    #     ids = Reddit_.find_threads()
    #     comments = Reddit_.gather_comments(ids)
    #
    #     plt.figure(figsize=(20,5))
    #     stopwords = set(STOPWORDS)
    #     wordcloud = WordCloud(stopwords = stopwords,max_font_size=75,background_color="white").generate(comments)
    #     plt.imshow(wordcloud, interpolation='bilinear')
    #     plt.axis("off")
    #     plt.show()
