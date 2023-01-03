import nltk
import string
from unidecode import unidecode

stopwords = nltk.corpus.stopwords.words('portuguese')


def remove_stopwords(text):
    text = text_normalize(text)

    text = ' '.join([k for k in text.split(" ") if k not in stopwords])

    return text

def text_normalize(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = unidecode(text)

    return text