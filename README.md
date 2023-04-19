 <img src="logo.png" width="125" height="125" align="right" />

# scikit-prune

> Prune your sklearn models.

## Installation 

```
python -m pip install scikit-prune
```

## Quickstart

Deep learning libraries offer pruning techniques to ensure that the
models are lightweight when they are stored on disk. It's a technique
that makes a lot of sense; you often don't need float64 numbers to
represent the weights of a machine learning model. 

It got me thinking, would such a technique also work in scikit-learn? 

## Enter `scikit-prune`

As a demo, let's say that we're dealing with a text classification use-case. 

```python
from sklearn.datasets import fetch_20newsgroups

text = fetch_20newsgroups()['data']
```

Then we might have a pipeline that fetches the sparse tf/idf features from
this text and then turns these into a dense representation via SVD. 

```python
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

pipe = make_pipeline(TfidfVectorizer(), TruncatedSVD(300))
pipe.fit(text)
```

Then we can choose to save this pipeline on disk, preferably via
a system like [skops](https://github.com/skops-dev/skops).

```python
from skops.io import dump

dump(pipe, "piper-orig.skops")
```

This results in a 275Mb file on disk, which is actually kind of big, and
the most significant chunk of these megabytes are spent on the float64 numpy 
arrays that belong to the SVD object. 

With this library, you can shrink that down a bit. 

```python
from skprune import prune 

dump(prune(pipe), "piper-lite.skops")
```

The `prune` function takes all the `float64` arrays in the pipeline and casts
them to become `float16` arrays instead. And as a result the file is fair bit lighter: only 126Mb on disk. Which is a step
in the right direction. You can get it down even further by saving it 
as a ZIP file which moves it closer to 41Mb. 

## Caveats 

This technique can save a bunch of disk space for sure, but at least theoretically,
it can _also_ lead to some numerical mishaps when you try to apply the pruned pipeline. 
Always make sure that you check and evaluate the pruned pipeline before doing anything
in production with it! 

It's also good to remember that your results may certainly vary. In our example
the `TruncatedSVD` component was the culprit because it was dealing with a _very_ large internal
matrix. If your pipeline doesn't have very large matrices, you probably won't get
big savings in disk space.
