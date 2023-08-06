# Multiply EGO

EGO (Efficient global optimization) and multiply target EGO method.

References:
Jones, D. R., Schonlau, M. & Welch, W. J. Efficient global optimization of expensive black-box functions. J. Global
Optim. 13, 455–492 (1998)

[![Python Versions](https://img.shields.io/pypi/pyversions/multiego.svg)](https://pypi.org/project/multiego/)
[![Version](https://img.shields.io/github/tag/MGEdata/multiego.svg)](https://github.com/MGEdata/multiego/releases/latest)
![pypi Versions](https://badge.fury.io/py/multiego.svg)

# Install

```bash
pip install multiego
```

# Usage

```bash
if __name__ == "__main__":
    from sklearn.datasets import fetch_california_housing
    import numpy as np
    from multiego.ego import search_space, Ego
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVR

    #####model1#####
    model = SVR() #pre-trained good model with optimized prarmeters for special features
    ###

    X, y = fetch_california_housing(return_X_y=True)
    X = X[:, :5] 
    searchspace_list = [
        np.arange(0.01, 1, 0.1),
        np.array([0, 20, 30, 50, 70, 90]),
        np.arange(1, 10, 1),
        np.array([0, 1]),
        np.arange(0.4, 0.6, 0.02),
    ]
    searchspace = search_space(*searchspace_list)
    #
    me = Ego(searchspace, X, y, 500, model, n_jobs=6)

    re = me.egosearch()
```

Introduction
-------------
[**multiego.ego.Ego**](https://github.com/MGEdata/multiego/blob/master/multiego/ego.py) 

For `sklean-type` single model.

[**multiego.base_ego.BaseEgo**](https://github.com/MGEdata/multiego/blob/master/multiego/base_ego.py)

1. For any user-defined  single model, just need offer mean and std of search space.
2. For  big search space out of memory , just need offer mean and std of search space.

[**multiego.multiplyego.MultiEgo**](https://github.com/MGEdata/multiego/blob/master/multiego/multiplyego.py)

For `sklean-type` models.

[**multiego.base_multiplyego.BaseMultiEgo**](https://github.com/MGEdata/multiego/blob/master/multiego/base_multiplyego.py) 

1. For any user-defined models, just need offer predict_y of search space.
2. For  big search space out of memory, just need offer predict_y of search space.

link
-----------
More examples can be found in [test](https://github.com/MGEdata/multiego/tree/master/test).

More powerful can be found  [mipego](https://github.com/wangronin/MIP-EGO)