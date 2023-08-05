# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 58.1.3-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class CapsuleInputV1(object):
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
        'end': 'object',
        'properties': 'list[ScalarPropertyV1]',
        'start': 'object'
    }

    attribute_map = {
        'end': 'end',
        'properties': 'properties',
        'start': 'start'
    }

    def __init__(self, end=None, properties=None, start=None):
        """
        CapsuleInputV1 - a model defined in Swagger
        """

        self._end = None
        self._properties = None
        self._start = None

        if end is not None:
          self.end = end
        if properties is not None:
          self.properties = properties
        if start is not None:
          self.start = start

    @property
    def end(self):
        """
        Gets the end of this CapsuleInputV1.
        The end of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds).

        :return: The end of this CapsuleInputV1.
        :rtype: object
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this CapsuleInputV1.
        The end of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds).

        :param end: The end of this CapsuleInputV1.
        :type: object
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")

        self._end = end

    @property
    def properties(self):
        """
        Gets the properties of this CapsuleInputV1.
        A list of the capsule's properties

        :return: The properties of this CapsuleInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CapsuleInputV1.
        A list of the capsule's properties

        :param properties: The properties of this CapsuleInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def start(self):
        """
        Gets the start of this CapsuleInputV1.
        The start of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds).

        :return: The start of this CapsuleInputV1.
        :rtype: object
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this CapsuleInputV1.
        The start of the capsule. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds).

        :param start: The start of this CapsuleInputV1.
        :type: object
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")

        self._start = start

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
        if not isinstance(other, CapsuleInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
