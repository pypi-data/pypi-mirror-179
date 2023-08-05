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


class WorkbenchSearchResultPreviewV1(object):
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
        'ancestors': 'list[ItemPreviewV1]',
        'created_at': 'str',
        'creator': 'IdentityPreviewV1',
        'data': 'str',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'headline': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_corporate': 'bool',
        'is_pinned': 'bool',
        'is_unmodifiable': 'bool',
        'name': 'str',
        'owner': 'IdentityPreviewV1',
        'parent_folder_id': 'str',
        'renderer': 'IdentityPreviewV1',
        'shared_at': 'str',
        'type': 'str',
        'updated_at': 'str',
        'workbook_id': 'str',
        'worksheet_id': 'str'
    }

    attribute_map = {
        'ancestors': 'ancestors',
        'created_at': 'createdAt',
        'creator': 'creator',
        'data': 'data',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'headline': 'headline',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_corporate': 'isCorporate',
        'is_pinned': 'isPinned',
        'is_unmodifiable': 'isUnmodifiable',
        'name': 'name',
        'owner': 'owner',
        'parent_folder_id': 'parentFolderId',
        'renderer': 'renderer',
        'shared_at': 'sharedAt',
        'type': 'type',
        'updated_at': 'updatedAt',
        'workbook_id': 'workbookId',
        'worksheet_id': 'worksheetId'
    }

    def __init__(self, ancestors=None, created_at=None, creator=None, data=None, description=None, effective_permissions=None, headline=None, id=None, is_archived=False, is_corporate=False, is_pinned=False, is_unmodifiable=False, name=None, owner=None, parent_folder_id=None, renderer=None, shared_at=None, type=None, updated_at=None, workbook_id=None, worksheet_id=None):
        """
        WorkbenchSearchResultPreviewV1 - a model defined in Swagger
        """

        self._ancestors = None
        self._created_at = None
        self._creator = None
        self._data = None
        self._description = None
        self._effective_permissions = None
        self._headline = None
        self._id = None
        self._is_archived = None
        self._is_corporate = None
        self._is_pinned = None
        self._is_unmodifiable = None
        self._name = None
        self._owner = None
        self._parent_folder_id = None
        self._renderer = None
        self._shared_at = None
        self._type = None
        self._updated_at = None
        self._workbook_id = None
        self._worksheet_id = None

        if ancestors is not None:
          self.ancestors = ancestors
        if created_at is not None:
          self.created_at = created_at
        if creator is not None:
          self.creator = creator
        if data is not None:
          self.data = data
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if headline is not None:
          self.headline = headline
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_corporate is not None:
          self.is_corporate = is_corporate
        if is_pinned is not None:
          self.is_pinned = is_pinned
        if is_unmodifiable is not None:
          self.is_unmodifiable = is_unmodifiable
        if name is not None:
          self.name = name
        if owner is not None:
          self.owner = owner
        if parent_folder_id is not None:
          self.parent_folder_id = parent_folder_id
        if renderer is not None:
          self.renderer = renderer
        if shared_at is not None:
          self.shared_at = shared_at
        if type is not None:
          self.type = type
        if updated_at is not None:
          self.updated_at = updated_at
        if workbook_id is not None:
          self.workbook_id = workbook_id
        if worksheet_id is not None:
          self.worksheet_id = worksheet_id

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkbenchSearchResultPreviewV1.
        The list of the item's folder ancestors, starting at the topmost folder to which the user has access

        :return: The ancestors of this WorkbenchSearchResultPreviewV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkbenchSearchResultPreviewV1.
        The list of the item's folder ancestors, starting at the topmost folder to which the user has access

        :param ancestors: The ancestors of this WorkbenchSearchResultPreviewV1.
        :type: list[ItemPreviewV1]
        """

        self._ancestors = ancestors

    @property
    def created_at(self):
        """
        Gets the created_at of this WorkbenchSearchResultPreviewV1.
        The ISO 8601 date of when the item was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The created_at of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this WorkbenchSearchResultPreviewV1.
        The ISO 8601 date of when the item was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param created_at: The created_at of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def creator(self):
        """
        Gets the creator of this WorkbenchSearchResultPreviewV1.

        :return: The creator of this WorkbenchSearchResultPreviewV1.
        :rtype: IdentityPreviewV1
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this WorkbenchSearchResultPreviewV1.

        :param creator: The creator of this WorkbenchSearchResultPreviewV1.
        :type: IdentityPreviewV1
        """

        self._creator = creator

    @property
    def data(self):
        """
        Gets the data of this WorkbenchSearchResultPreviewV1.
        Additional data about the item, provided as JSON

        :return: The data of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this WorkbenchSearchResultPreviewV1.
        Additional data about the item, provided as JSON

        :param data: The data of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._data = data

    @property
    def description(self):
        """
        Gets the description of this WorkbenchSearchResultPreviewV1.
        The item's description

        :return: The description of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkbenchSearchResultPreviewV1.
        The item's description

        :param description: The description of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this WorkbenchSearchResultPreviewV1.

        :return: The effective_permissions of this WorkbenchSearchResultPreviewV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this WorkbenchSearchResultPreviewV1.

        :param effective_permissions: The effective_permissions of this WorkbenchSearchResultPreviewV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def headline(self):
        """
        Gets the headline of this WorkbenchSearchResultPreviewV1.
        An indication of what text within this item matched a text search

        :return: The headline of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this WorkbenchSearchResultPreviewV1.
        An indication of what text within this item matched a text search

        :param headline: The headline of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._headline = headline

    @property
    def id(self):
        """
        Gets the id of this WorkbenchSearchResultPreviewV1.
        The ID that can be used to interact with the item

        :return: The id of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkbenchSearchResultPreviewV1.
        The ID that can be used to interact with the item

        :param id: The id of this WorkbenchSearchResultPreviewV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this WorkbenchSearchResultPreviewV1.
        Whether item is archived

        :return: The is_archived of this WorkbenchSearchResultPreviewV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this WorkbenchSearchResultPreviewV1.
        Whether item is archived

        :param is_archived: The is_archived of this WorkbenchSearchResultPreviewV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_corporate(self):
        """
        Gets the is_corporate of this WorkbenchSearchResultPreviewV1.
        Whether the item is under the corporate folder

        :return: The is_corporate of this WorkbenchSearchResultPreviewV1.
        :rtype: bool
        """
        return self._is_corporate

    @is_corporate.setter
    def is_corporate(self, is_corporate):
        """
        Sets the is_corporate of this WorkbenchSearchResultPreviewV1.
        Whether the item is under the corporate folder

        :param is_corporate: The is_corporate of this WorkbenchSearchResultPreviewV1.
        :type: bool
        """

        self._is_corporate = is_corporate

    @property
    def is_pinned(self):
        """
        Gets the is_pinned of this WorkbenchSearchResultPreviewV1.
        Flag indicating whether this item has been marked as a favorite by the current user

        :return: The is_pinned of this WorkbenchSearchResultPreviewV1.
        :rtype: bool
        """
        return self._is_pinned

    @is_pinned.setter
    def is_pinned(self, is_pinned):
        """
        Sets the is_pinned of this WorkbenchSearchResultPreviewV1.
        Flag indicating whether this item has been marked as a favorite by the current user

        :param is_pinned: The is_pinned of this WorkbenchSearchResultPreviewV1.
        :type: bool
        """

        self._is_pinned = is_pinned

    @property
    def is_unmodifiable(self):
        """
        Gets the is_unmodifiable of this WorkbenchSearchResultPreviewV1.
        Whether the item is unmodifiable

        :return: The is_unmodifiable of this WorkbenchSearchResultPreviewV1.
        :rtype: bool
        """
        return self._is_unmodifiable

    @is_unmodifiable.setter
    def is_unmodifiable(self, is_unmodifiable):
        """
        Sets the is_unmodifiable of this WorkbenchSearchResultPreviewV1.
        Whether the item is unmodifiable

        :param is_unmodifiable: The is_unmodifiable of this WorkbenchSearchResultPreviewV1.
        :type: bool
        """

        self._is_unmodifiable = is_unmodifiable

    @property
    def name(self):
        """
        Gets the name of this WorkbenchSearchResultPreviewV1.
        The name of the item

        :return: The name of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkbenchSearchResultPreviewV1.
        The name of the item

        :param name: The name of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """
        Gets the owner of this WorkbenchSearchResultPreviewV1.

        :return: The owner of this WorkbenchSearchResultPreviewV1.
        :rtype: IdentityPreviewV1
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this WorkbenchSearchResultPreviewV1.

        :param owner: The owner of this WorkbenchSearchResultPreviewV1.
        :type: IdentityPreviewV1
        """

        self._owner = owner

    @property
    def parent_folder_id(self):
        """
        Gets the parent_folder_id of this WorkbenchSearchResultPreviewV1.
        The ID of the folder this item belongs to

        :return: The parent_folder_id of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """
        Sets the parent_folder_id of this WorkbenchSearchResultPreviewV1.
        The ID of the folder this item belongs to

        :param parent_folder_id: The parent_folder_id of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def renderer(self):
        """
        Gets the renderer of this WorkbenchSearchResultPreviewV1.

        :return: The renderer of this WorkbenchSearchResultPreviewV1.
        :rtype: IdentityPreviewV1
        """
        return self._renderer

    @renderer.setter
    def renderer(self, renderer):
        """
        Sets the renderer of this WorkbenchSearchResultPreviewV1.

        :param renderer: The renderer of this WorkbenchSearchResultPreviewV1.
        :type: IdentityPreviewV1
        """

        self._renderer = renderer

    @property
    def shared_at(self):
        """
        Gets the shared_at of this WorkbenchSearchResultPreviewV1.
        The datetime when the item was shared with the current user

        :return: The shared_at of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._shared_at

    @shared_at.setter
    def shared_at(self, shared_at):
        """
        Sets the shared_at of this WorkbenchSearchResultPreviewV1.
        The datetime when the item was shared with the current user

        :param shared_at: The shared_at of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._shared_at = shared_at

    @property
    def type(self):
        """
        Gets the type of this WorkbenchSearchResultPreviewV1.
        The type of the item

        :return: The type of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkbenchSearchResultPreviewV1.
        The type of the item

        :param type: The type of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this WorkbenchSearchResultPreviewV1.
        The ISO 8601 date of when the item was last updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The updated_at of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this WorkbenchSearchResultPreviewV1.
        The ISO 8601 date of when the item was last updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param updated_at: The updated_at of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def workbook_id(self):
        """
        Gets the workbook_id of this WorkbenchSearchResultPreviewV1.
        Id of containing workbook if item is a journal or report

        :return: The workbook_id of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._workbook_id

    @workbook_id.setter
    def workbook_id(self, workbook_id):
        """
        Sets the workbook_id of this WorkbenchSearchResultPreviewV1.
        Id of containing workbook if item is a journal or report

        :param workbook_id: The workbook_id of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._workbook_id = workbook_id

    @property
    def worksheet_id(self):
        """
        Gets the worksheet_id of this WorkbenchSearchResultPreviewV1.
        Id of containing worksheet if item is a journal or report

        :return: The worksheet_id of this WorkbenchSearchResultPreviewV1.
        :rtype: str
        """
        return self._worksheet_id

    @worksheet_id.setter
    def worksheet_id(self, worksheet_id):
        """
        Sets the worksheet_id of this WorkbenchSearchResultPreviewV1.
        Id of containing worksheet if item is a journal or report

        :param worksheet_id: The worksheet_id of this WorkbenchSearchResultPreviewV1.
        :type: str
        """

        self._worksheet_id = worksheet_id

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
        if not isinstance(other, WorkbenchSearchResultPreviewV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
