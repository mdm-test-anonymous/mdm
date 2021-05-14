#!/usr/bin/env python

"""Tests for `mdm` package."""


import unittest
import mdm


class TestMdm(unittest.TestCase):
    """Tests for `mdm` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.raw_data = mdm.datas.get("data/", "dataset.csv")
        self.data = mdm.datas.transform(self.raw_data)
        self.X_train, self.y_train, self.X_dev, self.y_dev, self.X_test, self.y_test = mdm.datas.split(self.data,
                                                                                                       'activity',
                                                                                                       pct_test=0.2)
    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_get_data(self):
        """Test data import"""
        self.assertEqual(len(self.raw_data), 900)

    def test_001_transform_data(self):
        """Test data transformation"""
        self.assertEqual(len(self.data.columns), 8)

    def test_002_model_training(self):
        """Test model training"""
        acc, model = mdm.models.train(self.X_train, self.y_train, self.X_dev.append(self.X_test),
                                      self.y_dev.append(self.y_test))
        self.assertTrue(acc > 0.7)
