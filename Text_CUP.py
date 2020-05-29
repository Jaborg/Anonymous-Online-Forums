import nltk
from nltk.stem import WordNetLemmatizer



class Text_CUP:

    def __init__(self,comments):
        self.comments = comments

    def tokenizer_(self):
        word_list = nltk.word_tokenize(self.comments)
        return word_list

    def lemmatizer(self,word_list):
        lemmatizer = WordNetLemmatizer()
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        return lemmatized_output


wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension

wordfreq = str(list(zip(wordlist, wordfreq)))
print(wordfreq)
