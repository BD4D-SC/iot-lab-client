# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Reload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'duration': 'int',
        'reservation': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'reservation': 'reservation'
    }

    def __init__(self, duration=None, reservation=None):  # noqa: E501
        """Reload - a model defined in OpenAPI"""  # noqa: E501

        self._duration = None
        self._reservation = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if reservation is not None:
            self.reservation = reservation

    @property
    def duration(self):
        """Gets the duration of this Reload.  # noqa: E501


        :return: The duration of this Reload.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Reload.


        :param duration: The duration of this Reload.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def reservation(self):
        """Gets the reservation of this Reload.  # noqa: E501


        :return: The reservation of this Reload.  # noqa: E501
        :rtype: int
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this Reload.


        :param reservation: The reservation of this Reload.  # noqa: E501
        :type: int
        """

        self._reservation = reservation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Reload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
