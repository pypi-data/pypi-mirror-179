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


class FormulaDocKeywordListInputV1(object):
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
        'keywords': 'list[str]'
    }

    attribute_map = {
        'keywords': 'keywords'
    }

    def __init__(self, keywords=None):
        """
        FormulaDocKeywordListInputV1 - a model defined in Swagger
        """

        self._keywords = None

        if keywords is not None:
          self.keywords = keywords

    @property
    def keywords(self):
        """
        Gets the keywords of this FormulaDocKeywordListInputV1.
        The list of search keywords for a documentation page in Seeq Formula.

        :return: The keywords of this FormulaDocKeywordListInputV1.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this FormulaDocKeywordListInputV1.
        The list of search keywords for a documentation page in Seeq Formula.

        :param keywords: The keywords of this FormulaDocKeywordListInputV1.
        :type: list[str]
        """
        if keywords is None:
            raise ValueError("Invalid value for `keywords`, must not be `None`")

        self._keywords = keywords

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
        if not isinstance(other, FormulaDocKeywordListInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
