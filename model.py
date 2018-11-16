# coding: utf-8
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils import shuffle

def contents2characters(contents):
    return list(map(lambda x: ' '.join(list(str(x))), contents))


def contentchar2bow(vec, content_characters):
    return vec.transform(content_characters)


def create_vectorizer(content_characters, outfile="vec.pkl"):
    vec = CountVectorizer(strip_accents=None, stop_words=None, analyzer="char").fit(content_characters)
    with open(outfile, "wb") as f:
        pickle.dump(vec, f)
    return vec


def train(train_file="content.csv", outfile="model.pkl"):
    df = shuffle(pd.read_csv(train_file))
    data = contents2characters(df['content'])
    vec = create_vectorizer(data)
    vec_transformed = vec.transform(data)
    clf = RandomForestClassifier().fit(vec_transformed, df['label'])
    with open(outfile, "wb") as f:
        pickle.dump(clf, f)
    return clf


def predict(clf, vec, contents):
    return clf.predict_proba(contentchar2bow(vec, contents2characters(contents)))


def load(clffile="model.pkl", vecfile="vec.pkl"):
    with open(vecfile,"rb") as f:
        vec = pickle.load(f)

    with open(clffile,"rb") as f:
        clf = pickle.load(f)

    return clf, vec

if __name__ == "__main__":
    train()
