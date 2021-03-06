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


class UserResponse(object):
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
        'created': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'login': 'str',
        'email': 'str',
        'country': 'str',
        'organization': 'str',
        'motivations': 'str',
        'city': 'str',
        'category': 'str',
        'sshkeys': 'list[str]',
        'groups': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'created': 'created',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'login': 'login',
        'email': 'email',
        'country': 'country',
        'organization': 'organization',
        'motivations': 'motivations',
        'city': 'city',
        'category': 'category',
        'sshkeys': 'sshkeys',
        'groups': 'groups',
        'status': 'status'
    }

    def __init__(self, created=None, first_name=None, last_name=None, login=None, email=None, country=None, organization=None, motivations=None, city=None, category=None, sshkeys=None, groups=None, status=None):  # noqa: E501
        """UserResponse - a model defined in OpenAPI"""  # noqa: E501

        self._created = None
        self._first_name = None
        self._last_name = None
        self._login = None
        self._email = None
        self._country = None
        self._organization = None
        self._motivations = None
        self._city = None
        self._category = None
        self._sshkeys = None
        self._groups = None
        self._status = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if login is not None:
            self.login = login
        if email is not None:
            self.email = email
        if country is not None:
            self.country = country
        if organization is not None:
            self.organization = organization
        if motivations is not None:
            self.motivations = motivations
        if city is not None:
            self.city = city
        if category is not None:
            self.category = category
        if sshkeys is not None:
            self.sshkeys = sshkeys
        if groups is not None:
            self.groups = groups
        if status is not None:
            self.status = status

    @property
    def created(self):
        """Gets the created of this UserResponse.  # noqa: E501


        :return: The created of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserResponse.


        :param created: The created of this UserResponse.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def first_name(self):
        """Gets the first_name of this UserResponse.  # noqa: E501


        :return: The first_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserResponse.


        :param first_name: The first_name of this UserResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserResponse.  # noqa: E501


        :return: The last_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserResponse.


        :param last_name: The last_name of this UserResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def login(self):
        """Gets the login of this UserResponse.  # noqa: E501


        :return: The login of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserResponse.


        :param login: The login of this UserResponse.  # noqa: E501
        :type: str
        """
        if login is not None and len(login) > 20:
            raise ValueError("Invalid value for `login`, length must be less than or equal to `20`")  # noqa: E501
        if login is not None and len(login) < 4:
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `4`")  # noqa: E501
        if login is not None and not re.search(r'^[a-z][0-9a-z]{3,19}$', login):  # noqa: E501
            raise ValueError(r"Invalid value for `login`, must be a follow pattern or equal to `/^[a-z][0-9a-z]{3,19}$/`")  # noqa: E501

        self._login = login

    @property
    def email(self):
        """Gets the email of this UserResponse.  # noqa: E501


        :return: The email of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResponse.


        :param email: The email of this UserResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def country(self):
        """Gets the country of this UserResponse.  # noqa: E501


        :return: The country of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserResponse.


        :param country: The country of this UserResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def organization(self):
        """Gets the organization of this UserResponse.  # noqa: E501


        :return: The organization of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserResponse.


        :param organization: The organization of this UserResponse.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def motivations(self):
        """Gets the motivations of this UserResponse.  # noqa: E501


        :return: The motivations of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._motivations

    @motivations.setter
    def motivations(self, motivations):
        """Sets the motivations of this UserResponse.


        :param motivations: The motivations of this UserResponse.  # noqa: E501
        :type: str
        """

        self._motivations = motivations

    @property
    def city(self):
        """Gets the city of this UserResponse.  # noqa: E501


        :return: The city of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UserResponse.


        :param city: The city of this UserResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def category(self):
        """Gets the category of this UserResponse.  # noqa: E501


        :return: The category of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UserResponse.


        :param category: The category of this UserResponse.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def sshkeys(self):
        """Gets the sshkeys of this UserResponse.  # noqa: E501


        :return: The sshkeys of this UserResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._sshkeys

    @sshkeys.setter
    def sshkeys(self, sshkeys):
        """Sets the sshkeys of this UserResponse.


        :param sshkeys: The sshkeys of this UserResponse.  # noqa: E501
        :type: list[str]
        """

        self._sshkeys = sshkeys

    @property
    def groups(self):
        """Gets the groups of this UserResponse.  # noqa: E501


        :return: The groups of this UserResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserResponse.


        :param groups: The groups of this UserResponse.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def status(self):
        """Gets the status of this UserResponse.  # noqa: E501


        :return: The status of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserResponse.


        :param status: The status of this UserResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
