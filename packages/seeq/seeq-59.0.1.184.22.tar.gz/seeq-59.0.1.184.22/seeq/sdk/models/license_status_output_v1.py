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


class LicenseStatusOutputV1(object):
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
        'additional_features': 'list[LicensedFeatureStatusOutputV1]',
        'company_name': 'str',
        'contract_number': 'str',
        'days_to_expiration': 'int',
        'hostname': 'str',
        'level': 'str',
        'user_count': 'int',
        'user_limit_restrict': 'int',
        'user_limit_warn': 'int',
        'valid_through': 'str',
        'validity': 'str'
    }

    attribute_map = {
        'additional_features': 'additionalFeatures',
        'company_name': 'companyName',
        'contract_number': 'contractNumber',
        'days_to_expiration': 'daysToExpiration',
        'hostname': 'hostname',
        'level': 'level',
        'user_count': 'userCount',
        'user_limit_restrict': 'userLimitRestrict',
        'user_limit_warn': 'userLimitWarn',
        'valid_through': 'validThrough',
        'validity': 'validity'
    }

    def __init__(self, additional_features=None, company_name=None, contract_number=None, days_to_expiration=None, hostname=None, level=None, user_count=None, user_limit_restrict=None, user_limit_warn=None, valid_through=None, validity=None):
        """
        LicenseStatusOutputV1 - a model defined in Swagger
        """

        self._additional_features = None
        self._company_name = None
        self._contract_number = None
        self._days_to_expiration = None
        self._hostname = None
        self._level = None
        self._user_count = None
        self._user_limit_restrict = None
        self._user_limit_warn = None
        self._valid_through = None
        self._validity = None

        if additional_features is not None:
          self.additional_features = additional_features
        if company_name is not None:
          self.company_name = company_name
        if contract_number is not None:
          self.contract_number = contract_number
        if days_to_expiration is not None:
          self.days_to_expiration = days_to_expiration
        if hostname is not None:
          self.hostname = hostname
        if level is not None:
          self.level = level
        if user_count is not None:
          self.user_count = user_count
        if user_limit_restrict is not None:
          self.user_limit_restrict = user_limit_restrict
        if user_limit_warn is not None:
          self.user_limit_warn = user_limit_warn
        if valid_through is not None:
          self.valid_through = valid_through
        if validity is not None:
          self.validity = validity

    @property
    def additional_features(self):
        """
        Gets the additional_features of this LicenseStatusOutputV1.
        Additionally licensed features

        :return: The additional_features of this LicenseStatusOutputV1.
        :rtype: list[LicensedFeatureStatusOutputV1]
        """
        return self._additional_features

    @additional_features.setter
    def additional_features(self, additional_features):
        """
        Sets the additional_features of this LicenseStatusOutputV1.
        Additionally licensed features

        :param additional_features: The additional_features of this LicenseStatusOutputV1.
        :type: list[LicensedFeatureStatusOutputV1]
        """

        self._additional_features = additional_features

    @property
    def company_name(self):
        """
        Gets the company_name of this LicenseStatusOutputV1.
        The company/organization name associated with this license

        :return: The company_name of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this LicenseStatusOutputV1.
        The company/organization name associated with this license

        :param company_name: The company_name of this LicenseStatusOutputV1.
        :type: str
        """

        self._company_name = company_name

    @property
    def contract_number(self):
        """
        Gets the contract_number of this LicenseStatusOutputV1.
        The Seeq Contract Number associated with this license.

        :return: The contract_number of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """
        Sets the contract_number of this LicenseStatusOutputV1.
        The Seeq Contract Number associated with this license.

        :param contract_number: The contract_number of this LicenseStatusOutputV1.
        :type: str
        """

        self._contract_number = contract_number

    @property
    def days_to_expiration(self):
        """
        Gets the days_to_expiration of this LicenseStatusOutputV1.
        The number of days left before the current license will expire

        :return: The days_to_expiration of this LicenseStatusOutputV1.
        :rtype: int
        """
        return self._days_to_expiration

    @days_to_expiration.setter
    def days_to_expiration(self, days_to_expiration):
        """
        Sets the days_to_expiration of this LicenseStatusOutputV1.
        The number of days left before the current license will expire

        :param days_to_expiration: The days_to_expiration of this LicenseStatusOutputV1.
        :type: int
        """

        self._days_to_expiration = days_to_expiration

    @property
    def hostname(self):
        """
        Gets the hostname of this LicenseStatusOutputV1.
        The server hostname that is licensed

        :return: The hostname of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this LicenseStatusOutputV1.
        The server hostname that is licensed

        :param hostname: The hostname of this LicenseStatusOutputV1.
        :type: str
        """

        self._hostname = hostname

    @property
    def level(self):
        """
        Gets the level of this LicenseStatusOutputV1.
        The level of the license installed on this server. Possibilities: 'Trial', 'Standard'

        :return: The level of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this LicenseStatusOutputV1.
        The level of the license installed on this server. Possibilities: 'Trial', 'Standard'

        :param level: The level of this LicenseStatusOutputV1.
        :type: str
        """

        self._level = level

    @property
    def user_count(self):
        """
        Gets the user_count of this LicenseStatusOutputV1.
        The number of Seeq users

        :return: The user_count of this LicenseStatusOutputV1.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this LicenseStatusOutputV1.
        The number of Seeq users

        :param user_count: The user_count of this LicenseStatusOutputV1.
        :type: int
        """

        self._user_count = user_count

    @property
    def user_limit_restrict(self):
        """
        Gets the user_limit_restrict of this LicenseStatusOutputV1.
        The number of users at which to restrict creating new user accounts

        :return: The user_limit_restrict of this LicenseStatusOutputV1.
        :rtype: int
        """
        return self._user_limit_restrict

    @user_limit_restrict.setter
    def user_limit_restrict(self, user_limit_restrict):
        """
        Sets the user_limit_restrict of this LicenseStatusOutputV1.
        The number of users at which to restrict creating new user accounts

        :param user_limit_restrict: The user_limit_restrict of this LicenseStatusOutputV1.
        :type: int
        """

        self._user_limit_restrict = user_limit_restrict

    @property
    def user_limit_warn(self):
        """
        Gets the user_limit_warn of this LicenseStatusOutputV1.
        The number of users at which to warn about running out of available user accounts

        :return: The user_limit_warn of this LicenseStatusOutputV1.
        :rtype: int
        """
        return self._user_limit_warn

    @user_limit_warn.setter
    def user_limit_warn(self, user_limit_warn):
        """
        Sets the user_limit_warn of this LicenseStatusOutputV1.
        The number of users at which to warn about running out of available user accounts

        :param user_limit_warn: The user_limit_warn of this LicenseStatusOutputV1.
        :type: int
        """

        self._user_limit_warn = user_limit_warn

    @property
    def valid_through(self):
        """
        Gets the valid_through of this LicenseStatusOutputV1.
        The final day this license will be valid for

        :return: The valid_through of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._valid_through

    @valid_through.setter
    def valid_through(self, valid_through):
        """
        Sets the valid_through of this LicenseStatusOutputV1.
        The final day this license will be valid for

        :param valid_through: The valid_through of this LicenseStatusOutputV1.
        :type: str
        """

        self._valid_through = valid_through

    @property
    def validity(self):
        """
        Gets the validity of this LicenseStatusOutputV1.
        The validity of the license

        :return: The validity of this LicenseStatusOutputV1.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this LicenseStatusOutputV1.
        The validity of the license

        :param validity: The validity of this LicenseStatusOutputV1.
        :type: str
        """
        allowed_values = ["UnknownError", "Valid", "NoLicense", "Expired", "WrongHost", "BadSignature", "ClockTampering", "OverLimit"]
        if validity not in allowed_values:
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"
                .format(validity, allowed_values)
            )

        self._validity = validity

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
        if not isinstance(other, LicenseStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
