# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iotlabclient.client
from iotlabclient.client.api.experiments_api import ExperimentsApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestExperimentsApi(unittest.TestCase):
    """ExperimentsApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.experiments_api.ExperimentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_experiments(self):
        """Test case for get_experiments

        Returns experiments list  # noqa: E501
        """
        pass

    def test_get_experiments_total(self):
        """Test case for get_experiments_total

        Returns total number of experiments  # noqa: E501
        """
        pass

    def test_get_running_experiments(self):
        """Test case for get_running_experiments

        Returns running testbed experiments list  # noqa: E501
        """
        pass

    def test_submit_experiment(self):
        """Test case for submit_experiment

        Submit an experiment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
