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


class ExperimentRequest(object):
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
        'nodes': 'list[Alias]',
        'name': 'str',
        'duration': 'int',
        'type': 'str',
        'reservation': 'int',
        'profiles': 'CommonExperimentRequestProfiles',
        'mobilities': 'CommonExperimentRequestMobilities',
        'profileassociations': 'list[AliasMobilityAssociation]',
        'firmwareassociations': 'list[AliasFirmwareAssociation]',
        'mobilityassociations': 'list[AliasMobilityAssociation]',
        'siteassociations': 'ScriptAssociations'
    }

    attribute_map = {
        'nodes': 'nodes',
        'name': 'name',
        'duration': 'duration',
        'type': 'type',
        'reservation': 'reservation',
        'profiles': 'profiles',
        'mobilities': 'mobilities',
        'profileassociations': 'profileassociations',
        'firmwareassociations': 'firmwareassociations',
        'mobilityassociations': 'mobilityassociations',
        'siteassociations': 'siteassociations'
    }

    composed_hierarchy = {
        'anyOf': [],
        'allOf': [],
        'oneOf': ["ExperimentAlias", "ExperimentPhysical"],
    }

    def __init__(self, nodes=None, name=None, duration=None, type=None, reservation=None, profiles=None, mobilities=None, profileassociations=None, firmwareassociations=None, mobilityassociations=None, siteassociations=None):  # noqa: E501
        """ExperimentRequest - a model defined in OpenAPI"""  # noqa: E501

        self._nodes = None
        self._name = None
        self._duration = None
        self._type = None
        self._reservation = None
        self._profiles = None
        self._mobilities = None
        self._profileassociations = None
        self._firmwareassociations = None
        self._mobilityassociations = None
        self._siteassociations = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        self.type = type
        if reservation is not None:
            self.reservation = reservation
        if profiles is not None:
            self.profiles = profiles
        if mobilities is not None:
            self.mobilities = mobilities
        if profileassociations is not None:
            self.profileassociations = profileassociations
        if firmwareassociations is not None:
            self.firmwareassociations = firmwareassociations
        if mobilityassociations is not None:
            self.mobilityassociations = mobilityassociations
        if siteassociations is not None:
            self.siteassociations = siteassociations

    @property
    def nodes(self):
        """Gets the nodes of this ExperimentRequest.  # noqa: E501


        :return: The nodes of this ExperimentRequest.  # noqa: E501
        :rtype: list[Alias]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ExperimentRequest.


        :param nodes: The nodes of this ExperimentRequest.  # noqa: E501
        :type: list[Alias]
        """

        self._nodes = nodes

    @property
    def name(self):
        """Gets the name of this ExperimentRequest.  # noqa: E501


        :return: The name of this ExperimentRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentRequest.


        :param name: The name of this ExperimentRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def duration(self):
        """Gets the duration of this ExperimentRequest.  # noqa: E501


        :return: The duration of this ExperimentRequest.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ExperimentRequest.


        :param duration: The duration of this ExperimentRequest.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def type(self):
        """Gets the type of this ExperimentRequest.  # noqa: E501


        :return: The type of this ExperimentRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExperimentRequest.


        :param type: The type of this ExperimentRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["physical", "alias"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def reservation(self):
        """Gets the reservation of this ExperimentRequest.  # noqa: E501


        :return: The reservation of this ExperimentRequest.  # noqa: E501
        :rtype: int
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this ExperimentRequest.


        :param reservation: The reservation of this ExperimentRequest.  # noqa: E501
        :type: int
        """

        self._reservation = reservation

    @property
    def profiles(self):
        """Gets the profiles of this ExperimentRequest.  # noqa: E501


        :return: The profiles of this ExperimentRequest.  # noqa: E501
        :rtype: CommonExperimentRequestProfiles
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this ExperimentRequest.


        :param profiles: The profiles of this ExperimentRequest.  # noqa: E501
        :type: CommonExperimentRequestProfiles
        """

        self._profiles = profiles

    @property
    def mobilities(self):
        """Gets the mobilities of this ExperimentRequest.  # noqa: E501


        :return: The mobilities of this ExperimentRequest.  # noqa: E501
        :rtype: CommonExperimentRequestMobilities
        """
        return self._mobilities

    @mobilities.setter
    def mobilities(self, mobilities):
        """Sets the mobilities of this ExperimentRequest.


        :param mobilities: The mobilities of this ExperimentRequest.  # noqa: E501
        :type: CommonExperimentRequestMobilities
        """

        self._mobilities = mobilities

    @property
    def profileassociations(self):
        """Gets the profileassociations of this ExperimentRequest.  # noqa: E501


        :return: The profileassociations of this ExperimentRequest.  # noqa: E501
        :rtype: list[AliasMobilityAssociation]
        """
        return self._profileassociations

    @profileassociations.setter
    def profileassociations(self, profileassociations):
        """Sets the profileassociations of this ExperimentRequest.


        :param profileassociations: The profileassociations of this ExperimentRequest.  # noqa: E501
        :type: list[AliasMobilityAssociation]
        """

        self._profileassociations = profileassociations

    @property
    def firmwareassociations(self):
        """Gets the firmwareassociations of this ExperimentRequest.  # noqa: E501


        :return: The firmwareassociations of this ExperimentRequest.  # noqa: E501
        :rtype: list[AliasFirmwareAssociation]
        """
        return self._firmwareassociations

    @firmwareassociations.setter
    def firmwareassociations(self, firmwareassociations):
        """Sets the firmwareassociations of this ExperimentRequest.


        :param firmwareassociations: The firmwareassociations of this ExperimentRequest.  # noqa: E501
        :type: list[AliasFirmwareAssociation]
        """

        self._firmwareassociations = firmwareassociations

    @property
    def mobilityassociations(self):
        """Gets the mobilityassociations of this ExperimentRequest.  # noqa: E501


        :return: The mobilityassociations of this ExperimentRequest.  # noqa: E501
        :rtype: list[AliasMobilityAssociation]
        """
        return self._mobilityassociations

    @mobilityassociations.setter
    def mobilityassociations(self, mobilityassociations):
        """Sets the mobilityassociations of this ExperimentRequest.


        :param mobilityassociations: The mobilityassociations of this ExperimentRequest.  # noqa: E501
        :type: list[AliasMobilityAssociation]
        """

        self._mobilityassociations = mobilityassociations

    @property
    def siteassociations(self):
        """Gets the siteassociations of this ExperimentRequest.  # noqa: E501


        :return: The siteassociations of this ExperimentRequest.  # noqa: E501
        :rtype: ScriptAssociations
        """
        return self._siteassociations

    @siteassociations.setter
    def siteassociations(self, siteassociations):
        """Sets the siteassociations of this ExperimentRequest.


        :param siteassociations: The siteassociations of this ExperimentRequest.  # noqa: E501
        :type: ScriptAssociations
        """

        self._siteassociations = siteassociations

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
        if not isinstance(other, ExperimentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
