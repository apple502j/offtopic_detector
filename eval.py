from model import *
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def cross_val(clf, datafile="content.csv", cv=5):
    df = shuffle(pd.read_csv(datafile))
    data = contents2characters(df['content'])
    vec = create_vectorizer(data)
    vec_transformed = vec.transform(data)
    return cross_val_score(clf, vec_transformed, df['label'], scoring="roc_auc", cv=cv)


if __name__ == "__main__":
    print(cross_val(RandomForestClassifier()))
    print(cross_val(LogisticRegression()))
