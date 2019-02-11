# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProfileRadio(object):
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
        'mode': 'str',
        'num_per_channel': 'int',
        'period': 'int',
        'channels': 'list[int]'
    }

    attribute_map = {
        'mode': 'mode',
        'num_per_channel': 'num_per_channel',
        'period': 'period',
        'channels': 'channels'
    }

    def __init__(self, mode=None, num_per_channel=None, period=None, channels=None):  # noqa: E501
        """ProfileRadio - a model defined in OpenAPI"""  # noqa: E501

        self._mode = None
        self._num_per_channel = None
        self._period = None
        self._channels = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if num_per_channel is not None:
            self.num_per_channel = num_per_channel
        if period is not None:
            self.period = period
        if channels is not None:
            self.channels = channels

    @property
    def mode(self):
        """Gets the mode of this ProfileRadio.  # noqa: E501


        :return: The mode of this ProfileRadio.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ProfileRadio.


        :param mode: The mode of this ProfileRadio.  # noqa: E501
        :type: str
        """
        allowed_values = ["rssi", "sniffer"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def num_per_channel(self):
        """Gets the num_per_channel of this ProfileRadio.  # noqa: E501


        :return: The num_per_channel of this ProfileRadio.  # noqa: E501
        :rtype: int
        """
        return self._num_per_channel

    @num_per_channel.setter
    def num_per_channel(self, num_per_channel):
        """Sets the num_per_channel of this ProfileRadio.


        :param num_per_channel: The num_per_channel of this ProfileRadio.  # noqa: E501
        :type: int
        """
        if num_per_channel is not None and num_per_channel > 255:  # noqa: E501
            raise ValueError("Invalid value for `num_per_channel`, must be a value less than or equal to `255`")  # noqa: E501
        if num_per_channel is not None and num_per_channel < 0:  # noqa: E501
            raise ValueError("Invalid value for `num_per_channel`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_per_channel = num_per_channel

    @property
    def period(self):
        """Gets the period of this ProfileRadio.  # noqa: E501


        :return: The period of this ProfileRadio.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ProfileRadio.


        :param period: The period of this ProfileRadio.  # noqa: E501
        :type: int
        """
        if period is not None and period > 65535:  # noqa: E501
            raise ValueError("Invalid value for `period`, must be a value less than or equal to `65535`")  # noqa: E501
        if period is not None and period < 1:  # noqa: E501
            raise ValueError("Invalid value for `period`, must be a value greater than or equal to `1`")  # noqa: E501

        self._period = period

    @property
    def channels(self):
        """Gets the channels of this ProfileRadio.  # noqa: E501


        :return: The channels of this ProfileRadio.  # noqa: E501
        :rtype: list[int]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ProfileRadio.


        :param channels: The channels of this ProfileRadio.  # noqa: E501
        :type: list[int]
        """

        self._channels = channels

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
        if not isinstance(other, ProfileRadio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
