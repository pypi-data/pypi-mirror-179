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


class DisplayTemplateInputV1(object):
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
        'description': 'str',
        'name': 'str',
        'scoped_to': 'str',
        'source_workstep_id': 'str',
        'swap_source_asset_id': 'str'
    }

    attribute_map = {
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'name': 'name',
        'scoped_to': 'scopedTo',
        'source_workstep_id': 'sourceWorkstepId',
        'swap_source_asset_id': 'swapSourceAssetId'
    }

    def __init__(self, datasource_class=None, datasource_id=None, description=None, name=None, scoped_to=None, source_workstep_id=None, swap_source_asset_id=None):
        """
        DisplayTemplateInputV1 - a model defined in Swagger
        """

        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._name = None
        self._scoped_to = None
        self._source_workstep_id = None
        self._swap_source_asset_id = None

        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if source_workstep_id is not None:
          self.source_workstep_id = source_workstep_id
        if swap_source_asset_id is not None:
          self.swap_source_asset_id = swap_source_asset_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this DisplayTemplateInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource.

        :return: The datasource_class of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this DisplayTemplateInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource.

        :param datasource_class: The datasource_class of this DisplayTemplateInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this DisplayTemplateInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource.

        :return: The datasource_id of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this DisplayTemplateInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource.

        :param datasource_id: The datasource_id of this DisplayTemplateInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this DisplayTemplateInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DisplayTemplateInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this DisplayTemplateInputV1.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this DisplayTemplateInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DisplayTemplateInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this DisplayTemplateInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this DisplayTemplateInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this DisplayTemplateInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this DisplayTemplateInputV1.
        :type: str
        """
        if scoped_to is None:
            raise ValueError("Invalid value for `scoped_to`, must not be `None`")

        self._scoped_to = scoped_to

    @property
    def source_workstep_id(self):
        """
        Gets the source_workstep_id of this DisplayTemplateInputV1.
        The ID of the source workstep for the display template

        :return: The source_workstep_id of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._source_workstep_id

    @source_workstep_id.setter
    def source_workstep_id(self, source_workstep_id):
        """
        Sets the source_workstep_id of this DisplayTemplateInputV1.
        The ID of the source workstep for the display template

        :param source_workstep_id: The source_workstep_id of this DisplayTemplateInputV1.
        :type: str
        """
        if source_workstep_id is None:
            raise ValueError("Invalid value for `source_workstep_id`, must not be `None`")

        self._source_workstep_id = source_workstep_id

    @property
    def swap_source_asset_id(self):
        """
        Gets the swap_source_asset_id of this DisplayTemplateInputV1.
        The asset to swap out when loading displays based on this template

        :return: The swap_source_asset_id of this DisplayTemplateInputV1.
        :rtype: str
        """
        return self._swap_source_asset_id

    @swap_source_asset_id.setter
    def swap_source_asset_id(self, swap_source_asset_id):
        """
        Sets the swap_source_asset_id of this DisplayTemplateInputV1.
        The asset to swap out when loading displays based on this template

        :param swap_source_asset_id: The swap_source_asset_id of this DisplayTemplateInputV1.
        :type: str
        """

        self._swap_source_asset_id = swap_source_asset_id

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
        if not isinstance(other, DisplayTemplateInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
