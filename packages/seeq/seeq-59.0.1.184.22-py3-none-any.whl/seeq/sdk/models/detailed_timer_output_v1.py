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


class DetailedTimerOutputV1(object):
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
        'count': 'int',
        'description': 'str',
        'path': 'str',
        'seconds': 'float'
    }

    attribute_map = {
        'count': 'count',
        'description': 'description',
        'path': 'path',
        'seconds': 'seconds'
    }

    def __init__(self, count=None, description=None, path=None, seconds=None):
        """
        DetailedTimerOutputV1 - a model defined in Swagger
        """

        self._count = None
        self._description = None
        self._path = None
        self._seconds = None

        if count is not None:
          self.count = count
        if description is not None:
          self.description = description
        if path is not None:
          self.path = path
        if seconds is not None:
          self.seconds = seconds

    @property
    def count(self):
        """
        Gets the count of this DetailedTimerOutputV1.
        Number of occurrences of a timed event. The value may increase if the timed event is still in progress.

        :return: The count of this DetailedTimerOutputV1.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DetailedTimerOutputV1.
        Number of occurrences of a timed event. The value may increase if the timed event is still in progress.

        :param count: The count of this DetailedTimerOutputV1.
        :type: int
        """

        self._count = count

    @property
    def description(self):
        """
        Gets the description of this DetailedTimerOutputV1.
        Human readable description of the facet of the system being monitored.

        :return: The description of this DetailedTimerOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DetailedTimerOutputV1.
        Human readable description of the facet of the system being monitored.

        :param description: The description of this DetailedTimerOutputV1.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this DetailedTimerOutputV1.
        Unique ID for the monitored value.

        :return: The path of this DetailedTimerOutputV1.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this DetailedTimerOutputV1.
        Unique ID for the monitored value.

        :param path: The path of this DetailedTimerOutputV1.
        :type: str
        """

        self._path = path

    @property
    def seconds(self):
        """
        Gets the seconds of this DetailedTimerOutputV1.
        Total duration, in seconds, for all occurrences of a timed event. The value may increase if the timed event is still in progress.

        :return: The seconds of this DetailedTimerOutputV1.
        :rtype: float
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """
        Sets the seconds of this DetailedTimerOutputV1.
        Total duration, in seconds, for all occurrences of a timed event. The value may increase if the timed event is still in progress.

        :param seconds: The seconds of this DetailedTimerOutputV1.
        :type: float
        """

        self._seconds = seconds

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
        if not isinstance(other, DetailedTimerOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
