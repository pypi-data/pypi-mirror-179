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


class AgentStatusOutputV1(object):
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
        'name': 'str',
        'remote_agent': 'bool',
        'remote_update_error': 'str',
        'remote_update_status': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remote_agent': 'remoteAgent',
        'remote_update_error': 'remoteUpdateError',
        'remote_update_status': 'remoteUpdateStatus',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, name=None, remote_agent=False, remote_update_error=None, remote_update_status=None, status=None, version=None):
        """
        AgentStatusOutputV1 - a model defined in Swagger
        """

        self._name = None
        self._remote_agent = None
        self._remote_update_error = None
        self._remote_update_status = None
        self._status = None
        self._version = None

        if name is not None:
          self.name = name
        if remote_agent is not None:
          self.remote_agent = remote_agent
        if remote_update_error is not None:
          self.remote_update_error = remote_update_error
        if remote_update_status is not None:
          self.remote_update_status = remote_update_status
        if status is not None:
          self.status = status
        if version is not None:
          self.version = version

    @property
    def name(self):
        """
        Gets the name of this AgentStatusOutputV1.
        The name of the agent. This name uniquely identifies the agent

        :return: The name of this AgentStatusOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AgentStatusOutputV1.
        The name of the agent. This name uniquely identifies the agent

        :param name: The name of this AgentStatusOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def remote_agent(self):
        """
        Gets the remote_agent of this AgentStatusOutputV1.
        Indicates if the agent is a remote agent. This is false for local agents.

        :return: The remote_agent of this AgentStatusOutputV1.
        :rtype: bool
        """
        return self._remote_agent

    @remote_agent.setter
    def remote_agent(self, remote_agent):
        """
        Sets the remote_agent of this AgentStatusOutputV1.
        Indicates if the agent is a remote agent. This is false for local agents.

        :param remote_agent: The remote_agent of this AgentStatusOutputV1.
        :type: bool
        """

        self._remote_agent = remote_agent

    @property
    def remote_update_error(self):
        """
        Gets the remote_update_error of this AgentStatusOutputV1.
        Error if any for remote agent update

        :return: The remote_update_error of this AgentStatusOutputV1.
        :rtype: str
        """
        return self._remote_update_error

    @remote_update_error.setter
    def remote_update_error(self, remote_update_error):
        """
        Sets the remote_update_error of this AgentStatusOutputV1.
        Error if any for remote agent update

        :param remote_update_error: The remote_update_error of this AgentStatusOutputV1.
        :type: str
        """

        self._remote_update_error = remote_update_error

    @property
    def remote_update_status(self):
        """
        Gets the remote_update_status of this AgentStatusOutputV1.
        Version Update status of remote agents

        :return: The remote_update_status of this AgentStatusOutputV1.
        :rtype: str
        """
        return self._remote_update_status

    @remote_update_status.setter
    def remote_update_status(self, remote_update_status):
        """
        Sets the remote_update_status of this AgentStatusOutputV1.
        Version Update status of remote agents

        :param remote_update_status: The remote_update_status of this AgentStatusOutputV1.
        :type: str
        """

        self._remote_update_status = remote_update_status

    @property
    def status(self):
        """
        Gets the status of this AgentStatusOutputV1.
        The status of the current connection between the agent and the Seeq application server. Valid values are CONNECTED, CONNECTING and DISCONNECTED

        :return: The status of this AgentStatusOutputV1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AgentStatusOutputV1.
        The status of the current connection between the agent and the Seeq application server. Valid values are CONNECTED, CONNECTING and DISCONNECTED

        :param status: The status of this AgentStatusOutputV1.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def version(self):
        """
        Gets the version of this AgentStatusOutputV1.
        The Seeq version of the agent

        :return: The version of this AgentStatusOutputV1.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AgentStatusOutputV1.
        The Seeq version of the agent

        :param version: The version of this AgentStatusOutputV1.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, AgentStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
