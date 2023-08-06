# -*- coding: utf-8 -*-

# @Time    : 2020/9/8 23:51
# @Email   : 986798607@qq.com
# @Software: PyCharm
# @License: BSD 3-Clause
# -*- coding: utf-8 -*-

"""This is one general method to calculate Efficient global optimization,
This one is with no restrictions on the type of X and model.

"""
import warnings

import numpy as np
import pandas as pd
from scipy import stats


class BaseEgo:
    """
    EGO (Efficient global optimization).

    References:
        Jones, D. R., Schonlau, M. & Welch, W. J.
        Efficient global optimization of expensive black-box functions. J.
        Global Optim. 13, 455–492 (1998)

    Examples:

        >>>me = BaseEgo()
        >>>result = me.rank(y=y, mean_std=mean_std)

    """

    def __init__(self, sign=1):
        self.rank = self.egosearch
        self.sign = sign

    @staticmethod
    def meanandstd(predict_y):
        """calculate meanandstd."""
        mean = np.mean(predict_y, axis=1)
        std = np.std(predict_y, axis=1)
        data_predict = np.column_stack((mean, std))
        print(data_predict.shape)
        return data_predict

    @staticmethod
    def CalculateEi(y0, mean_std0, flexibility=0.0, sign=1):

        """calculate EI."""
        y = sign * y0
        if not isinstance(y0, float):
            ym = max(y)
        else:
            ym = y
        mean_std = np.copy(mean_std0)
        mean_std[:, 0] = mean_std[:, 0] * sign

        ego = (mean_std[:, 0] - (ym - flexibility)) / (mean_std[:, 1])
        ei_ego = mean_std[:, 1] * ego * stats.norm.cdf(ego) + mean_std[:, 1] * stats.norm.pdf(ego)
        kg = (mean_std[:, 0] - max(max(mean_std[:, 0]), ym - flexibility)) / (mean_std[:, 1])
        ei_kg = mean_std[:, 1] * kg * stats.norm.cdf(kg) + mean_std[:, 1] * stats.norm.pdf(kg)
        max_P = stats.norm.cdf(ego)
        ei = np.column_stack((mean_std0, ei_ego, ei_kg, max_P))

        if np.sum(np.isfinite(ei_ego)) == len(ei_ego):
            raise ValueError("There are too much 'nan' for ei_kg!!! "
                          "\n1. The models may be the same, please keep them "
                          "difference by using different training data.\n"
                          "2. The predicted space are out of ability of models, "
                          "please using data near the training data.")

        elif np.sum(np.isfinite(ei_ego)) < len(ei_ego)/3:
            warnings.warn("There are too much 'nan' for ei_kg!!! "
                          "\n1. The models may be the same, please keep them "
                          "difference by using different training data.\n"
                          "2. The predicted space are out of ability of models, "
                          "please using data near the training data."
                          )

        print('Ego is done.')
        return ei

    def egosearch(self, y, mean_std, searchspace=None, rankway="ego", return_type="pd", flexibility=0, fraction=1000, ):
        """
        Result is 2 dimensions array.
        1st column = sequence number,\n
        2nd part = your search space,\n
        3rd part = mean,std,ego,kg,maxp,sequentially.

        Parameters
        ----------
        y: np.ndarray of shape (n_sample_train, 1)
            train y.
        mean_std: np.ndarray of shape (n_sample_pre, n_feature)
            mean_std of n times of prediction on search space.
            First column is mean and second is std.
        rankway : str
            ["ego","kg","maxp","No"]
            resort the result by rankway name.
        searchspace : np.ndarray of shape (n_sample_pre, n_feature)
            search space, the search space in BaseEgo is not used, just as one placeholder for corresponding .
        return_type: str
            "pd" or "np"
        fraction:int
            choice top n_sample/fraction.
        flexibility:float
            Flexibility to calculate EI, the bigger flexibility, the more search space Ei >0.
            make sure less than max(y) for max problem.

        Returns
        ----------
        table:np.ndarray (2d), pd.Dateframe

        """
        if flexibility != 0:
            warnings.warn(
                "``Flexibility`` means reduction of y boundary, Please use it if you know what you are doing.")

        reverse = False
        if rankway not in ['ego', 'kg', 'maxp', 'no', 'mean','std']:
            print('Don\'t kidding me,checking rankway=what?\a')
        else:

            result = self.CalculateEi(y, mean_std, flexibility=flexibility, sign=self.sign)
            bianhao = np.arange(0, len(result)).reshape(-1, 1)
            if searchspace is None:
                searchspace = bianhao
            result1 = np.column_stack((bianhao, searchspace, result))

            # for all score: [-3,-2,-1] could check by one [-3]
            assert not np.all(result1[:, -3] <= 1e-10), "All the ego score is 0, This is invalid calculation. " \
                                                        "Please try these methods:\n" \
                                                        "1. Improve your model precision, especially near the expected scope for y. " \
                                                        "For example, for max proplem, the point near the maximum y should be accurate by model.\n" \
                                                        "2. Make sure your search space near the training space.\n" \
                                                        "3. If the above methods are still unable to solve, add flexibility to find point by reduction of y boundary. ()\n"
            kv = {"mean":-5,"std":-4,"ego":-3,"kg":-2,"maxp":-1}

            if rankway != "no":
                paixu = np.argsort(-result1[:, kv[rankway]])
            else:
                paixu = bianhao

            if paixu.size >= fraction:
                select_number = paixu[:int(paixu.size / fraction)]
            else:
                print(
                    "search space grid number {} is smaller than fraction, the ``fraction`` parameter is ignored.".format(
                        paixu.size))
                select_number = paixu

            result1 = result1[select_number]

            if return_type != "pd":
                return result1
            else:
                result1 = pd.DataFrame(result1)
                fea = ["feature%d" % i for i in range(searchspace.shape[1])]
                mean_stds = ["mean_std%d" % i for i in range(mean_std.shape[1])]
                name = ["number"] + fea + mean_stds + ['ego', 'kg', 'maxp']
                result1.columns = name
                return result1
