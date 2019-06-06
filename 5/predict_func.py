from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups

categories = ['talk.religion.misc','soc.religion.christian','sci.space','comp.graphics']

def predict_category(s, train=fetch_20newsgroups(subset= 'train',categories= categories), model= make_pipeline(TfidfVectorizer(),MultinomialNB())):
    """prediction of category of string with text
    :Args:
        s (str): strig with targeted text
        train (fetch_20newsgroups): tain with categories
        categories (tuple of stings): default is ['talk.religion.misc','soc.religion.christian','sci.space','comp.graphics']
    :Returns:
        text category"""
    pred = model.predict([s])
    return train.target_names[pred[0]]