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


class ExportPreviewV1(object):
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
        'autoupdate_time_range': 'bool',
        'created_at': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'scoped_to': 'str',
        'translation_key': 'str',
        'type': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'autoupdate_time_range': 'autoupdateTimeRange',
        'created_at': 'createdAt',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'scoped_to': 'scopedTo',
        'translation_key': 'translationKey',
        'type': 'type',
        'updated_at': 'updatedAt'
    }

    def __init__(self, autoupdate_time_range=False, created_at=None, id=None, is_archived=False, is_redacted=False, name=None, scoped_to=None, translation_key=None, type=None, updated_at=None):
        """
        ExportPreviewV1 - a model defined in Swagger
        """

        self._autoupdate_time_range = None
        self._created_at = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._scoped_to = None
        self._translation_key = None
        self._type = None
        self._updated_at = None

        if autoupdate_time_range is not None:
          self.autoupdate_time_range = autoupdate_time_range
        if created_at is not None:
          self.created_at = created_at
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def autoupdate_time_range(self):
        """
        Gets the autoupdate_time_range of this ExportPreviewV1.
        Boolean indicating if the time range for export will be updated to 'now' when the export is started.

        :return: The autoupdate_time_range of this ExportPreviewV1.
        :rtype: bool
        """
        return self._autoupdate_time_range

    @autoupdate_time_range.setter
    def autoupdate_time_range(self, autoupdate_time_range):
        """
        Sets the autoupdate_time_range of this ExportPreviewV1.
        Boolean indicating if the time range for export will be updated to 'now' when the export is started.

        :param autoupdate_time_range: The autoupdate_time_range of this ExportPreviewV1.
        :type: bool
        """

        self._autoupdate_time_range = autoupdate_time_range

    @property
    def created_at(self):
        """
        Gets the created_at of this ExportPreviewV1.
        The ISO 8601 date of when the export was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The created_at of this ExportPreviewV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ExportPreviewV1.
        The ISO 8601 date of when the export was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param created_at: The created_at of this ExportPreviewV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """
        Gets the id of this ExportPreviewV1.
        The ID that can be used to interact with the item

        :return: The id of this ExportPreviewV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExportPreviewV1.
        The ID that can be used to interact with the item

        :param id: The id of this ExportPreviewV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ExportPreviewV1.
        Whether item is archived

        :return: The is_archived of this ExportPreviewV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ExportPreviewV1.
        Whether item is archived

        :param is_archived: The is_archived of this ExportPreviewV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this ExportPreviewV1.
        Whether item is redacted

        :return: The is_redacted of this ExportPreviewV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this ExportPreviewV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this ExportPreviewV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this ExportPreviewV1.
        The human readable name

        :return: The name of this ExportPreviewV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExportPreviewV1.
        The human readable name

        :param name: The name of this ExportPreviewV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ExportPreviewV1.
        The ID of the workbook to which this item is scoped. If null, the export is globally-scoped.

        :return: The scoped_to of this ExportPreviewV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ExportPreviewV1.
        The ID of the workbook to which this item is scoped. If null, the export is globally-scoped.

        :param scoped_to: The scoped_to of this ExportPreviewV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def translation_key(self):
        """
        Gets the translation_key of this ExportPreviewV1.
        The item's translation key, if any

        :return: The translation_key of this ExportPreviewV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this ExportPreviewV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this ExportPreviewV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this ExportPreviewV1.
        The type of the item

        :return: The type of this ExportPreviewV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExportPreviewV1.
        The type of the item

        :param type: The type of this ExportPreviewV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ExportPreviewV1.
        The ISO 8601 date of when the export was updated/run (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The updated_at of this ExportPreviewV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ExportPreviewV1.
        The ISO 8601 date of when the export was updated/run (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param updated_at: The updated_at of this ExportPreviewV1.
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, ExportPreviewV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
