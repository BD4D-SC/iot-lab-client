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


class ExperimentResponse(object):
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
        'user': 'str',
        'nb_nodes': 'int',
        'state': 'str',
        'submitted_duration': 'int',
        'effective_duration': 'int',
        'scheduled_date': 'str',
        'start_date': 'str',
        'stop_date': 'str',
        'submission_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user': 'user',
        'nb_nodes': 'nb_nodes',
        'state': 'state',
        'submitted_duration': 'submitted_duration',
        'effective_duration': 'effective_duration',
        'scheduled_date': 'scheduled_date',
        'start_date': 'start_date',
        'stop_date': 'stop_date',
        'submission_date': 'submission_date'
    }

    def __init__(self, id=None, name=None, user=None, nb_nodes=None, state=None, submitted_duration=None, effective_duration=None, scheduled_date=None, start_date=None, stop_date=None, submission_date=None):  # noqa: E501
        """ExperimentResponse - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._user = None
        self._nb_nodes = None
        self._state = None
        self._submitted_duration = None
        self._effective_duration = None
        self._scheduled_date = None
        self._start_date = None
        self._stop_date = None
        self._submission_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
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

    @property
    def id(self):
        """Gets the id of this ExperimentResponse.  # noqa: E501


        :return: The id of this ExperimentResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExperimentResponse.


        :param id: The id of this ExperimentResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExperimentResponse.  # noqa: E501


        :return: The name of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentResponse.


        :param name: The name of this ExperimentResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user(self):
        """Gets the user of this ExperimentResponse.  # noqa: E501


        :return: The user of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ExperimentResponse.


        :param user: The user of this ExperimentResponse.  # noqa: E501
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
        """Gets the nb_nodes of this ExperimentResponse.  # noqa: E501


        :return: The nb_nodes of this ExperimentResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_nodes

    @nb_nodes.setter
    def nb_nodes(self, nb_nodes):
        """Sets the nb_nodes of this ExperimentResponse.


        :param nb_nodes: The nb_nodes of this ExperimentResponse.  # noqa: E501
        :type: int
        """

        self._nb_nodes = nb_nodes

    @property
    def state(self):
        """Gets the state of this ExperimentResponse.  # noqa: E501


        :return: The state of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ExperimentResponse.


        :param state: The state of this ExperimentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "Launching", "Waiting", "Stopped", "Finishing", "Terminated", "Error"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def submitted_duration(self):
        """Gets the submitted_duration of this ExperimentResponse.  # noqa: E501


        :return: The submitted_duration of this ExperimentResponse.  # noqa: E501
        :rtype: int
        """
        return self._submitted_duration

    @submitted_duration.setter
    def submitted_duration(self, submitted_duration):
        """Sets the submitted_duration of this ExperimentResponse.


        :param submitted_duration: The submitted_duration of this ExperimentResponse.  # noqa: E501
        :type: int
        """

        self._submitted_duration = submitted_duration

    @property
    def effective_duration(self):
        """Gets the effective_duration of this ExperimentResponse.  # noqa: E501


        :return: The effective_duration of this ExperimentResponse.  # noqa: E501
        :rtype: int
        """
        return self._effective_duration

    @effective_duration.setter
    def effective_duration(self, effective_duration):
        """Sets the effective_duration of this ExperimentResponse.


        :param effective_duration: The effective_duration of this ExperimentResponse.  # noqa: E501
        :type: int
        """

        self._effective_duration = effective_duration

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this ExperimentResponse.  # noqa: E501


        :return: The scheduled_date of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this ExperimentResponse.


        :param scheduled_date: The scheduled_date of this ExperimentResponse.  # noqa: E501
        :type: str
        """

        self._scheduled_date = scheduled_date

    @property
    def start_date(self):
        """Gets the start_date of this ExperimentResponse.  # noqa: E501


        :return: The start_date of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExperimentResponse.


        :param start_date: The start_date of this ExperimentResponse.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def stop_date(self):
        """Gets the stop_date of this ExperimentResponse.  # noqa: E501


        :return: The stop_date of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._stop_date

    @stop_date.setter
    def stop_date(self, stop_date):
        """Sets the stop_date of this ExperimentResponse.


        :param stop_date: The stop_date of this ExperimentResponse.  # noqa: E501
        :type: str
        """

        self._stop_date = stop_date

    @property
    def submission_date(self):
        """Gets the submission_date of this ExperimentResponse.  # noqa: E501


        :return: The submission_date of this ExperimentResponse.  # noqa: E501
        :rtype: str
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this ExperimentResponse.


        :param submission_date: The submission_date of this ExperimentResponse.  # noqa: E501
        :type: str
        """

        self._submission_date = submission_date

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
        if not isinstance(other, ExperimentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
