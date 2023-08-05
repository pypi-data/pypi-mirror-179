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


class RemoteAgentStatusOutputV1(object):
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
        'available_versions': 'list[str]',
        'base_version': 'str',
        'current_version': 'str',
        'free_disk_space': 'int',
        'name': 'str',
        'pending_progress': 'float',
        'pending_status': 'str',
        'pending_version': 'str',
        'platform': 'str',
        'platform_architecture': 'str',
        'platform_version': 'str',
        'status': 'str',
        'status_received_time': 'int',
        'updates_enabled': 'bool'
    }

    attribute_map = {
        'available_versions': 'availableVersions',
        'base_version': 'baseVersion',
        'current_version': 'currentVersion',
        'free_disk_space': 'freeDiskSpace',
        'name': 'name',
        'pending_progress': 'pendingProgress',
        'pending_status': 'pendingStatus',
        'pending_version': 'pendingVersion',
        'platform': 'platform',
        'platform_architecture': 'platformArchitecture',
        'platform_version': 'platformVersion',
        'status': 'status',
        'status_received_time': 'statusReceivedTime',
        'updates_enabled': 'updatesEnabled'
    }

    def __init__(self, available_versions=None, base_version=None, current_version=None, free_disk_space=None, name=None, pending_progress=None, pending_status=None, pending_version=None, platform=None, platform_architecture=None, platform_version=None, status=None, status_received_time=None, updates_enabled=False):
        """
        RemoteAgentStatusOutputV1 - a model defined in Swagger
        """

        self._available_versions = None
        self._base_version = None
        self._current_version = None
        self._free_disk_space = None
        self._name = None
        self._pending_progress = None
        self._pending_status = None
        self._pending_version = None
        self._platform = None
        self._platform_architecture = None
        self._platform_version = None
        self._status = None
        self._status_received_time = None
        self._updates_enabled = None

        if available_versions is not None:
          self.available_versions = available_versions
        if base_version is not None:
          self.base_version = base_version
        if current_version is not None:
          self.current_version = current_version
        if free_disk_space is not None:
          self.free_disk_space = free_disk_space
        if name is not None:
          self.name = name
        if pending_progress is not None:
          self.pending_progress = pending_progress
        if pending_status is not None:
          self.pending_status = pending_status
        if pending_version is not None:
          self.pending_version = pending_version
        if platform is not None:
          self.platform = platform
        if platform_architecture is not None:
          self.platform_architecture = platform_architecture
        if platform_version is not None:
          self.platform_version = platform_version
        if status is not None:
          self.status = status
        if status_received_time is not None:
          self.status_received_time = status_received_time
        if updates_enabled is not None:
          self.updates_enabled = updates_enabled

    @property
    def available_versions(self):
        """
        Gets the available_versions of this RemoteAgentStatusOutputV1.
        All versions that have been unpacked on the remote agent

        :return: The available_versions of this RemoteAgentStatusOutputV1.
        :rtype: list[str]
        """
        return self._available_versions

    @available_versions.setter
    def available_versions(self, available_versions):
        """
        Sets the available_versions of this RemoteAgentStatusOutputV1.
        All versions that have been unpacked on the remote agent

        :param available_versions: The available_versions of this RemoteAgentStatusOutputV1.
        :type: list[str]
        """

        self._available_versions = available_versions

    @property
    def base_version(self):
        """
        Gets the base_version of this RemoteAgentStatusOutputV1.
        The version installed by executing the installer, usually to a admin protected location. For example the installation located in C:\\Program Files\\ on Windows

        :return: The base_version of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._base_version

    @base_version.setter
    def base_version(self, base_version):
        """
        Sets the base_version of this RemoteAgentStatusOutputV1.
        The version installed by executing the installer, usually to a admin protected location. For example the installation located in C:\\Program Files\\ on Windows

        :param base_version: The base_version of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._base_version = base_version

    @property
    def current_version(self):
        """
        Gets the current_version of this RemoteAgentStatusOutputV1.
        The version currently running on the remote agent

        :return: The current_version of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """
        Sets the current_version of this RemoteAgentStatusOutputV1.
        The version currently running on the remote agent

        :param current_version: The current_version of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._current_version = current_version

    @property
    def free_disk_space(self):
        """
        Gets the free_disk_space of this RemoteAgentStatusOutputV1.
        Amount of free space in bytes on the drive containing the data folder of the remote agent

        :return: The free_disk_space of this RemoteAgentStatusOutputV1.
        :rtype: int
        """
        return self._free_disk_space

    @free_disk_space.setter
    def free_disk_space(self, free_disk_space):
        """
        Sets the free_disk_space of this RemoteAgentStatusOutputV1.
        Amount of free space in bytes on the drive containing the data folder of the remote agent

        :param free_disk_space: The free_disk_space of this RemoteAgentStatusOutputV1.
        :type: int
        """

        self._free_disk_space = free_disk_space

    @property
    def name(self):
        """
        Gets the name of this RemoteAgentStatusOutputV1.
        Name of the remote agent; composed of the hostname and the installation suffix

        :return: The name of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RemoteAgentStatusOutputV1.
        Name of the remote agent; composed of the hostname and the installation suffix

        :param name: The name of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._name = name

    @property
    def pending_progress(self):
        """
        Gets the pending_progress of this RemoteAgentStatusOutputV1.
        The progress of downloading and extracting the pending version; A number between 0 and 1 inclusive where 0 indicates 0% complete and 1 indicates 100% complete

        :return: The pending_progress of this RemoteAgentStatusOutputV1.
        :rtype: float
        """
        return self._pending_progress

    @pending_progress.setter
    def pending_progress(self, pending_progress):
        """
        Sets the pending_progress of this RemoteAgentStatusOutputV1.
        The progress of downloading and extracting the pending version; A number between 0 and 1 inclusive where 0 indicates 0% complete and 1 indicates 100% complete

        :param pending_progress: The pending_progress of this RemoteAgentStatusOutputV1.
        :type: float
        """

        self._pending_progress = pending_progress

    @property
    def pending_status(self):
        """
        Gets the pending_status of this RemoteAgentStatusOutputV1.
        The current stage of a pending downloading and extracting on a remote agent

        :return: The pending_status of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._pending_status

    @pending_status.setter
    def pending_status(self, pending_status):
        """
        Sets the pending_status of this RemoteAgentStatusOutputV1.
        The current stage of a pending downloading and extracting on a remote agent

        :param pending_status: The pending_status of this RemoteAgentStatusOutputV1.
        :type: str
        """
        allowed_values = ["NONE", "DOWNLOADING", "EXTRACTING", "SUCCESS", "RESTART", "ERROR"]
        if pending_status not in allowed_values:
            raise ValueError(
                "Invalid value for `pending_status` ({0}), must be one of {1}"
                .format(pending_status, allowed_values)
            )

        self._pending_status = pending_status

    @property
    def pending_version(self):
        """
        Gets the pending_version of this RemoteAgentStatusOutputV1.
        The version currently downloading and/or extracting on the remote agent

        :return: The pending_version of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._pending_version

    @pending_version.setter
    def pending_version(self, pending_version):
        """
        Sets the pending_version of this RemoteAgentStatusOutputV1.
        The version currently downloading and/or extracting on the remote agent

        :param pending_version: The pending_version of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._pending_version = pending_version

    @property
    def platform(self):
        """
        Gets the platform of this RemoteAgentStatusOutputV1.
        Operating system of the remote agent; linux or windows

        :return: The platform of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this RemoteAgentStatusOutputV1.
        Operating system of the remote agent; linux or windows

        :param platform: The platform of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._platform = platform

    @property
    def platform_architecture(self):
        """
        Gets the platform_architecture of this RemoteAgentStatusOutputV1.
        Architecture of platform; 32bits or 64bits

        :return: The platform_architecture of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._platform_architecture

    @platform_architecture.setter
    def platform_architecture(self, platform_architecture):
        """
        Sets the platform_architecture of this RemoteAgentStatusOutputV1.
        Architecture of platform; 32bits or 64bits

        :param platform_architecture: The platform_architecture of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._platform_architecture = platform_architecture

    @property
    def platform_version(self):
        """
        Gets the platform_version of this RemoteAgentStatusOutputV1.
        Version and distribution of platform; Ubuntu 20.04, Windows Server 2019, etc

        :return: The platform_version of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this RemoteAgentStatusOutputV1.
        Version and distribution of platform; Ubuntu 20.04, Windows Server 2019, etc

        :param platform_version: The platform_version of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._platform_version = platform_version

    @property
    def status(self):
        """
        Gets the status of this RemoteAgentStatusOutputV1.
        Free form text description of the current stage of the remote agent. If the pending version couldn't be downloaded or extracted then the status should include the error or reason that it couldn't be completed and if the operation will be retried

        :return: The status of this RemoteAgentStatusOutputV1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RemoteAgentStatusOutputV1.
        Free form text description of the current stage of the remote agent. If the pending version couldn't be downloaded or extracted then the status should include the error or reason that it couldn't be completed and if the operation will be retried

        :param status: The status of this RemoteAgentStatusOutputV1.
        :type: str
        """

        self._status = status

    @property
    def status_received_time(self):
        """
        Gets the status_received_time of this RemoteAgentStatusOutputV1.
        Time when the status was last received

        :return: The status_received_time of this RemoteAgentStatusOutputV1.
        :rtype: int
        """
        return self._status_received_time

    @status_received_time.setter
    def status_received_time(self, status_received_time):
        """
        Sets the status_received_time of this RemoteAgentStatusOutputV1.
        Time when the status was last received

        :param status_received_time: The status_received_time of this RemoteAgentStatusOutputV1.
        :type: int
        """

        self._status_received_time = status_received_time

    @property
    def updates_enabled(self):
        """
        Gets the updates_enabled of this RemoteAgentStatusOutputV1.
        True if remote agent has the remote update feature enabled

        :return: The updates_enabled of this RemoteAgentStatusOutputV1.
        :rtype: bool
        """
        return self._updates_enabled

    @updates_enabled.setter
    def updates_enabled(self, updates_enabled):
        """
        Sets the updates_enabled of this RemoteAgentStatusOutputV1.
        True if remote agent has the remote update feature enabled

        :param updates_enabled: The updates_enabled of this RemoteAgentStatusOutputV1.
        :type: bool
        """

        self._updates_enabled = updates_enabled

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
        if not isinstance(other, RemoteAgentStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
