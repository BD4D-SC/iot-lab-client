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


class Circuit(object):
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
        'coordinates': 'dict(str, Point)',
        'loop': 'bool',
        'name': 'str',
        'site': 'str',
        'type': 'str',
        'points': 'list[str]'
    }

    attribute_map = {
        'coordinates': 'coordinates',
        'loop': 'loop',
        'name': 'name',
        'site': 'site',
        'type': 'type',
        'points': 'points'
    }

    def __init__(self, coordinates=None, loop=None, name=None, site=None, type=None, points=None):  # noqa: E501
        """Circuit - a model defined in OpenAPI"""  # noqa: E501

        self._coordinates = None
        self._loop = None
        self._name = None
        self._site = None
        self._type = None
        self._points = None
        self.discriminator = None

        if coordinates is not None:
            self.coordinates = coordinates
        if loop is not None:
            self.loop = loop
        if name is not None:
            self.name = name
        if site is not None:
            self.site = site
        if type is not None:
            self.type = type
        if points is not None:
            self.points = points

    @property
    def coordinates(self):
        """Gets the coordinates of this Circuit.  # noqa: E501


        :return: The coordinates of this Circuit.  # noqa: E501
        :rtype: dict(str, Point)
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Circuit.


        :param coordinates: The coordinates of this Circuit.  # noqa: E501
        :type: dict(str, Point)
        """

        self._coordinates = coordinates

    @property
    def loop(self):
        """Gets the loop of this Circuit.  # noqa: E501


        :return: The loop of this Circuit.  # noqa: E501
        :rtype: bool
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this Circuit.


        :param loop: The loop of this Circuit.  # noqa: E501
        :type: bool
        """

        self._loop = loop

    @property
    def name(self):
        """Gets the name of this Circuit.  # noqa: E501


        :return: The name of this Circuit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Circuit.


        :param name: The name of this Circuit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site(self):
        """Gets the site of this Circuit.  # noqa: E501


        :return: The site of this Circuit.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Circuit.


        :param site: The site of this Circuit.  # noqa: E501
        :type: str
        """

        self._site = site

    @property
    def type(self):
        """Gets the type of this Circuit.  # noqa: E501


        :return: The type of this Circuit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Circuit.


        :param type: The type of this Circuit.  # noqa: E501
        :type: str
        """
        allowed_values = ["userdefined", "predefined"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def points(self):
        """Gets the points of this Circuit.  # noqa: E501


        :return: The points of this Circuit.  # noqa: E501
        :rtype: list[str]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this Circuit.


        :param points: The points of this Circuit.  # noqa: E501
        :type: list[str]
        """

        self._points = points

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
        if not isinstance(other, Circuit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other