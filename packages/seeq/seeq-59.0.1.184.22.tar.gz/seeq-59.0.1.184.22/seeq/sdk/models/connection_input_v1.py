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


class ConnectionInputV1(object):
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
        'backup_name': 'str',
        'datasource_id': 'str',
        'enabled': 'bool',
        'json': 'str',
        'max_concurrent_requests': 'int',
        'max_results_per_requests': 'int',
        'transforms': 'str'
    }

    attribute_map = {
        'backup_name': 'backupName',
        'datasource_id': 'datasourceId',
        'enabled': 'enabled',
        'json': 'json',
        'max_concurrent_requests': 'maxConcurrentRequests',
        'max_results_per_requests': 'maxResultsPerRequests',
        'transforms': 'transforms'
    }

    def __init__(self, backup_name=None, datasource_id=None, enabled=False, json=None, max_concurrent_requests=None, max_results_per_requests=None, transforms=None):
        """
        ConnectionInputV1 - a model defined in Swagger
        """

        self._backup_name = None
        self._datasource_id = None
        self._enabled = None
        self._json = None
        self._max_concurrent_requests = None
        self._max_results_per_requests = None
        self._transforms = None

        if backup_name is not None:
          self.backup_name = backup_name
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if enabled is not None:
          self.enabled = enabled
        if json is not None:
          self.json = json
        if max_concurrent_requests is not None:
          self.max_concurrent_requests = max_concurrent_requests
        if max_results_per_requests is not None:
          self.max_results_per_requests = max_results_per_requests
        if transforms is not None:
          self.transforms = transforms

    @property
    def backup_name(self):
        """
        Gets the backup_name of this ConnectionInputV1.
        The name of a connection backup to restore, when updating a connection.

        :return: The backup_name of this ConnectionInputV1.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """
        Sets the backup_name of this ConnectionInputV1.
        The name of a connection backup to restore, when updating a connection.

        :param backup_name: The backup_name of this ConnectionInputV1.
        :type: str
        """

        self._backup_name = backup_name

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ConnectionInputV1.
        The datasource id

        :return: The datasource_id of this ConnectionInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ConnectionInputV1.
        The datasource id

        :param datasource_id: The datasource_id of this ConnectionInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def enabled(self):
        """
        Gets the enabled of this ConnectionInputV1.
        True if the connection is enabled

        :return: The enabled of this ConnectionInputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ConnectionInputV1.
        True if the connection is enabled

        :param enabled: The enabled of this ConnectionInputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def json(self):
        """
        Gets the json of this ConnectionInputV1.
        The connection configuration json.

        :return: The json of this ConnectionInputV1.
        :rtype: str
        """
        return self._json

    @json.setter
    def json(self, json):
        """
        Sets the json of this ConnectionInputV1.
        The connection configuration json.

        :param json: The json of this ConnectionInputV1.
        :type: str
        """

        self._json = json

    @property
    def max_concurrent_requests(self):
        """
        Gets the max_concurrent_requests of this ConnectionInputV1.
        The maximum number of concurrent requests through this connection

        :return: The max_concurrent_requests of this ConnectionInputV1.
        :rtype: int
        """
        return self._max_concurrent_requests

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, max_concurrent_requests):
        """
        Sets the max_concurrent_requests of this ConnectionInputV1.
        The maximum number of concurrent requests through this connection

        :param max_concurrent_requests: The max_concurrent_requests of this ConnectionInputV1.
        :type: int
        """

        self._max_concurrent_requests = max_concurrent_requests

    @property
    def max_results_per_requests(self):
        """
        Gets the max_results_per_requests of this ConnectionInputV1.
        The maximum number of sample/capsule results that can be returned by a request. When null, no limit is imposed. 

        :return: The max_results_per_requests of this ConnectionInputV1.
        :rtype: int
        """
        return self._max_results_per_requests

    @max_results_per_requests.setter
    def max_results_per_requests(self, max_results_per_requests):
        """
        Sets the max_results_per_requests of this ConnectionInputV1.
        The maximum number of sample/capsule results that can be returned by a request. When null, no limit is imposed. 

        :param max_results_per_requests: The max_results_per_requests of this ConnectionInputV1.
        :type: int
        """

        self._max_results_per_requests = max_results_per_requests

    @property
    def transforms(self):
        """
        Gets the transforms of this ConnectionInputV1.
        The transforms to be applied as JSON

        :return: The transforms of this ConnectionInputV1.
        :rtype: str
        """
        return self._transforms

    @transforms.setter
    def transforms(self, transforms):
        """
        Sets the transforms of this ConnectionInputV1.
        The transforms to be applied as JSON

        :param transforms: The transforms of this ConnectionInputV1.
        :type: str
        """

        self._transforms = transforms

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
        if not isinstance(other, ConnectionInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
