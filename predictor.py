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

    def predict_list(self, path_list, is_url=True):
        if is_url:
            return predict(self.clf, self.vec, [get_content(path) for path in path_list])
        else:
            for path in path_list:
                data = []
                with open(path) as f:
                    data.append(f.read())
            return predict(self.clf, self.vec, data)


if __name__ == "__main__":
    import sys
    predictor = Predictor()
    print(predictor.predict(sys.argv[1]))
