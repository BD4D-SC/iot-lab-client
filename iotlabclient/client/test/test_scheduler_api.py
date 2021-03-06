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
from iotlabclient.client.api.scheduler_api import SchedulerApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestSchedulerApi(unittest.TestCase):
    """SchedulerApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.scheduler_api.SchedulerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_experiments_jobs(self):
        """Test case for get_experiments_jobs

        Returns past & future testbed experiments jobs lists  # noqa: E501
        """
        pass

    def test_get_nodes_states(self):
        """Test case for get_nodes_states

        Returns nodes states, past & current  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
