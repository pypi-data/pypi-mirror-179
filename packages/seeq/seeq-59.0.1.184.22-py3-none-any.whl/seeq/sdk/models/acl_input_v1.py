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


class AclInputV1(object):
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
        'disable_permission_inheritance': 'bool',
        'entries': 'list[AceInputV1]',
        'localize_inherited': 'bool',
        'preview': 'bool'
    }

    attribute_map = {
        'disable_permission_inheritance': 'disablePermissionInheritance',
        'entries': 'entries',
        'localize_inherited': 'localizeInherited',
        'preview': 'preview'
    }

    def __init__(self, disable_permission_inheritance=False, entries=None, localize_inherited=False, preview=False):
        """
        AclInputV1 - a model defined in Swagger
        """

        self._disable_permission_inheritance = None
        self._entries = None
        self._localize_inherited = None
        self._preview = None

        if disable_permission_inheritance is not None:
          self.disable_permission_inheritance = disable_permission_inheritance
        if entries is not None:
          self.entries = entries
        if localize_inherited is not None:
          self.localize_inherited = localize_inherited
        if preview is not None:
          self.preview = preview

    @property
    def disable_permission_inheritance(self):
        """
        Gets the disable_permission_inheritance of this AclInputV1.
        Whether permission inheritance for the item should be disabled (default is false)

        :return: The disable_permission_inheritance of this AclInputV1.
        :rtype: bool
        """
        return self._disable_permission_inheritance

    @disable_permission_inheritance.setter
    def disable_permission_inheritance(self, disable_permission_inheritance):
        """
        Sets the disable_permission_inheritance of this AclInputV1.
        Whether permission inheritance for the item should be disabled (default is false)

        :param disable_permission_inheritance: The disable_permission_inheritance of this AclInputV1.
        :type: bool
        """

        self._disable_permission_inheritance = disable_permission_inheritance

    @property
    def entries(self):
        """
        Gets the entries of this AclInputV1.
        List of access control entries to set. Entries will be flattened to a minimal set of entries

        :return: The entries of this AclInputV1.
        :rtype: list[AceInputV1]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this AclInputV1.
        List of access control entries to set. Entries will be flattened to a minimal set of entries

        :param entries: The entries of this AclInputV1.
        :type: list[AceInputV1]
        """

        self._entries = entries

    @property
    def localize_inherited(self):
        """
        Gets the localize_inherited of this AclInputV1.
        If true, any existing inherited access control entries should be merged into the supplied ACL (default is true). This enables changing permission inheritance without changing the access to the item (default is true).

        :return: The localize_inherited of this AclInputV1.
        :rtype: bool
        """
        return self._localize_inherited

    @localize_inherited.setter
    def localize_inherited(self, localize_inherited):
        """
        Sets the localize_inherited of this AclInputV1.
        If true, any existing inherited access control entries should be merged into the supplied ACL (default is true). This enables changing permission inheritance without changing the access to the item (default is true).

        :param localize_inherited: The localize_inherited of this AclInputV1.
        :type: bool
        """

        self._localize_inherited = localize_inherited

    @property
    def preview(self):
        """
        Gets the preview of this AclInputV1.
        If true, new acl entries will be generated and returned but those acl entries will not be persisted to the item. This is useful for previewing how an acl change will modify entries without persisting the change

        :return: The preview of this AclInputV1.
        :rtype: bool
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """
        Sets the preview of this AclInputV1.
        If true, new acl entries will be generated and returned but those acl entries will not be persisted to the item. This is useful for previewing how an acl change will modify entries without persisting the change

        :param preview: The preview of this AclInputV1.
        :type: bool
        """

        self._preview = preview

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
        if not isinstance(other, AclInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
