import unittest

from AutoSklearn.components.regression.random_forest import RandomForest
from AutoSklearn.util import _test_regressor

import sklearn.metrics


class RandomForestComponentTest(unittest.TestCase):
    def test_default_configuration(self):
        for i in range(10):

            predictions, targets = _test_regressor(RandomForest,
                                                   dataset='diabetes')
            self.assertAlmostEqual(0.33418320818089353, #0.30805962106685625,
                sklearn.metrics.r2_score(y_true=targets, y_pred=predictions))