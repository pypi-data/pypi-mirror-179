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


class ReportSummaryDayOutputV1(object):
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
        'day': 'str',
        'results': 'list[int]'
    }

    attribute_map = {
        'day': 'day',
        'results': 'results'
    }

    def __init__(self, day=None, results=None):
        """
        ReportSummaryDayOutputV1 - a model defined in Swagger
        """

        self._day = None
        self._results = None

        if day is not None:
          self.day = day
        if results is not None:
          self.results = results

    @property
    def day(self):
        """
        Gets the day of this ReportSummaryDayOutputV1.
        The day that the results are for

        :return: The day of this ReportSummaryDayOutputV1.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """
        Sets the day of this ReportSummaryDayOutputV1.
        The day that the results are for

        :param day: The day of this ReportSummaryDayOutputV1.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if day not in allowed_values:
            raise ValueError(
                "Invalid value for `day` ({0}), must be one of {1}"
                .format(day, allowed_values)
            )

        self._day = day

    @property
    def results(self):
        """
        Gets the results of this ReportSummaryDayOutputV1.
        The summarized values for the given day

        :return: The results of this ReportSummaryDayOutputV1.
        :rtype: list[int]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ReportSummaryDayOutputV1.
        The summarized values for the given day

        :param results: The results of this ReportSummaryDayOutputV1.
        :type: list[int]
        """

        self._results = results

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
        if not isinstance(other, ReportSummaryDayOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
