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


class ScheduledNotebookOutputV1(object):
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
        'average_run_time': 'int',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'enabled': 'bool',
        'file_path': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'label': 'str',
        'name': 'str',
        'project': 'ItemPreviewV1',
        'run_user': 'IdentityPreviewV1',
        'schedules': 'list[ScheduleOutputV1]',
        'status_message': 'str',
        'timezone': 'str',
        'total_run_time': 'int',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'average_run_time': 'averageRunTime',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'enabled': 'enabled',
        'file_path': 'filePath',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'label': 'label',
        'name': 'name',
        'project': 'project',
        'run_user': 'runUser',
        'schedules': 'schedules',
        'status_message': 'statusMessage',
        'timezone': 'timezone',
        'total_run_time': 'totalRunTime',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, average_run_time=None, description=None, effective_permissions=None, enabled=True, file_path=None, id=None, is_archived=False, is_redacted=False, label=None, name=None, project=None, run_user=None, schedules=None, status_message=None, timezone=None, total_run_time=None, translation_key=None, type=None):
        """
        ScheduledNotebookOutputV1 - a model defined in Swagger
        """

        self._average_run_time = None
        self._description = None
        self._effective_permissions = None
        self._enabled = None
        self._file_path = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._label = None
        self._name = None
        self._project = None
        self._run_user = None
        self._schedules = None
        self._status_message = None
        self._timezone = None
        self._total_run_time = None
        self._translation_key = None
        self._type = None

        if average_run_time is not None:
          self.average_run_time = average_run_time
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if enabled is not None:
          self.enabled = enabled
        if file_path is not None:
          self.file_path = file_path
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if label is not None:
          self.label = label
        if name is not None:
          self.name = name
        if project is not None:
          self.project = project
        if run_user is not None:
          self.run_user = run_user
        if schedules is not None:
          self.schedules = schedules
        if status_message is not None:
          self.status_message = status_message
        if timezone is not None:
          self.timezone = timezone
        if total_run_time is not None:
          self.total_run_time = total_run_time
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def average_run_time(self):
        """
        Gets the average_run_time of this ScheduledNotebookOutputV1.
        The average run time of the Notebook, in ms

        :return: The average_run_time of this ScheduledNotebookOutputV1.
        :rtype: int
        """
        return self._average_run_time

    @average_run_time.setter
    def average_run_time(self, average_run_time):
        """
        Sets the average_run_time of this ScheduledNotebookOutputV1.
        The average run time of the Notebook, in ms

        :param average_run_time: The average_run_time of this ScheduledNotebookOutputV1.
        :type: int
        """

        self._average_run_time = average_run_time

    @property
    def description(self):
        """
        Gets the description of this ScheduledNotebookOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduledNotebookOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this ScheduledNotebookOutputV1.

        :return: The effective_permissions of this ScheduledNotebookOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this ScheduledNotebookOutputV1.

        :param effective_permissions: The effective_permissions of this ScheduledNotebookOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def enabled(self):
        """
        Gets the enabled of this ScheduledNotebookOutputV1.
        Whether the schedule is enabled to run jobs

        :return: The enabled of this ScheduledNotebookOutputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ScheduledNotebookOutputV1.
        Whether the schedule is enabled to run jobs

        :param enabled: The enabled of this ScheduledNotebookOutputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def file_path(self):
        """
        Gets the file_path of this ScheduledNotebookOutputV1.
        The path to the ipynb file to be run

        :return: The file_path of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path of this ScheduledNotebookOutputV1.
        The path to the ipynb file to be run

        :param file_path: The file_path of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._file_path = file_path

    @property
    def id(self):
        """
        Gets the id of this ScheduledNotebookOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledNotebookOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ScheduledNotebookOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ScheduledNotebookOutputV1.
        Whether item is archived

        :return: The is_archived of this ScheduledNotebookOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ScheduledNotebookOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this ScheduledNotebookOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this ScheduledNotebookOutputV1.
        Whether item is redacted

        :return: The is_redacted of this ScheduledNotebookOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this ScheduledNotebookOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this ScheduledNotebookOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def label(self):
        """
        Gets the label of this ScheduledNotebookOutputV1.
        The label to distinguish different schedules of a given Notebook filePath

        :return: The label of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ScheduledNotebookOutputV1.
        The label to distinguish different schedules of a given Notebook filePath

        :param label: The label of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this ScheduledNotebookOutputV1.
        The human readable name

        :return: The name of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScheduledNotebookOutputV1.
        The human readable name

        :param name: The name of this ScheduledNotebookOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def project(self):
        """
        Gets the project of this ScheduledNotebookOutputV1.

        :return: The project of this ScheduledNotebookOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this ScheduledNotebookOutputV1.

        :param project: The project of this ScheduledNotebookOutputV1.
        :type: ItemPreviewV1
        """

        self._project = project

    @property
    def run_user(self):
        """
        Gets the run_user of this ScheduledNotebookOutputV1.

        :return: The run_user of this ScheduledNotebookOutputV1.
        :rtype: IdentityPreviewV1
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        """
        Sets the run_user of this ScheduledNotebookOutputV1.

        :param run_user: The run_user of this ScheduledNotebookOutputV1.
        :type: IdentityPreviewV1
        """

        self._run_user = run_user

    @property
    def schedules(self):
        """
        Gets the schedules of this ScheduledNotebookOutputV1.
        The run schedule for the Notebook-label combination

        :return: The schedules of this ScheduledNotebookOutputV1.
        :rtype: list[ScheduleOutputV1]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this ScheduledNotebookOutputV1.
        The run schedule for the Notebook-label combination

        :param schedules: The schedules of this ScheduledNotebookOutputV1.
        :type: list[ScheduleOutputV1]
        """

        self._schedules = schedules

    @property
    def status_message(self):
        """
        Gets the status_message of this ScheduledNotebookOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ScheduledNotebookOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduledNotebookOutputV1.
        The timezone in which the schedule will be run

        :return: The timezone of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduledNotebookOutputV1.
        The timezone in which the schedule will be run

        :param timezone: The timezone of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._timezone = timezone

    @property
    def total_run_time(self):
        """
        Gets the total_run_time of this ScheduledNotebookOutputV1.
        The total run time of the Notebook, in ms

        :return: The total_run_time of this ScheduledNotebookOutputV1.
        :rtype: int
        """
        return self._total_run_time

    @total_run_time.setter
    def total_run_time(self, total_run_time):
        """
        Sets the total_run_time of this ScheduledNotebookOutputV1.
        The total run time of the Notebook, in ms

        :param total_run_time: The total_run_time of this ScheduledNotebookOutputV1.
        :type: int
        """

        self._total_run_time = total_run_time

    @property
    def translation_key(self):
        """
        Gets the translation_key of this ScheduledNotebookOutputV1.
        The item's translation key, if any

        :return: The translation_key of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this ScheduledNotebookOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this ScheduledNotebookOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this ScheduledNotebookOutputV1.
        The type of the item

        :return: The type of this ScheduledNotebookOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ScheduledNotebookOutputV1.
        The type of the item

        :param type: The type of this ScheduledNotebookOutputV1.
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
        if not isinstance(other, ScheduledNotebookOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
