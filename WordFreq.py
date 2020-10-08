from collections import Counter
import numpy as np
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def freq_dist(data):

        ngram_vectorizer = CountVectorizer(analyzer='word', tokenizer=word_tokenize, ngram_range=(1, 1), min_df=1)
        X = ngram_vectorizer.fit_transform(data.split('\n'))
        vocab = list(ngram_vectorizer.get_feature_names())
        counts = X.sum(axis=0).A1
        Freq = Counter(dict(zip(vocab, counts)))
        df = pd.DataFrame.from_dict(Freq, orient='index').reset_index()
        df.rename(columns={0:'Count','index':'Word'},inplace=True)
        return df
