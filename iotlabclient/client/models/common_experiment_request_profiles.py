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


class CommonExperimentRequestProfiles(object):
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
        'profilename': 'Profile'
    }

    attribute_map = {
        'profilename': 'profilename'
    }

    def __init__(self, profilename=None):  # noqa: E501
        """CommonExperimentRequestProfiles - a model defined in OpenAPI"""  # noqa: E501

        self._profilename = None
        self.discriminator = None

        if profilename is not None:
            self.profilename = profilename

    @property
    def profilename(self):
        """Gets the profilename of this CommonExperimentRequestProfiles.  # noqa: E501


        :return: The profilename of this CommonExperimentRequestProfiles.  # noqa: E501
        :rtype: Profile
        """
        return self._profilename

    @profilename.setter
    def profilename(self, profilename):
        """Sets the profilename of this CommonExperimentRequestProfiles.


        :param profilename: The profilename of this CommonExperimentRequestProfiles.  # noqa: E501
        :type: Profile
        """

        self._profilename = profilename

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
        if not isinstance(other, CommonExperimentRequestProfiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
