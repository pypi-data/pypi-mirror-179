# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 59.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class PropertyOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'name': 'str',
        'status_message': 'str',
        'unit_of_measure': 'str',
        'value': 'str'
    }

    attribute_map = {
        'href': 'href',
        'name': 'name',
        'status_message': 'statusMessage',
        'unit_of_measure': 'unitOfMeasure',
        'value': 'value'
    }

    def __init__(self, href=None, name=None, status_message=None, unit_of_measure=None, value=None):
        """
        PropertyOutputV1 - a model defined in Swagger
        """

        self._href = None
        self._name = None
        self._status_message = None
        self._unit_of_measure = None
        self._value = None

        if href is not None:
          self.href = href
        if name is not None:
          self.name = name
        if status_message is not None:
          self.status_message = status_message
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure
        if value is not None:
          self.value = value

    @property
    def href(self):
        """
        Gets the href of this PropertyOutputV1.
        The href that can be used to interact with the property

        :return: The href of this PropertyOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this PropertyOutputV1.
        The href that can be used to interact with the property

        :param href: The href of this PropertyOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def name(self):
        """
        Gets the name of this PropertyOutputV1.
        The name of this property

        :return: The name of this PropertyOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PropertyOutputV1.
        The name of this property

        :param name: The name of this PropertyOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status_message(self):
        """
        Gets the status_message of this PropertyOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this PropertyOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this PropertyOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this PropertyOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this PropertyOutputV1.
        The unit of measure for this property's value

        :return: The unit_of_measure of this PropertyOutputV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this PropertyOutputV1.
        The unit of measure for this property's value

        :param unit_of_measure: The unit_of_measure of this PropertyOutputV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def value(self):
        """
        Gets the value of this PropertyOutputV1.
        The value of this property

        :return: The value of this PropertyOutputV1.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PropertyOutputV1.
        The value of this property

        :param value: The value of this PropertyOutputV1.
        :type: str
        """

        self._value = value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PropertyOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
