# -*- coding: utf-8 -*-

from .context import data_dictionary

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(data_dictionary.hmm())


if __name__ == '__main__':
    unittest.main()
