# import des librairies
import nltk
import numpy as np
import random
import string # to process standard python strings
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words


def tokens():
# import du texte & nettoyages
    f=open('./static/infos_corona.txt','r',errors = 'ignore', encoding = "utf8")
    raw=f.read()
    raw=raw.lower()# converts to lowercase
    # quelques modifications : 
    raw = re.sub(r"n.c.a.", "", raw)
    raw = re.sub(r"covid.*", "coronavirus", raw)
    raw = re.sub(r"\n", " ", raw)
    # Création d'une liste de phrases (= tokenization)
    sent_tokens = nltk.sent_tokenize(raw)
    i = 1
    for n in range(len(sent_tokens)):
        a = len(sent_tokens)- i
        if (re.search("\?", sent_tokens[a])):
            del sent_tokens[a]
        i += 1
    return sent_tokens

def matrix_tfidf(sent_tokens):
# Entraînement d'une matrice TF-IDF
    french_stop_words = get_stop_words('french')
    TfidfVec = TfidfVectorizer(stop_words = french_stop_words)
    tfidf = TfidfVec.fit(sent_tokens)
    # on crée la matrice TF-IDF sur le texte de la page wiki
    phrases_tf = tfidf.transform(sent_tokens)
    return phrases_tf, tfidf