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


class InlineObject5(object):
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
        'script': 'file',
        'scriptconfig': 'file',
        'scriptassociation': 'ScriptAssociations'
    }

    attribute_map = {
        'script': 'script',
        'scriptconfig': 'scriptconfig',
        'scriptassociation': 'scriptassociation'
    }

    def __init__(self, script=None, scriptconfig=None, scriptassociation=None):  # noqa: E501
        """InlineObject5 - a model defined in OpenAPI"""  # noqa: E501

        self._script = None
        self._scriptconfig = None
        self._scriptassociation = None
        self.discriminator = None

        if script is not None:
            self.script = script
        if scriptconfig is not None:
            self.scriptconfig = scriptconfig
        if scriptassociation is not None:
            self.scriptassociation = scriptassociation

    @property
    def script(self):
        """Gets the script of this InlineObject5.  # noqa: E501

        script binary file  # noqa: E501

        :return: The script of this InlineObject5.  # noqa: E501
        :rtype: file
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this InlineObject5.

        script binary file  # noqa: E501

        :param script: The script of this InlineObject5.  # noqa: E501
        :type: file
        """

        self._script = script

    @property
    def scriptconfig(self):
        """Gets the scriptconfig of this InlineObject5.  # noqa: E501

        script config file  # noqa: E501

        :return: The scriptconfig of this InlineObject5.  # noqa: E501
        :rtype: file
        """
        return self._scriptconfig

    @scriptconfig.setter
    def scriptconfig(self, scriptconfig):
        """Sets the scriptconfig of this InlineObject5.

        script config file  # noqa: E501

        :param scriptconfig: The scriptconfig of this InlineObject5.  # noqa: E501
        :type: file
        """

        self._scriptconfig = scriptconfig

    @property
    def scriptassociation(self):
        """Gets the scriptassociation of this InlineObject5.  # noqa: E501


        :return: The scriptassociation of this InlineObject5.  # noqa: E501
        :rtype: ScriptAssociations
        """
        return self._scriptassociation

    @scriptassociation.setter
    def scriptassociation(self, scriptassociation):
        """Sets the scriptassociation of this InlineObject5.


        :param scriptassociation: The scriptassociation of this InlineObject5.  # noqa: E501
        :type: ScriptAssociations
        """

        self._scriptassociation = scriptassociation

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
        if not isinstance(other, InlineObject5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
