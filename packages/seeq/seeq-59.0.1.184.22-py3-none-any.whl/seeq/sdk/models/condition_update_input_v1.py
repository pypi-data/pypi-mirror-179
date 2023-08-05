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


class ConditionUpdateInputV1(object):
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
        'capsule_properties': 'list[CapsulePropertyInputV1]',
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'formula': 'str',
        'historical_data_version': 'str',
        'host_id': 'str',
        'maximum_duration': 'str',
        'name': 'str',
        'parameters': 'list[str]',
        'properties': 'list[ScalarPropertyV1]',
        'replace_capsule_properties': 'bool',
        'scoped_to': 'str',
        'security_string': 'str',
        'source_security_string': 'str',
        'sync_token': 'str',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'capsule_properties': 'capsuleProperties',
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'formula': 'formula',
        'historical_data_version': 'historicalDataVersion',
        'host_id': 'hostId',
        'maximum_duration': 'maximumDuration',
        'name': 'name',
        'parameters': 'parameters',
        'properties': 'properties',
        'replace_capsule_properties': 'replaceCapsuleProperties',
        'scoped_to': 'scopedTo',
        'security_string': 'securityString',
        'source_security_string': 'sourceSecurityString',
        'sync_token': 'syncToken',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, additional_properties=None, capsule_properties=None, data_id=None, datasource_class=None, datasource_id=None, description=None, formula=None, historical_data_version=None, host_id=None, maximum_duration=None, name=None, parameters=None, properties=None, replace_capsule_properties=False, scoped_to=None, security_string=None, source_security_string=None, sync_token=None, unit_of_measure=None):
        """
        ConditionUpdateInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._capsule_properties = None
        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._formula = None
        self._historical_data_version = None
        self._host_id = None
        self._maximum_duration = None
        self._name = None
        self._parameters = None
        self._properties = None
        self._replace_capsule_properties = None
        self._scoped_to = None
        self._security_string = None
        self._source_security_string = None
        self._sync_token = None
        self._unit_of_measure = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if capsule_properties is not None:
          self.capsule_properties = capsule_properties
        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if historical_data_version is not None:
          self.historical_data_version = historical_data_version
        if host_id is not None:
          self.host_id = host_id
        if maximum_duration is not None:
          self.maximum_duration = maximum_duration
        if name is not None:
          self.name = name
        if parameters is not None:
          self.parameters = parameters
        if properties is not None:
          self.properties = properties
        if replace_capsule_properties is not None:
          self.replace_capsule_properties = replace_capsule_properties
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if security_string is not None:
          self.security_string = security_string
        if source_security_string is not None:
          self.source_security_string = source_security_string
        if sync_token is not None:
          self.sync_token = sync_token
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ConditionUpdateInputV1.

        :return: The additional_properties of this ConditionUpdateInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ConditionUpdateInputV1.

        :param additional_properties: The additional_properties of this ConditionUpdateInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def capsule_properties(self):
        """
        Gets the capsule_properties of this ConditionUpdateInputV1.
        Property metadata for capsules on this condition. Only applicable to stored conditions.

        :return: The capsule_properties of this ConditionUpdateInputV1.
        :rtype: list[CapsulePropertyInputV1]
        """
        return self._capsule_properties

    @capsule_properties.setter
    def capsule_properties(self, capsule_properties):
        """
        Sets the capsule_properties of this ConditionUpdateInputV1.
        Property metadata for capsules on this condition. Only applicable to stored conditions.

        :param capsule_properties: The capsule_properties of this ConditionUpdateInputV1.
        :type: list[CapsulePropertyInputV1]
        """

        self._capsule_properties = capsule_properties

    @property
    def data_id(self):
        """
        Gets the data_id of this ConditionUpdateInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this ConditionUpdateInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this ConditionUpdateInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ConditionUpdateInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_class of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ConditionUpdateInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_class: The datasource_class of this ConditionUpdateInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ConditionUpdateInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_id of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ConditionUpdateInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_id: The datasource_id of this ConditionUpdateInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this ConditionUpdateInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConditionUpdateInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this ConditionUpdateInputV1.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this ConditionUpdateInputV1.
        Information about the formula used to create a calculated item. Not marked as required because this class is extended by classes where it is optional

        :return: The formula of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this ConditionUpdateInputV1.
        Information about the formula used to create a calculated item. Not marked as required because this class is extended by classes where it is optional

        :param formula: The formula of this ConditionUpdateInputV1.
        :type: str
        """

        self._formula = formula

    @property
    def historical_data_version(self):
        """
        Gets the historical_data_version of this ConditionUpdateInputV1.
        This property tells Seeq that certain, and thus potentially cached, capsules in the past have been changed. Changing the value of this property will will clear the cache of this condition and all formulas that depend on it. It should not be changed when new uncached capsules are coming in. Changes to this property have no effect on calculated conditions.

        :return: The historical_data_version of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._historical_data_version

    @historical_data_version.setter
    def historical_data_version(self, historical_data_version):
        """
        Sets the historical_data_version of this ConditionUpdateInputV1.
        This property tells Seeq that certain, and thus potentially cached, capsules in the past have been changed. Changing the value of this property will will clear the cache of this condition and all formulas that depend on it. It should not be changed when new uncached capsules are coming in. Changes to this property have no effect on calculated conditions.

        :param historical_data_version: The historical_data_version of this ConditionUpdateInputV1.
        :type: str
        """

        self._historical_data_version = historical_data_version

    @property
    def host_id(self):
        """
        Gets the host_id of this ConditionUpdateInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :return: The host_id of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this ConditionUpdateInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :param host_id: The host_id of this ConditionUpdateInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def maximum_duration(self):
        """
        Gets the maximum_duration of this ConditionUpdateInputV1.
        The maximum duration of capsules in this series. Required for stored conditions.

        :return: The maximum_duration of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._maximum_duration

    @maximum_duration.setter
    def maximum_duration(self, maximum_duration):
        """
        Sets the maximum_duration of this ConditionUpdateInputV1.
        The maximum duration of capsules in this series. Required for stored conditions.

        :param maximum_duration: The maximum_duration of this ConditionUpdateInputV1.
        :type: str
        """
        if maximum_duration is None:
            raise ValueError("Invalid value for `maximum_duration`, must not be `None`")

        self._maximum_duration = maximum_duration

    @property
    def name(self):
        """
        Gets the name of this ConditionUpdateInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConditionUpdateInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this ConditionUpdateInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameters(self):
        """
        Gets the parameters of this ConditionUpdateInputV1.

        :return: The parameters of this ConditionUpdateInputV1.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ConditionUpdateInputV1.

        :param parameters: The parameters of this ConditionUpdateInputV1.
        :type: list[str]
        """

        self._parameters = parameters

    @property
    def properties(self):
        """
        Gets the properties of this ConditionUpdateInputV1.

        :return: The properties of this ConditionUpdateInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ConditionUpdateInputV1.

        :param properties: The properties of this ConditionUpdateInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def replace_capsule_properties(self):
        """
        Gets the replace_capsule_properties of this ConditionUpdateInputV1.
        When true, remove all capsule properties that are not specified incapsuleProperties on the condition input; not used for calculated or stored-in-Seeq conditions

        :return: The replace_capsule_properties of this ConditionUpdateInputV1.
        :rtype: bool
        """
        return self._replace_capsule_properties

    @replace_capsule_properties.setter
    def replace_capsule_properties(self, replace_capsule_properties):
        """
        Sets the replace_capsule_properties of this ConditionUpdateInputV1.
        When true, remove all capsule properties that are not specified incapsuleProperties on the condition input; not used for calculated or stored-in-Seeq conditions

        :param replace_capsule_properties: The replace_capsule_properties of this ConditionUpdateInputV1.
        :type: bool
        """

        self._replace_capsule_properties = replace_capsule_properties

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ConditionUpdateInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ConditionUpdateInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this ConditionUpdateInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def security_string(self):
        """
        Gets the security_string of this ConditionUpdateInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :return: The security_string of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._security_string

    @security_string.setter
    def security_string(self, security_string):
        """
        Sets the security_string of this ConditionUpdateInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :param security_string: The security_string of this ConditionUpdateInputV1.
        :type: str
        """

        self._security_string = security_string

    @property
    def source_security_string(self):
        """
        Gets the source_security_string of this ConditionUpdateInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :return: The source_security_string of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._source_security_string

    @source_security_string.setter
    def source_security_string(self, source_security_string):
        """
        Sets the source_security_string of this ConditionUpdateInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :param source_security_string: The source_security_string of this ConditionUpdateInputV1.
        :type: str
        """

        self._source_security_string = source_security_string

    @property
    def sync_token(self):
        """
        Gets the sync_token of this ConditionUpdateInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this ConditionUpdateInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this ConditionUpdateInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this ConditionUpdateInputV1.

        :return: The unit_of_measure of this ConditionUpdateInputV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this ConditionUpdateInputV1.

        :param unit_of_measure: The unit_of_measure of this ConditionUpdateInputV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if not isinstance(other, ConditionUpdateInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
