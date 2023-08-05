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


class ValidityRegionV1(object):
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
        'end_inclusive': 'bool',
        'start': 'object'
    }

    attribute_map = {
        'end': 'end',
        'end_inclusive': 'endInclusive',
        'start': 'start'
    }

    def __init__(self, end=None, end_inclusive=False, start=None):
        """
        ValidityRegionV1 - a model defined in Swagger
        """

        self._end = None
        self._end_inclusive = None
        self._start = None

        if end is not None:
          self.end = end
        if end_inclusive is not None:
          self.end_inclusive = end_inclusive
        if start is not None:
          self.start = start

    @property
    def end(self):
        """
        Gets the end of this ValidityRegionV1.
        The end of the region. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :return: The end of this ValidityRegionV1.
        :rtype: object
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this ValidityRegionV1.
        The end of the region. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :param end: The end of this ValidityRegionV1.
        :type: object
        """

        self._end = end

    @property
    def end_inclusive(self):
        """
        Gets the end_inclusive of this ValidityRegionV1.
        True if the region of cache validity includes the end key.

        :return: The end_inclusive of this ValidityRegionV1.
        :rtype: bool
        """
        return self._end_inclusive

    @end_inclusive.setter
    def end_inclusive(self, end_inclusive):
        """
        Sets the end_inclusive of this ValidityRegionV1.
        True if the region of cache validity includes the end key.

        :param end_inclusive: The end_inclusive of this ValidityRegionV1.
        :type: bool
        """

        self._end_inclusive = end_inclusive

    @property
    def start(self):
        """
        Gets the start of this ValidityRegionV1.
        The start of the region. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :return: The start of this ValidityRegionV1.
        :rtype: object
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this ValidityRegionV1.
        The start of the region. For a time, an ISO 8601 date string (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm), or a whole number of nanoseconds since the unix epoch (if the units are nanoseconds). For a numeric (non-time), a double-precision number.

        :param start: The start of this ValidityRegionV1.
        :type: object
        """

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
        if not isinstance(other, ValidityRegionV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
