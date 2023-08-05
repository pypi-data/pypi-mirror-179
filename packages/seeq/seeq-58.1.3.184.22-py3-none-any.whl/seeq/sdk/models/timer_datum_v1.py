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


class TimerDatumV1(object):
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
        'args': 'list[str]',
        'durations': 'list[int]',
        'monitor': 'str'
    }

    attribute_map = {
        'args': 'args',
        'durations': 'durations',
        'monitor': 'monitor'
    }

    def __init__(self, args=None, durations=None, monitor=None):
        """
        TimerDatumV1 - a model defined in Swagger
        """

        self._args = None
        self._durations = None
        self._monitor = None

        if args is not None:
          self.args = args
        if durations is not None:
          self.durations = durations
        if monitor is not None:
          self.monitor = monitor

    @property
    def args(self):
        """
        Gets the args of this TimerDatumV1.
        List of arguments to include in the monitor path

        :return: The args of this TimerDatumV1.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this TimerDatumV1.
        List of arguments to include in the monitor path

        :param args: The args of this TimerDatumV1.
        :type: list[str]
        """

        self._args = args

    @property
    def durations(self):
        """
        Gets the durations of this TimerDatumV1.
        Duration of each timed event in nanoseconds.

        :return: The durations of this TimerDatumV1.
        :rtype: list[int]
        """
        return self._durations

    @durations.setter
    def durations(self, durations):
        """
        Sets the durations of this TimerDatumV1.
        Duration of each timed event in nanoseconds.

        :param durations: The durations of this TimerDatumV1.
        :type: list[int]
        """
        if durations is None:
            raise ValueError("Invalid value for `durations`, must not be `None`")

        self._durations = durations

    @property
    def monitor(self):
        """
        Gets the monitor of this TimerDatumV1.
        Name of the monitor item this data should apply to.

        :return: The monitor of this TimerDatumV1.
        :rtype: str
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        """
        Sets the monitor of this TimerDatumV1.
        Name of the monitor item this data should apply to.

        :param monitor: The monitor of this TimerDatumV1.
        :type: str
        """
        if monitor is None:
            raise ValueError("Invalid value for `monitor`, must not be `None`")

        self._monitor = monitor

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
        if not isinstance(other, TimerDatumV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
