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


class ValidateCronOutputV1(object):
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
        'error': 'str',
        'next_run_time': 'str',
        'quartz_cron_expression': 'str',
        'quartz_cron_expression_summary': 'str',
        'valid': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'next_run_time': 'nextRunTime',
        'quartz_cron_expression': 'quartzCronExpression',
        'quartz_cron_expression_summary': 'quartzCronExpressionSummary',
        'valid': 'valid'
    }

    def __init__(self, error=None, next_run_time=None, quartz_cron_expression=None, quartz_cron_expression_summary=None, valid=False):
        """
        ValidateCronOutputV1 - a model defined in Swagger
        """

        self._error = None
        self._next_run_time = None
        self._quartz_cron_expression = None
        self._quartz_cron_expression_summary = None
        self._valid = None

        if error is not None:
          self.error = error
        if next_run_time is not None:
          self.next_run_time = next_run_time
        if quartz_cron_expression is not None:
          self.quartz_cron_expression = quartz_cron_expression
        if quartz_cron_expression_summary is not None:
          self.quartz_cron_expression_summary = quartz_cron_expression_summary
        if valid is not None:
          self.valid = valid

    @property
    def error(self):
        """
        Gets the error of this ValidateCronOutputV1.
        The error message if the Quartz cron expression is not valid

        :return: The error of this ValidateCronOutputV1.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ValidateCronOutputV1.
        The error message if the Quartz cron expression is not valid

        :param error: The error of this ValidateCronOutputV1.
        :type: str
        """

        self._error = error

    @property
    def next_run_time(self):
        """
        Gets the next_run_time of this ValidateCronOutputV1.
        The next time after the the input nextValidTimeAfter in which the schedule will trigger

        :return: The next_run_time of this ValidateCronOutputV1.
        :rtype: str
        """
        return self._next_run_time

    @next_run_time.setter
    def next_run_time(self, next_run_time):
        """
        Sets the next_run_time of this ValidateCronOutputV1.
        The next time after the the input nextValidTimeAfter in which the schedule will trigger

        :param next_run_time: The next_run_time of this ValidateCronOutputV1.
        :type: str
        """

        self._next_run_time = next_run_time

    @property
    def quartz_cron_expression(self):
        """
        Gets the quartz_cron_expression of this ValidateCronOutputV1.
        The input Quartz cron expression

        :return: The quartz_cron_expression of this ValidateCronOutputV1.
        :rtype: str
        """
        return self._quartz_cron_expression

    @quartz_cron_expression.setter
    def quartz_cron_expression(self, quartz_cron_expression):
        """
        Sets the quartz_cron_expression of this ValidateCronOutputV1.
        The input Quartz cron expression

        :param quartz_cron_expression: The quartz_cron_expression of this ValidateCronOutputV1.
        :type: str
        """

        self._quartz_cron_expression = quartz_cron_expression

    @property
    def quartz_cron_expression_summary(self):
        """
        Gets the quartz_cron_expression_summary of this ValidateCronOutputV1.
        The full summary of the cron expression

        :return: The quartz_cron_expression_summary of this ValidateCronOutputV1.
        :rtype: str
        """
        return self._quartz_cron_expression_summary

    @quartz_cron_expression_summary.setter
    def quartz_cron_expression_summary(self, quartz_cron_expression_summary):
        """
        Sets the quartz_cron_expression_summary of this ValidateCronOutputV1.
        The full summary of the cron expression

        :param quartz_cron_expression_summary: The quartz_cron_expression_summary of this ValidateCronOutputV1.
        :type: str
        """

        self._quartz_cron_expression_summary = quartz_cron_expression_summary

    @property
    def valid(self):
        """
        Gets the valid of this ValidateCronOutputV1.
        True if the Quartz cron expression was parsed and there's a valid nextRunTime

        :return: The valid of this ValidateCronOutputV1.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this ValidateCronOutputV1.
        True if the Quartz cron expression was parsed and there's a valid nextRunTime

        :param valid: The valid of this ValidateCronOutputV1.
        :type: bool
        """

        self._valid = valid

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
        if not isinstance(other, ValidateCronOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
