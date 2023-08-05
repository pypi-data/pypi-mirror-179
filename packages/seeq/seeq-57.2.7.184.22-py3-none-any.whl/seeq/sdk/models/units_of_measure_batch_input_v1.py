# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 57.2.7-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class UnitsOfMeasureBatchInputV1(object):
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
        'units_of_measure': 'list[str]'
    }

    attribute_map = {
        'units_of_measure': 'unitsOfMeasure'
    }

    def __init__(self, units_of_measure=None):
        """
        UnitsOfMeasureBatchInputV1 - a model defined in Swagger
        """

        self._units_of_measure = None

        if units_of_measure is not None:
          self.units_of_measure = units_of_measure

    @property
    def units_of_measure(self):
        """
        Gets the units_of_measure of this UnitsOfMeasureBatchInputV1.
        A list of strings representing units of measure to look up

        :return: The units_of_measure of this UnitsOfMeasureBatchInputV1.
        :rtype: list[str]
        """
        return self._units_of_measure

    @units_of_measure.setter
    def units_of_measure(self, units_of_measure):
        """
        Sets the units_of_measure of this UnitsOfMeasureBatchInputV1.
        A list of strings representing units of measure to look up

        :param units_of_measure: The units_of_measure of this UnitsOfMeasureBatchInputV1.
        :type: list[str]
        """
        if units_of_measure is None:
            raise ValueError("Invalid value for `units_of_measure`, must not be `None`")

        self._units_of_measure = units_of_measure

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
        if not isinstance(other, UnitsOfMeasureBatchInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
