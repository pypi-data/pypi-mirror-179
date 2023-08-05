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


class FormulaPackageInputV1(object):
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
        'creator_contact_info': 'str',
        'creator_name': 'str',
        'host_id': 'str',
        'installer': 'str',
        'name': 'str',
        'sync_token': 'str',
        'version_string': 'str'
    }

    attribute_map = {
        'creator_contact_info': 'creatorContactInfo',
        'creator_name': 'creatorName',
        'host_id': 'hostId',
        'installer': 'installer',
        'name': 'name',
        'sync_token': 'syncToken',
        'version_string': 'versionString'
    }

    def __init__(self, creator_contact_info=None, creator_name=None, host_id=None, installer=None, name=None, sync_token=None, version_string=None):
        """
        FormulaPackageInputV1 - a model defined in Swagger
        """

        self._creator_contact_info = None
        self._creator_name = None
        self._host_id = None
        self._installer = None
        self._name = None
        self._sync_token = None
        self._version_string = None

        if creator_contact_info is not None:
          self.creator_contact_info = creator_contact_info
        if creator_name is not None:
          self.creator_name = creator_name
        if host_id is not None:
          self.host_id = host_id
        if installer is not None:
          self.installer = installer
        if name is not None:
          self.name = name
        if sync_token is not None:
          self.sync_token = sync_token
        if version_string is not None:
          self.version_string = version_string

    @property
    def creator_contact_info(self):
        """
        Gets the creator_contact_info of this FormulaPackageInputV1.
        The contact information of the entity that created this FormulaPackage. If not specified, the email address of the installer will try to be used.

        :return: The creator_contact_info of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._creator_contact_info

    @creator_contact_info.setter
    def creator_contact_info(self, creator_contact_info):
        """
        Sets the creator_contact_info of this FormulaPackageInputV1.
        The contact information of the entity that created this FormulaPackage. If not specified, the email address of the installer will try to be used.

        :param creator_contact_info: The creator_contact_info of this FormulaPackageInputV1.
        :type: str
        """

        self._creator_contact_info = creator_contact_info

    @property
    def creator_name(self):
        """
        Gets the creator_name of this FormulaPackageInputV1.
        The name of the entity that created this FormulaPackage. If not specified, the name of the installer will be used.

        :return: The creator_name of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """
        Sets the creator_name of this FormulaPackageInputV1.
        The name of the entity that created this FormulaPackage. If not specified, the name of the installer will be used.

        :param creator_name: The creator_name of this FormulaPackageInputV1.
        :type: str
        """

        self._creator_name = creator_name

    @property
    def host_id(self):
        """
        Gets the host_id of this FormulaPackageInputV1.
        The Seeq identifier for a datasource.

        :return: The host_id of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this FormulaPackageInputV1.
        The Seeq identifier for a datasource.

        :param host_id: The host_id of this FormulaPackageInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def installer(self):
        """
        Gets the installer of this FormulaPackageInputV1.
        The ID of the Identity that installer this FormulaPackage. If omitted when creating a new FormulaPackage, the authenticated user is used by default. Only administrators may set this to a different Identity.

        :return: The installer of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._installer

    @installer.setter
    def installer(self, installer):
        """
        Sets the installer of this FormulaPackageInputV1.
        The ID of the Identity that installer this FormulaPackage. If omitted when creating a new FormulaPackage, the authenticated user is used by default. Only administrators may set this to a different Identity.

        :param installer: The installer of this FormulaPackageInputV1.
        :type: str
        """

        self._installer = installer

    @property
    def name(self):
        """
        Gets the name of this FormulaPackageInputV1.
        The name of this FormulaPackage.

        :return: The name of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaPackageInputV1.
        The name of this FormulaPackage.

        :param name: The name of this FormulaPackageInputV1.
        :type: str
        """

        self._name = name

    @property
    def sync_token(self):
        """
        Gets the sync_token of this FormulaPackageInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this FormulaPackageInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this FormulaPackageInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def version_string(self):
        """
        Gets the version_string of this FormulaPackageInputV1.
        The version of this FormulaPackage if such identification is useful. This value does not need to conform to any set semantics.

        :return: The version_string of this FormulaPackageInputV1.
        :rtype: str
        """
        return self._version_string

    @version_string.setter
    def version_string(self, version_string):
        """
        Sets the version_string of this FormulaPackageInputV1.
        The version of this FormulaPackage if such identification is useful. This value does not need to conform to any set semantics.

        :param version_string: The version_string of this FormulaPackageInputV1.
        :type: str
        """

        self._version_string = version_string

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
        if not isinstance(other, FormulaPackageInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
