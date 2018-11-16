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
    print(predictor.predict("https://qiita.com/Yuta_Yamamoto/items/fbeb7b31173b3e787fc2"))
    print(predictor.predict("https://qiita.com/riversun/items/29d5264480dd06c7b9fb"))
    print(predictor.predict("https://qiita.com/_EnumHack/items/3d7d50c43523c71ab307"))
