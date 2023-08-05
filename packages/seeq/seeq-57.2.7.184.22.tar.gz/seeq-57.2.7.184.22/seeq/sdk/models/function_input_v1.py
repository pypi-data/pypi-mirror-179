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


class FunctionInputV1(object):
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
        'additional_properties': 'list[ScalarPropertyV1]',
        'data_id': 'str',
        'description': 'str',
        'formula': 'str',
        'host_id': 'str',
        'name': 'str',
        'package_name': 'str',
        'parameters': 'list[FormulaParameterInputV1]',
        'properties': 'list[ScalarPropertyV1]',
        'scoped_to': 'str',
        'sync_token': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'data_id': 'dataId',
        'description': 'description',
        'formula': 'formula',
        'host_id': 'hostId',
        'name': 'name',
        'package_name': 'packageName',
        'parameters': 'parameters',
        'properties': 'properties',
        'scoped_to': 'scopedTo',
        'sync_token': 'syncToken',
        'type': 'type'
    }

    def __init__(self, additional_properties=None, data_id=None, description=None, formula=None, host_id=None, name=None, package_name=None, parameters=None, properties=None, scoped_to=None, sync_token=None, type=None):
        """
        FunctionInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._data_id = None
        self._description = None
        self._formula = None
        self._host_id = None
        self._name = None
        self._package_name = None
        self._parameters = None
        self._properties = None
        self._scoped_to = None
        self._sync_token = None
        self._type = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if data_id is not None:
          self.data_id = data_id
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if host_id is not None:
          self.host_id = host_id
        if name is not None:
          self.name = name
        if package_name is not None:
          self.package_name = package_name
        if parameters is not None:
          self.parameters = parameters
        if properties is not None:
          self.properties = properties
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if sync_token is not None:
          self.sync_token = sync_token
        if type is not None:
          self.type = type

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this FunctionInputV1.

        :return: The additional_properties of this FunctionInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this FunctionInputV1.

        :param additional_properties: The additional_properties of this FunctionInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def data_id(self):
        """
        Gets the data_id of this FunctionInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this FunctionInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this FunctionInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this FunctionInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def description(self):
        """
        Gets the description of this FunctionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this FunctionInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FunctionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this FunctionInputV1.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this FunctionInputV1.
        The formula that represents the body of the function

        :return: The formula of this FunctionInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FunctionInputV1.
        The formula that represents the body of the function

        :param formula: The formula of this FunctionInputV1.
        :type: str
        """
        if formula is None:
            raise ValueError("Invalid value for `formula`, must not be `None`")

        self._formula = formula

    @property
    def host_id(self):
        """
        Gets the host_id of this FunctionInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :return: The host_id of this FunctionInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this FunctionInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :param host_id: The host_id of this FunctionInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def name(self):
        """
        Gets the name of this FunctionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this FunctionInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FunctionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this FunctionInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def package_name(self):
        """
        Gets the package_name of this FunctionInputV1.
        The name of the package that contains this function. Valid only for UserDefinedFormulaFunctions when creating the function, cannot be changed for existing UDFs.

        :return: The package_name of this FunctionInputV1.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this FunctionInputV1.
        The name of the package that contains this function. Valid only for UserDefinedFormulaFunctions when creating the function, cannot be changed for existing UDFs.

        :param package_name: The package_name of this FunctionInputV1.
        :type: str
        """

        self._package_name = package_name

    @property
    def parameters(self):
        """
        Gets the parameters of this FunctionInputV1.
        Any parameters that should be placed in the context of the executing formula. At least one unbound parameter is required for AggregatingFormulaFunctions and Charts.

        :return: The parameters of this FunctionInputV1.
        :rtype: list[FormulaParameterInputV1]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FunctionInputV1.
        Any parameters that should be placed in the context of the executing formula. At least one unbound parameter is required for AggregatingFormulaFunctions and Charts.

        :param parameters: The parameters of this FunctionInputV1.
        :type: list[FormulaParameterInputV1]
        """

        self._parameters = parameters

    @property
    def properties(self):
        """
        Gets the properties of this FunctionInputV1.

        :return: The properties of this FunctionInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this FunctionInputV1.

        :param properties: The properties of this FunctionInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this FunctionInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this FunctionInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this FunctionInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this FunctionInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def sync_token(self):
        """
        Gets the sync_token of this FunctionInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this FunctionInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this FunctionInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this FunctionInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def type(self):
        """
        Gets the type of this FunctionInputV1.
        The item subtype for this function. Valid types include AggregatingFormulaFunction, UserDefinedFormulaFunction, and Chart

        :return: The type of this FunctionInputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FunctionInputV1.
        The item subtype for this function. Valid types include AggregatingFormulaFunction, UserDefinedFormulaFunction, and Chart

        :param type: The type of this FunctionInputV1.
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
        if not isinstance(other, FunctionInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
