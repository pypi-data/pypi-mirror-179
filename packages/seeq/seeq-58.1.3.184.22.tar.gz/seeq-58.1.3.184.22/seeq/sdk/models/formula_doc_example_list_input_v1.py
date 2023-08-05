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


class FormulaDocExampleListInputV1(object):
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
        'examples': 'list[FormulaDocExampleInputV1]'
    }

    attribute_map = {
        'examples': 'examples'
    }

    def __init__(self, examples=None):
        """
        FormulaDocExampleListInputV1 - a model defined in Swagger
        """

        self._examples = None

        if examples is not None:
          self.examples = examples

    @property
    def examples(self):
        """
        Gets the examples of this FormulaDocExampleListInputV1.
        The list of examples for a documentation page in Seeq Formula.

        :return: The examples of this FormulaDocExampleListInputV1.
        :rtype: list[FormulaDocExampleInputV1]
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """
        Sets the examples of this FormulaDocExampleListInputV1.
        The list of examples for a documentation page in Seeq Formula.

        :param examples: The examples of this FormulaDocExampleListInputV1.
        :type: list[FormulaDocExampleInputV1]
        """
        if examples is None:
            raise ValueError("Invalid value for `examples`, must not be `None`")

        self._examples = examples

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
        if not isinstance(other, FormulaDocExampleListInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
