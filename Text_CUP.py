import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
chachedWords = stopwords.words('english')



class Text_CUP:

    def __init__(self,comments):
        self.comments = comments

    def tokenizer_(self):
        word_list = nltk.word_tokenize(self.comments)
        return word_list

    def lemmatizer(self,word_list):
        lemmatizer = WordNetLemmatizer()
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list if w.isalpha() and w not in chachedWords])
        return lemmatized_output
