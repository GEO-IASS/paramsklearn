import unittest

from ParamSklearn.components.classification.gradient_boosting import \
    GradientBoostingClassifier
from ParamSklearn.util import _test_classifier, _test_classifier_iterative_fit

import sklearn.metrics


class GradientBoostingComponentTest(unittest.TestCase):
    def test_default_configuration(self):
        for i in range(10):
            predictions, targets = \
                _test_classifier(GradientBoostingClassifier)
            self.assertAlmostEqual(0.95999999999999996,
                sklearn.metrics.accuracy_score(predictions, targets))

    def test_default_configuration_iterative_fit(self):
        for i in range(10):
            predictions, targets = \
                _test_classifier_iterative_fit(GradientBoostingClassifier)
            self.assertAlmostEqual(0.95999999999999996,
                                   sklearn.metrics.accuracy_score(predictions,
                                                                  targets))