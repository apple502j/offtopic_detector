from model import predict, load
from get_content import get_content

class Predictor:

    def __init__(self):
        self.clf, self.vec = load()

    def predict(self, path, is_url=True):
        if is_url:
            return predict(self.clf, self.vec, [get_content(path)])
        else:
            with open(path) as f:
                return predict(self.clf, self.vec, [f.read()])


if __name__ == "__main__":
    predictor = Predictor()
    print(predictor.predict("https://qiita.com/taku910/items/7e52f1e58d0ea6e7859c"))
    print(predictor.predict("https://qiita.com/Yuta_Yamamoto/items/fbeb7b31173b3e787fc2"))
    print(predictor.predict("https://qiita.com/riversun/items/29d5264480dd06c7b9fb"))
    print(predictor.predict("https://qiita.com/_EnumHack/items/3d7d50c43523c71ab307"))
    print(predictor.predict("https://qiita.com/tani_AI_Academy/items/3edc5effeb386ae3caa9"))
    print(predictor.predict("https://qiita.com/charmston/items/df31a419a4e57ebe86ba"))
    print(predictor.predict("https://qiita.com/rana_kualu/items/afe544b0f5680e81fabc"))
    print(predictor.predict("https://qiita.com/qiitadaisuki/items/2160a390ce91283707a1"))
    print(predictor.predict("https://qiita.com/Kosuke-Szk/items/4b74b5cce84f423b7125"))
    print(predictor.predict("https://qiita.com/Y_F_Acoustics/items/6742a0a8ad6b37a0f4f5"))
    print(predictor.predict("https://qiita.com/ozikot/items/f7e5c346e631de067efb"))
    print(predictor.predict("https://qiita.com/kurogelee/items/1c081a5a7e209e81921c"))
