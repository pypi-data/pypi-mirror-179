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


class SamplesOverwriteInputV1(object):
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
        'interval': 'IntervalV1',
        'samples': 'list[SampleInputV1]'
    }

    attribute_map = {
        'interval': 'interval',
        'samples': 'samples'
    }

    def __init__(self, interval=None, samples=None):
        """
        SamplesOverwriteInputV1 - a model defined in Swagger
        """

        self._interval = None
        self._samples = None

        if interval is not None:
          self.interval = interval
        if samples is not None:
          self.samples = samples

    @property
    def interval(self):
        """
        Gets the interval of this SamplesOverwriteInputV1.

        :return: The interval of this SamplesOverwriteInputV1.
        :rtype: IntervalV1
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this SamplesOverwriteInputV1.

        :param interval: The interval of this SamplesOverwriteInputV1.
        :type: IntervalV1
        """

        self._interval = interval

    @property
    def samples(self):
        """
        Gets the samples of this SamplesOverwriteInputV1.
        The samples in the signal

        :return: The samples of this SamplesOverwriteInputV1.
        :rtype: list[SampleInputV1]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """
        Sets the samples of this SamplesOverwriteInputV1.
        The samples in the signal

        :param samples: The samples of this SamplesOverwriteInputV1.
        :type: list[SampleInputV1]
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")

        self._samples = samples

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
        if not isinstance(other, SamplesOverwriteInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
