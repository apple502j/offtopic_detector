# poem_detector
Detecting whether a Qiita article is good or not.

## how to use?

```python
from predictor import Predictor

pr = Predictor()
pr.predict(Qiita article URL)
```

output is like:

```
[[0.1, 0.9]]
```

0.1 is a probability which means "bad article", and 0.9 is "a prob of good article".

## how it works?

This model is based on RandomForest with character based BoW.

## Training data

good_articles.txt: examples of good articles.
bad_articles.txt: examples of bad articles.