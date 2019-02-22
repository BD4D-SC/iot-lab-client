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


class ExperimentSubmission(object):
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
        'id': 'int',
        'name': 'str',
        'type': 'str',
        'user': 'str',
        'nb_nodes': 'int',
        'state': 'str',
        'submitted_duration': 'int',
        'effective_duration': 'int',
        'scheduled_date': 'str',
        'start_date': 'str',
        'stop_date': 'str',
        'submission_date': 'str',
        'profiles': 'CommonExperimentRequestProfiles',
        'mobilities': 'CommonExperimentRequestMobilities',
        'nodes': 'list[Alias]',
        'duration': 'int',
        'reservation': 'int',
        'profileassociations': 'list[ProfileAliasAssociation]',
        'firmwareassociations': 'list[FirmwareAliasAssociation]',
        'mobilityassociations': 'list[MobilityAliasAssociation]',
        'siteassociations': 'ScriptAssociations'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'user': 'user',
        'nb_nodes': 'nb_nodes',
        'state': 'state',
        'submitted_duration': 'submitted_duration',
        'effective_duration': 'effective_duration',
        'scheduled_date': 'scheduled_date',
        'start_date': 'start_date',
        'stop_date': 'stop_date',
        'submission_date': 'submission_date',
        'profiles': 'profiles',
        'mobilities': 'mobilities',
        'nodes': 'nodes',
        'duration': 'duration',
        'reservation': 'reservation',
        'profileassociations': 'profileassociations',
        'firmwareassociations': 'firmwareassociations',
        'mobilityassociations': 'mobilityassociations',
        'siteassociations': 'siteassociations'
    }

    discriminator_value_class_map = {
        
        'physical': 'ExperimentSubmissionPhysical',
        'alias': 'ExperimentSubmissionAlias'
    }

    def __init__(self, id=None, name=None, type=None, user=None, nb_nodes=None, state=None, submitted_duration=None, effective_duration=None, scheduled_date=None, start_date=None, stop_date=None, submission_date=None, profiles=None, mobilities=None, nodes=None, duration=None, reservation=None, profileassociations=None, firmwareassociations=None, mobilityassociations=None, siteassociations=None):  # noqa: E501
        """ExperimentSubmission - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._user = None
        self._nb_nodes = None
        self._state = None
        self._submitted_duration = None
        self._effective_duration = None
        self._scheduled_date = None
        self._start_date = None
        self._stop_date = None
        self._submission_date = None
        self._profiles = None
        self._mobilities = None
        self._nodes = None
        self._duration = None
        self._reservation = None
        self._profileassociations = None
        self._firmwareassociations = None
        self._mobilityassociations = None
        self._siteassociations = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.type = type
        if user is not None:
            self.user = user
        if nb_nodes is not None:
            self.nb_nodes = nb_nodes
        if state is not None:
            self.state = state
        if submitted_duration is not None:
            self.submitted_duration = submitted_duration
        if effective_duration is not None:
            self.effective_duration = effective_duration
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if start_date is not None:
            self.start_date = start_date
        if stop_date is not None:
            self.stop_date = stop_date
        if submission_date is not None:
            self.submission_date = submission_date
        if profiles is not None:
            self.profiles = profiles
        if mobilities is not None:
            self.mobilities = mobilities
        if nodes is not None:
            self.nodes = nodes
        if duration is not None:
            self.duration = duration
        if reservation is not None:
            self.reservation = reservation
        if profileassociations is not None:
            self.profileassociations = profileassociations
        if firmwareassociations is not None:
            self.firmwareassociations = firmwareassociations
        if mobilityassociations is not None:
            self.mobilityassociations = mobilityassociations
        if siteassociations is not None:
            self.siteassociations = siteassociations

    @property
    def id(self):
        """Gets the id of this ExperimentSubmission.  # noqa: E501


        :return: The id of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExperimentSubmission.


        :param id: The id of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExperimentSubmission.  # noqa: E501


        :return: The name of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentSubmission.


        :param name: The name of this ExperimentSubmission.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ExperimentSubmission.  # noqa: E501


        :return: The type of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExperimentSubmission.


        :param type: The type of this ExperimentSubmission.  # noqa: E501
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
    def user(self):
        """Gets the user of this ExperimentSubmission.  # noqa: E501


        :return: The user of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ExperimentSubmission.


        :param user: The user of this ExperimentSubmission.  # noqa: E501
        :type: str
        """
        if user is not None and len(user) > 20:
            raise ValueError("Invalid value for `user`, length must be less than or equal to `20`")  # noqa: E501
        if user is not None and len(user) < 4:
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `4`")  # noqa: E501
        if user is not None and not re.search(r'^[a-z][0-9a-z]{3,19}$', user):  # noqa: E501
            raise ValueError(r"Invalid value for `user`, must be a follow pattern or equal to `/^[a-z][0-9a-z]{3,19}$/`")  # noqa: E501

        self._user = user

    @property
    def nb_nodes(self):
        """Gets the nb_nodes of this ExperimentSubmission.  # noqa: E501


        :return: The nb_nodes of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._nb_nodes

    @nb_nodes.setter
    def nb_nodes(self, nb_nodes):
        """Sets the nb_nodes of this ExperimentSubmission.


        :param nb_nodes: The nb_nodes of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._nb_nodes = nb_nodes

    @property
    def state(self):
        """Gets the state of this ExperimentSubmission.  # noqa: E501


        :return: The state of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ExperimentSubmission.


        :param state: The state of this ExperimentSubmission.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "Launching", "Waiting", "Stopped", "Finishing", "Terminated", "toLaunch"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def submitted_duration(self):
        """Gets the submitted_duration of this ExperimentSubmission.  # noqa: E501


        :return: The submitted_duration of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._submitted_duration

    @submitted_duration.setter
    def submitted_duration(self, submitted_duration):
        """Sets the submitted_duration of this ExperimentSubmission.


        :param submitted_duration: The submitted_duration of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._submitted_duration = submitted_duration

    @property
    def effective_duration(self):
        """Gets the effective_duration of this ExperimentSubmission.  # noqa: E501


        :return: The effective_duration of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._effective_duration

    @effective_duration.setter
    def effective_duration(self, effective_duration):
        """Sets the effective_duration of this ExperimentSubmission.


        :param effective_duration: The effective_duration of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._effective_duration = effective_duration

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this ExperimentSubmission.  # noqa: E501


        :return: The scheduled_date of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this ExperimentSubmission.


        :param scheduled_date: The scheduled_date of this ExperimentSubmission.  # noqa: E501
        :type: str
        """

        self._scheduled_date = scheduled_date

    @property
    def start_date(self):
        """Gets the start_date of this ExperimentSubmission.  # noqa: E501


        :return: The start_date of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExperimentSubmission.


        :param start_date: The start_date of this ExperimentSubmission.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def stop_date(self):
        """Gets the stop_date of this ExperimentSubmission.  # noqa: E501


        :return: The stop_date of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._stop_date

    @stop_date.setter
    def stop_date(self, stop_date):
        """Sets the stop_date of this ExperimentSubmission.


        :param stop_date: The stop_date of this ExperimentSubmission.  # noqa: E501
        :type: str
        """

        self._stop_date = stop_date

    @property
    def submission_date(self):
        """Gets the submission_date of this ExperimentSubmission.  # noqa: E501


        :return: The submission_date of this ExperimentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this ExperimentSubmission.


        :param submission_date: The submission_date of this ExperimentSubmission.  # noqa: E501
        :type: str
        """

        self._submission_date = submission_date

    @property
    def profiles(self):
        """Gets the profiles of this ExperimentSubmission.  # noqa: E501


        :return: The profiles of this ExperimentSubmission.  # noqa: E501
        :rtype: CommonExperimentRequestProfiles
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this ExperimentSubmission.


        :param profiles: The profiles of this ExperimentSubmission.  # noqa: E501
        :type: CommonExperimentRequestProfiles
        """

        self._profiles = profiles

    @property
    def mobilities(self):
        """Gets the mobilities of this ExperimentSubmission.  # noqa: E501


        :return: The mobilities of this ExperimentSubmission.  # noqa: E501
        :rtype: CommonExperimentRequestMobilities
        """
        return self._mobilities

    @mobilities.setter
    def mobilities(self, mobilities):
        """Sets the mobilities of this ExperimentSubmission.


        :param mobilities: The mobilities of this ExperimentSubmission.  # noqa: E501
        :type: CommonExperimentRequestMobilities
        """

        self._mobilities = mobilities

    @property
    def nodes(self):
        """Gets the nodes of this ExperimentSubmission.  # noqa: E501


        :return: The nodes of this ExperimentSubmission.  # noqa: E501
        :rtype: list[Alias]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ExperimentSubmission.


        :param nodes: The nodes of this ExperimentSubmission.  # noqa: E501
        :type: list[Alias]
        """

        self._nodes = nodes

    @property
    def duration(self):
        """Gets the duration of this ExperimentSubmission.  # noqa: E501


        :return: The duration of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ExperimentSubmission.


        :param duration: The duration of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def reservation(self):
        """Gets the reservation of this ExperimentSubmission.  # noqa: E501


        :return: The reservation of this ExperimentSubmission.  # noqa: E501
        :rtype: int
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this ExperimentSubmission.


        :param reservation: The reservation of this ExperimentSubmission.  # noqa: E501
        :type: int
        """

        self._reservation = reservation

    @property
    def profileassociations(self):
        """Gets the profileassociations of this ExperimentSubmission.  # noqa: E501


        :return: The profileassociations of this ExperimentSubmission.  # noqa: E501
        :rtype: list[ProfileAliasAssociation]
        """
        return self._profileassociations

    @profileassociations.setter
    def profileassociations(self, profileassociations):
        """Sets the profileassociations of this ExperimentSubmission.


        :param profileassociations: The profileassociations of this ExperimentSubmission.  # noqa: E501
        :type: list[ProfileAliasAssociation]
        """

        self._profileassociations = profileassociations

    @property
    def firmwareassociations(self):
        """Gets the firmwareassociations of this ExperimentSubmission.  # noqa: E501


        :return: The firmwareassociations of this ExperimentSubmission.  # noqa: E501
        :rtype: list[FirmwareAliasAssociation]
        """
        return self._firmwareassociations

    @firmwareassociations.setter
    def firmwareassociations(self, firmwareassociations):
        """Sets the firmwareassociations of this ExperimentSubmission.


        :param firmwareassociations: The firmwareassociations of this ExperimentSubmission.  # noqa: E501
        :type: list[FirmwareAliasAssociation]
        """

        self._firmwareassociations = firmwareassociations

    @property
    def mobilityassociations(self):
        """Gets the mobilityassociations of this ExperimentSubmission.  # noqa: E501


        :return: The mobilityassociations of this ExperimentSubmission.  # noqa: E501
        :rtype: list[MobilityAliasAssociation]
        """
        return self._mobilityassociations

    @mobilityassociations.setter
    def mobilityassociations(self, mobilityassociations):
        """Sets the mobilityassociations of this ExperimentSubmission.


        :param mobilityassociations: The mobilityassociations of this ExperimentSubmission.  # noqa: E501
        :type: list[MobilityAliasAssociation]
        """

        self._mobilityassociations = mobilityassociations

    @property
    def siteassociations(self):
        """Gets the siteassociations of this ExperimentSubmission.  # noqa: E501


        :return: The siteassociations of this ExperimentSubmission.  # noqa: E501
        :rtype: ScriptAssociations
        """
        return self._siteassociations

    @siteassociations.setter
    def siteassociations(self, siteassociations):
        """Sets the siteassociations of this ExperimentSubmission.


        :param siteassociations: The siteassociations of this ExperimentSubmission.  # noqa: E501
        :type: ScriptAssociations
        """

        self._siteassociations = siteassociations

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, ExperimentSubmission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
