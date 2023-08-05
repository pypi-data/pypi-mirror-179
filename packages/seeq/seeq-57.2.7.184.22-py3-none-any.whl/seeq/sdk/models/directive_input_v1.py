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


class DirectiveInputV1(object):
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
        'download_installer': 'bool',
        'run_version': 'str',
        'stage_installer': 'str'
    }

    attribute_map = {
        'download_installer': 'downloadInstaller',
        'run_version': 'runVersion',
        'stage_installer': 'stageInstaller'
    }

    def __init__(self, download_installer=None, run_version=None, stage_installer=None):
        """
        DirectiveInputV1 - a model defined in Swagger
        """

        self._download_installer = None
        self._run_version = None
        self._stage_installer = None

        if download_installer is not None:
          self.download_installer = download_installer
        if run_version is not None:
          self.run_version = run_version
        if stage_installer is not None:
          self.stage_installer = stage_installer

    @property
    def download_installer(self):
        """
        Gets the download_installer of this DirectiveInputV1.
        If true the installer must be downloaded from the seeq site.

        :return: The download_installer of this DirectiveInputV1.
        :rtype: bool
        """
        return self._download_installer

    @download_installer.setter
    def download_installer(self, download_installer):
        """
        Sets the download_installer of this DirectiveInputV1.
        If true the installer must be downloaded from the seeq site.

        :param download_installer: The download_installer of this DirectiveInputV1.
        :type: bool
        """

        self._download_installer = download_installer

    @property
    def run_version(self):
        """
        Gets the run_version of this DirectiveInputV1.
        Product Marketing Name of the installer

        :return: The run_version of this DirectiveInputV1.
        :rtype: str
        """
        return self._run_version

    @run_version.setter
    def run_version(self, run_version):
        """
        Sets the run_version of this DirectiveInputV1.
        Product Marketing Name of the installer

        :param run_version: The run_version of this DirectiveInputV1.
        :type: str
        """

        self._run_version = run_version

    @property
    def stage_installer(self):
        """
        Gets the stage_installer of this DirectiveInputV1.
        Installer name with extension

        :return: The stage_installer of this DirectiveInputV1.
        :rtype: str
        """
        return self._stage_installer

    @stage_installer.setter
    def stage_installer(self, stage_installer):
        """
        Sets the stage_installer of this DirectiveInputV1.
        Installer name with extension

        :param stage_installer: The stage_installer of this DirectiveInputV1.
        :type: str
        """

        self._stage_installer = stage_installer

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
        if not isinstance(other, DirectiveInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
