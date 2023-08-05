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


class DatasourcePreviewV1(object):
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
        'datasource_class': 'str',
        'datasource_id': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, datasource_class=None, datasource_id=None, id=None, is_archived=False, is_redacted=False, name=None, translation_key=None, type=None):
        """
        DatasourcePreviewV1 - a model defined in Swagger
        """

        self._datasource_class = None
        self._datasource_id = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._translation_key = None
        self._type = None

        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this DatasourcePreviewV1.
        The class of the datasource

        :return: The datasource_class of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this DatasourcePreviewV1.
        The class of the datasource

        :param datasource_class: The datasource_class of this DatasourcePreviewV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this DatasourcePreviewV1.
        The ID of the datasource

        :return: The datasource_id of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this DatasourcePreviewV1.
        The ID of the datasource

        :param datasource_id: The datasource_id of this DatasourcePreviewV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def id(self):
        """
        Gets the id of this DatasourcePreviewV1.
        The ID that can be used to interact with the item

        :return: The id of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatasourcePreviewV1.
        The ID that can be used to interact with the item

        :param id: The id of this DatasourcePreviewV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this DatasourcePreviewV1.
        Whether item is archived

        :return: The is_archived of this DatasourcePreviewV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this DatasourcePreviewV1.
        Whether item is archived

        :param is_archived: The is_archived of this DatasourcePreviewV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this DatasourcePreviewV1.
        Whether item is redacted

        :return: The is_redacted of this DatasourcePreviewV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this DatasourcePreviewV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this DatasourcePreviewV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this DatasourcePreviewV1.
        The human readable name

        :return: The name of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatasourcePreviewV1.
        The human readable name

        :param name: The name of this DatasourcePreviewV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def translation_key(self):
        """
        Gets the translation_key of this DatasourcePreviewV1.
        The item's translation key, if any

        :return: The translation_key of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this DatasourcePreviewV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this DatasourcePreviewV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this DatasourcePreviewV1.
        The type of the item

        :return: The type of this DatasourcePreviewV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatasourcePreviewV1.
        The type of the item

        :param type: The type of this DatasourcePreviewV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, DatasourcePreviewV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
