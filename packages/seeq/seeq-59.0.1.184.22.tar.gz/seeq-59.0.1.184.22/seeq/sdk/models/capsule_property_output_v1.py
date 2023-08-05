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


class CapsulePropertyOutputV1(object):
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
        'name': 'str',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'name': 'name',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, name=None, unit_of_measure=None):
        """
        CapsulePropertyOutputV1 - a model defined in Swagger
        """

        self._name = None
        self._unit_of_measure = None

        if name is not None:
          self.name = name
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure

    @property
    def name(self):
        """
        Gets the name of this CapsulePropertyOutputV1.
        Property name

        :return: The name of this CapsulePropertyOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CapsulePropertyOutputV1.
        Property name

        :param name: The name of this CapsulePropertyOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this CapsulePropertyOutputV1.
        The unit of measure that applies to this property. An empty string indicates unitless

        :return: The unit_of_measure of this CapsulePropertyOutputV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this CapsulePropertyOutputV1.
        The unit of measure that applies to this property. An empty string indicates unitless

        :param unit_of_measure: The unit_of_measure of this CapsulePropertyOutputV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if not isinstance(other, CapsulePropertyOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
