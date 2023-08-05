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


class ScheduledNotebookInputV1(object):
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
        'description': 'str',
        'enabled': 'bool',
        'file_path': 'str',
        'label': 'str',
        'schedules': 'list[ScheduleInputV1]',
        'timezone': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'file_path': 'filePath',
        'label': 'label',
        'schedules': 'schedules',
        'timezone': 'timezone',
        'user_id': 'userId'
    }

    def __init__(self, description=None, enabled=True, file_path=None, label=None, schedules=None, timezone=None, user_id=None):
        """
        ScheduledNotebookInputV1 - a model defined in Swagger
        """

        self._description = None
        self._enabled = None
        self._file_path = None
        self._label = None
        self._schedules = None
        self._timezone = None
        self._user_id = None

        if description is not None:
          self.description = description
        if enabled is not None:
          self.enabled = enabled
        if file_path is not None:
          self.file_path = file_path
        if label is not None:
          self.label = label
        if schedules is not None:
          self.schedules = schedules
        if timezone is not None:
          self.timezone = timezone
        if user_id is not None:
          self.user_id = user_id

    @property
    def description(self):
        """
        Gets the description of this ScheduledNotebookInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input

        :return: The description of this ScheduledNotebookInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduledNotebookInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input

        :param description: The description of this ScheduledNotebookInputV1.
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this ScheduledNotebookInputV1.
        Whether the schedule should be enabled to run jobs

        :return: The enabled of this ScheduledNotebookInputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ScheduledNotebookInputV1.
        Whether the schedule should be enabled to run jobs

        :param enabled: The enabled of this ScheduledNotebookInputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def file_path(self):
        """
        Gets the file_path of this ScheduledNotebookInputV1.
        The path to the ipynb file to be run (case-sensitive). May not be altered after initial creation

        :return: The file_path of this ScheduledNotebookInputV1.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path of this ScheduledNotebookInputV1.
        The path to the ipynb file to be run (case-sensitive). May not be altered after initial creation

        :param file_path: The file_path of this ScheduledNotebookInputV1.
        :type: str
        """
        if file_path is None:
            raise ValueError("Invalid value for `file_path`, must not be `None`")

        self._file_path = file_path

    @property
    def label(self):
        """
        Gets the label of this ScheduledNotebookInputV1.
        An optional label that differentiates this schedule (case-sensitive), allowing the samefilePath to be run by multiple users. May not be altered after initial creation

        :return: The label of this ScheduledNotebookInputV1.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ScheduledNotebookInputV1.
        An optional label that differentiates this schedule (case-sensitive), allowing the samefilePath to be run by multiple users. May not be altered after initial creation

        :param label: The label of this ScheduledNotebookInputV1.
        :type: str
        """

        self._label = label

    @property
    def schedules(self):
        """
        Gets the schedules of this ScheduledNotebookInputV1.
        The Notebook's run schedule.  Any entries for which a key is not provided will be supplied with a key from a 0-based list of integers

        :return: The schedules of this ScheduledNotebookInputV1.
        :rtype: list[ScheduleInputV1]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this ScheduledNotebookInputV1.
        The Notebook's run schedule.  Any entries for which a key is not provided will be supplied with a key from a 0-based list of integers

        :param schedules: The schedules of this ScheduledNotebookInputV1.
        :type: list[ScheduleInputV1]
        """

        self._schedules = schedules

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduledNotebookInputV1.
        The timezone in which the scheduled times will be run, defaults to UTC

        :return: The timezone of this ScheduledNotebookInputV1.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduledNotebookInputV1.
        The timezone in which the scheduled times will be run, defaults to UTC

        :param timezone: The timezone of this ScheduledNotebookInputV1.
        :type: str
        """

        self._timezone = timezone

    @property
    def user_id(self):
        """
        Gets the user_id of this ScheduledNotebookInputV1.
        The user ID to run the Notebook as, defaults to the current user if not specified. Only an admin user is allowed to specify a user ID

        :return: The user_id of this ScheduledNotebookInputV1.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ScheduledNotebookInputV1.
        The user ID to run the Notebook as, defaults to the current user if not specified. Only an admin user is allowed to specify a user ID

        :param user_id: The user_id of this ScheduledNotebookInputV1.
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, ScheduledNotebookInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
