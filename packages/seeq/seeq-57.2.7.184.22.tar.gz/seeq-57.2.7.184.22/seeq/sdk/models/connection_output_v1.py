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


class ConnectionOutputV1(object):
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
        'agent_name': 'str',
        'backups': 'list[JsonBackupOutputV1]',
        'connection_id': 'str',
        'connector_name': 'str',
        'created_at': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'enabled': 'bool',
        'id': 'str',
        'indexing_connection': 'bool',
        'is_archived': 'bool',
        'json': 'str',
        'max_concurrent_requests': 'int',
        'max_results_per_requests': 'int',
        'name': 'str',
        'propagation_pending': 'bool',
        'pull_connection': 'bool',
        'status_message': 'str',
        'transforms': 'str',
        'type': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'agent_name': 'agentName',
        'backups': 'backups',
        'connection_id': 'connectionId',
        'connector_name': 'connectorName',
        'created_at': 'createdAt',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'enabled': 'enabled',
        'id': 'id',
        'indexing_connection': 'indexingConnection',
        'is_archived': 'isArchived',
        'json': 'json',
        'max_concurrent_requests': 'maxConcurrentRequests',
        'max_results_per_requests': 'maxResultsPerRequests',
        'name': 'name',
        'propagation_pending': 'propagationPending',
        'pull_connection': 'pullConnection',
        'status_message': 'statusMessage',
        'transforms': 'transforms',
        'type': 'type',
        'updated_at': 'updatedAt'
    }

    def __init__(self, agent_name=None, backups=None, connection_id=None, connector_name=None, created_at=None, datasource_class=None, datasource_id=None, description=None, effective_permissions=None, enabled=False, id=None, indexing_connection=False, is_archived=False, json=None, max_concurrent_requests=None, max_results_per_requests=None, name=None, propagation_pending=False, pull_connection=False, status_message=None, transforms=None, type=None, updated_at=None):
        """
        ConnectionOutputV1 - a model defined in Swagger
        """

        self._agent_name = None
        self._backups = None
        self._connection_id = None
        self._connector_name = None
        self._created_at = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._effective_permissions = None
        self._enabled = None
        self._id = None
        self._indexing_connection = None
        self._is_archived = None
        self._json = None
        self._max_concurrent_requests = None
        self._max_results_per_requests = None
        self._name = None
        self._propagation_pending = None
        self._pull_connection = None
        self._status_message = None
        self._transforms = None
        self._type = None
        self._updated_at = None

        if agent_name is not None:
          self.agent_name = agent_name
        if backups is not None:
          self.backups = backups
        if connection_id is not None:
          self.connection_id = connection_id
        if connector_name is not None:
          self.connector_name = connector_name
        if created_at is not None:
          self.created_at = created_at
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if enabled is not None:
          self.enabled = enabled
        if id is not None:
          self.id = id
        if indexing_connection is not None:
          self.indexing_connection = indexing_connection
        if is_archived is not None:
          self.is_archived = is_archived
        if json is not None:
          self.json = json
        if max_concurrent_requests is not None:
          self.max_concurrent_requests = max_concurrent_requests
        if max_results_per_requests is not None:
          self.max_results_per_requests = max_results_per_requests
        if name is not None:
          self.name = name
        if propagation_pending is not None:
          self.propagation_pending = propagation_pending
        if pull_connection is not None:
          self.pull_connection = pull_connection
        if status_message is not None:
          self.status_message = status_message
        if transforms is not None:
          self.transforms = transforms
        if type is not None:
          self.type = type
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def agent_name(self):
        """
        Gets the agent_name of this ConnectionOutputV1.
        The name of the agent

        :return: The agent_name of this ConnectionOutputV1.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """
        Sets the agent_name of this ConnectionOutputV1.
        The name of the agent

        :param agent_name: The agent_name of this ConnectionOutputV1.
        :type: str
        """

        self._agent_name = agent_name

    @property
    def backups(self):
        """
        Gets the backups of this ConnectionOutputV1.
        The list of backups for this object's json property.

        :return: The backups of this ConnectionOutputV1.
        :rtype: list[JsonBackupOutputV1]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """
        Sets the backups of this ConnectionOutputV1.
        The list of backups for this object's json property.

        :param backups: The backups of this ConnectionOutputV1.
        :type: list[JsonBackupOutputV1]
        """

        self._backups = backups

    @property
    def connection_id(self):
        """
        Gets the connection_id of this ConnectionOutputV1.
        The human readable unique identifier of the connection

        :return: The connection_id of this ConnectionOutputV1.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this ConnectionOutputV1.
        The human readable unique identifier of the connection

        :param connection_id: The connection_id of this ConnectionOutputV1.
        :type: str
        """

        self._connection_id = connection_id

    @property
    def connector_name(self):
        """
        Gets the connector_name of this ConnectionOutputV1.
        The name of the connector

        :return: The connector_name of this ConnectionOutputV1.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this ConnectionOutputV1.
        The name of the connector

        :param connector_name: The connector_name of this ConnectionOutputV1.
        :type: str
        """

        self._connector_name = connector_name

    @property
    def created_at(self):
        """
        Gets the created_at of this ConnectionOutputV1.
        The ISO 8601 date of when the object was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :return: The created_at of this ConnectionOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ConnectionOutputV1.
        The ISO 8601 date of when the object was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :param created_at: The created_at of this ConnectionOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ConnectionOutputV1.
        The datasource class

        :return: The datasource_class of this ConnectionOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ConnectionOutputV1.
        The datasource class

        :param datasource_class: The datasource_class of this ConnectionOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ConnectionOutputV1.
        The datasource ID

        :return: The datasource_id of this ConnectionOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ConnectionOutputV1.
        The datasource ID

        :param datasource_id: The datasource_id of this ConnectionOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this ConnectionOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this ConnectionOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConnectionOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this ConnectionOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this ConnectionOutputV1.

        :return: The effective_permissions of this ConnectionOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this ConnectionOutputV1.

        :param effective_permissions: The effective_permissions of this ConnectionOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def enabled(self):
        """
        Gets the enabled of this ConnectionOutputV1.
        True if the connection is enabled

        :return: The enabled of this ConnectionOutputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ConnectionOutputV1.
        True if the connection is enabled

        :param enabled: The enabled of this ConnectionOutputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """
        Gets the id of this ConnectionOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ConnectionOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ConnectionOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def indexing_connection(self):
        """
        Gets the indexing_connection of this ConnectionOutputV1.
        True if the connection is an indexing connection

        :return: The indexing_connection of this ConnectionOutputV1.
        :rtype: bool
        """
        return self._indexing_connection

    @indexing_connection.setter
    def indexing_connection(self, indexing_connection):
        """
        Sets the indexing_connection of this ConnectionOutputV1.
        True if the connection is an indexing connection

        :param indexing_connection: The indexing_connection of this ConnectionOutputV1.
        :type: bool
        """

        self._indexing_connection = indexing_connection

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ConnectionOutputV1.
        Whether item is archived

        :return: The is_archived of this ConnectionOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ConnectionOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this ConnectionOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def json(self):
        """
        Gets the json of this ConnectionOutputV1.
        The connection configuration json.

        :return: The json of this ConnectionOutputV1.
        :rtype: str
        """
        return self._json

    @json.setter
    def json(self, json):
        """
        Sets the json of this ConnectionOutputV1.
        The connection configuration json.

        :param json: The json of this ConnectionOutputV1.
        :type: str
        """

        self._json = json

    @property
    def max_concurrent_requests(self):
        """
        Gets the max_concurrent_requests of this ConnectionOutputV1.
        The maximum number of requests through this connection

        :return: The max_concurrent_requests of this ConnectionOutputV1.
        :rtype: int
        """
        return self._max_concurrent_requests

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, max_concurrent_requests):
        """
        Sets the max_concurrent_requests of this ConnectionOutputV1.
        The maximum number of requests through this connection

        :param max_concurrent_requests: The max_concurrent_requests of this ConnectionOutputV1.
        :type: int
        """

        self._max_concurrent_requests = max_concurrent_requests

    @property
    def max_results_per_requests(self):
        """
        Gets the max_results_per_requests of this ConnectionOutputV1.
        The maximum number of results returned

        :return: The max_results_per_requests of this ConnectionOutputV1.
        :rtype: int
        """
        return self._max_results_per_requests

    @max_results_per_requests.setter
    def max_results_per_requests(self, max_results_per_requests):
        """
        Sets the max_results_per_requests of this ConnectionOutputV1.
        The maximum number of results returned

        :param max_results_per_requests: The max_results_per_requests of this ConnectionOutputV1.
        :type: int
        """

        self._max_results_per_requests = max_results_per_requests

    @property
    def name(self):
        """
        Gets the name of this ConnectionOutputV1.
        The human readable name

        :return: The name of this ConnectionOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionOutputV1.
        The human readable name

        :param name: The name of this ConnectionOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def propagation_pending(self):
        """
        Gets the propagation_pending of this ConnectionOutputV1.
        Whether the configuration change propagation is pending.

        :return: The propagation_pending of this ConnectionOutputV1.
        :rtype: bool
        """
        return self._propagation_pending

    @propagation_pending.setter
    def propagation_pending(self, propagation_pending):
        """
        Sets the propagation_pending of this ConnectionOutputV1.
        Whether the configuration change propagation is pending.

        :param propagation_pending: The propagation_pending of this ConnectionOutputV1.
        :type: bool
        """

        self._propagation_pending = propagation_pending

    @property
    def pull_connection(self):
        """
        Gets the pull_connection of this ConnectionOutputV1.
        True if the connection is a pull connection

        :return: The pull_connection of this ConnectionOutputV1.
        :rtype: bool
        """
        return self._pull_connection

    @pull_connection.setter
    def pull_connection(self, pull_connection):
        """
        Sets the pull_connection of this ConnectionOutputV1.
        True if the connection is a pull connection

        :param pull_connection: The pull_connection of this ConnectionOutputV1.
        :type: bool
        """

        self._pull_connection = pull_connection

    @property
    def status_message(self):
        """
        Gets the status_message of this ConnectionOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ConnectionOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ConnectionOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ConnectionOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def transforms(self):
        """
        Gets the transforms of this ConnectionOutputV1.
        The transforms to be applied as JSON

        :return: The transforms of this ConnectionOutputV1.
        :rtype: str
        """
        return self._transforms

    @transforms.setter
    def transforms(self, transforms):
        """
        Sets the transforms of this ConnectionOutputV1.
        The transforms to be applied as JSON

        :param transforms: The transforms of this ConnectionOutputV1.
        :type: str
        """

        self._transforms = transforms

    @property
    def type(self):
        """
        Gets the type of this ConnectionOutputV1.
        The type of the item

        :return: The type of this ConnectionOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConnectionOutputV1.
        The type of the item

        :param type: The type of this ConnectionOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ConnectionOutputV1.
        The ISO 8601 date of when the object was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :return: The updated_at of this ConnectionOutputV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ConnectionOutputV1.
        The ISO 8601 date of when the object was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm).

        :param updated_at: The updated_at of this ConnectionOutputV1.
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
        if not isinstance(other, ConnectionOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
