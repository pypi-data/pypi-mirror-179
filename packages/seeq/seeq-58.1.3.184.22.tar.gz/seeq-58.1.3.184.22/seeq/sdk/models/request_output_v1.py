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


class RequestOutputV1(object):
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
        'activities': 'list[ActivityOutputV1]',
        'activity_graph': 'ActivityGraphOutputV1',
        'detailed_meters': 'list[DetailedMeterOutputV1]',
        'detailed_timers': 'list[DetailedTimerOutputV1]',
        'flame_graph': 'FoldedStackNodeV1',
        'href': 'str',
        'parallelization_count': 'int',
        'parameters': 'dict(str, list[str])',
        'progress': 'ProgressInformationOutputV1',
        'request_method': 'str',
        'request_path': 'str',
        'run_duration': 'int',
        'user_email': 'str',
        'username': 'str'
    }

    attribute_map = {
        'activities': 'activities',
        'activity_graph': 'activityGraph',
        'detailed_meters': 'detailedMeters',
        'detailed_timers': 'detailedTimers',
        'flame_graph': 'flameGraph',
        'href': 'href',
        'parallelization_count': 'parallelizationCount',
        'parameters': 'parameters',
        'progress': 'progress',
        'request_method': 'requestMethod',
        'request_path': 'requestPath',
        'run_duration': 'runDuration',
        'user_email': 'userEmail',
        'username': 'username'
    }

    def __init__(self, activities=None, activity_graph=None, detailed_meters=None, detailed_timers=None, flame_graph=None, href=None, parallelization_count=None, parameters=None, progress=None, request_method=None, request_path=None, run_duration=None, user_email=None, username=None):
        """
        RequestOutputV1 - a model defined in Swagger
        """

        self._activities = None
        self._activity_graph = None
        self._detailed_meters = None
        self._detailed_timers = None
        self._flame_graph = None
        self._href = None
        self._parallelization_count = None
        self._parameters = None
        self._progress = None
        self._request_method = None
        self._request_path = None
        self._run_duration = None
        self._user_email = None
        self._username = None

        if activities is not None:
          self.activities = activities
        if activity_graph is not None:
          self.activity_graph = activity_graph
        if detailed_meters is not None:
          self.detailed_meters = detailed_meters
        if detailed_timers is not None:
          self.detailed_timers = detailed_timers
        if flame_graph is not None:
          self.flame_graph = flame_graph
        if href is not None:
          self.href = href
        if parallelization_count is not None:
          self.parallelization_count = parallelization_count
        if parameters is not None:
          self.parameters = parameters
        if progress is not None:
          self.progress = progress
        if request_method is not None:
          self.request_method = request_method
        if request_path is not None:
          self.request_path = request_path
        if run_duration is not None:
          self.run_duration = run_duration
        if user_email is not None:
          self.user_email = user_email
        if username is not None:
          self.username = username

    @property
    def activities(self):
        """
        Gets the activities of this RequestOutputV1.
        The current chain of activities for the request. The last activity in the list represents the current operation being performed.

        :return: The activities of this RequestOutputV1.
        :rtype: list[ActivityOutputV1]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """
        Sets the activities of this RequestOutputV1.
        The current chain of activities for the request. The last activity in the list represents the current operation being performed.

        :param activities: The activities of this RequestOutputV1.
        :type: list[ActivityOutputV1]
        """

        self._activities = activities

    @property
    def activity_graph(self):
        """
        Gets the activity_graph of this RequestOutputV1.

        :return: The activity_graph of this RequestOutputV1.
        :rtype: ActivityGraphOutputV1
        """
        return self._activity_graph

    @activity_graph.setter
    def activity_graph(self, activity_graph):
        """
        Sets the activity_graph of this RequestOutputV1.

        :param activity_graph: The activity_graph of this RequestOutputV1.
        :type: ActivityGraphOutputV1
        """

        self._activity_graph = activity_graph

    @property
    def detailed_meters(self):
        """
        Gets the detailed_meters of this RequestOutputV1.
        All metered items that are attributable to the processing of the request.

        :return: The detailed_meters of this RequestOutputV1.
        :rtype: list[DetailedMeterOutputV1]
        """
        return self._detailed_meters

    @detailed_meters.setter
    def detailed_meters(self, detailed_meters):
        """
        Sets the detailed_meters of this RequestOutputV1.
        All metered items that are attributable to the processing of the request.

        :param detailed_meters: The detailed_meters of this RequestOutputV1.
        :type: list[DetailedMeterOutputV1]
        """

        self._detailed_meters = detailed_meters

    @property
    def detailed_timers(self):
        """
        Gets the detailed_timers of this RequestOutputV1.
        All timed events that are attributable to the processing of the request.

        :return: The detailed_timers of this RequestOutputV1.
        :rtype: list[DetailedTimerOutputV1]
        """
        return self._detailed_timers

    @detailed_timers.setter
    def detailed_timers(self, detailed_timers):
        """
        Sets the detailed_timers of this RequestOutputV1.
        All timed events that are attributable to the processing of the request.

        :param detailed_timers: The detailed_timers of this RequestOutputV1.
        :type: list[DetailedTimerOutputV1]
        """

        self._detailed_timers = detailed_timers

    @property
    def flame_graph(self):
        """
        Gets the flame_graph of this RequestOutputV1.

        :return: The flame_graph of this RequestOutputV1.
        :rtype: FoldedStackNodeV1
        """
        return self._flame_graph

    @flame_graph.setter
    def flame_graph(self, flame_graph):
        """
        Sets the flame_graph of this RequestOutputV1.

        :param flame_graph: The flame_graph of this RequestOutputV1.
        :type: FoldedStackNodeV1
        """

        self._flame_graph = flame_graph

    @property
    def href(self):
        """
        Gets the href of this RequestOutputV1.
        The href that can be used to interact with the request

        :return: The href of this RequestOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this RequestOutputV1.
        The href that can be used to interact with the request

        :param href: The href of this RequestOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def parallelization_count(self):
        """
        Gets the parallelization_count of this RequestOutputV1.
        The number of threads working on this request

        :return: The parallelization_count of this RequestOutputV1.
        :rtype: int
        """
        return self._parallelization_count

    @parallelization_count.setter
    def parallelization_count(self, parallelization_count):
        """
        Sets the parallelization_count of this RequestOutputV1.
        The number of threads working on this request

        :param parallelization_count: The parallelization_count of this RequestOutputV1.
        :type: int
        """
        if parallelization_count is None:
            raise ValueError("Invalid value for `parallelization_count`, must not be `None`")

        self._parallelization_count = parallelization_count

    @property
    def parameters(self):
        """
        Gets the parameters of this RequestOutputV1.
        The list of HTTP parameters

        :return: The parameters of this RequestOutputV1.
        :rtype: dict(str, list[str])
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this RequestOutputV1.
        The list of HTTP parameters

        :param parameters: The parameters of this RequestOutputV1.
        :type: dict(str, list[str])
        """

        self._parameters = parameters

    @property
    def progress(self):
        """
        Gets the progress of this RequestOutputV1.

        :return: The progress of this RequestOutputV1.
        :rtype: ProgressInformationOutputV1
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this RequestOutputV1.

        :param progress: The progress of this RequestOutputV1.
        :type: ProgressInformationOutputV1
        """

        self._progress = progress

    @property
    def request_method(self):
        """
        Gets the request_method of this RequestOutputV1.
        The request method that this request was created for (GET, POST, DELETE)

        :return: The request_method of this RequestOutputV1.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """
        Sets the request_method of this RequestOutputV1.
        The request method that this request was created for (GET, POST, DELETE)

        :param request_method: The request_method of this RequestOutputV1.
        :type: str
        """
        if request_method is None:
            raise ValueError("Invalid value for `request_method`, must not be `None`")

        self._request_method = request_method

    @property
    def request_path(self):
        """
        Gets the request_path of this RequestOutputV1.
        The URI path that this request was created for

        :return: The request_path of this RequestOutputV1.
        :rtype: str
        """
        return self._request_path

    @request_path.setter
    def request_path(self, request_path):
        """
        Sets the request_path of this RequestOutputV1.
        The URI path that this request was created for

        :param request_path: The request_path of this RequestOutputV1.
        :type: str
        """
        if request_path is None:
            raise ValueError("Invalid value for `request_path`, must not be `None`")

        self._request_path = request_path

    @property
    def run_duration(self):
        """
        Gets the run_duration of this RequestOutputV1.
        The time (in nanoseconds) that this request has been running for

        :return: The run_duration of this RequestOutputV1.
        :rtype: int
        """
        return self._run_duration

    @run_duration.setter
    def run_duration(self, run_duration):
        """
        Sets the run_duration of this RequestOutputV1.
        The time (in nanoseconds) that this request has been running for

        :param run_duration: The run_duration of this RequestOutputV1.
        :type: int
        """
        if run_duration is None:
            raise ValueError("Invalid value for `run_duration`, must not be `None`")

        self._run_duration = run_duration

    @property
    def user_email(self):
        """
        Gets the user_email of this RequestOutputV1.
        The email of the user that created this request

        :return: The user_email of this RequestOutputV1.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """
        Sets the user_email of this RequestOutputV1.
        The email of the user that created this request

        :param user_email: The user_email of this RequestOutputV1.
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")

        self._user_email = user_email

    @property
    def username(self):
        """
        Gets the username of this RequestOutputV1.
        The username of the user that created this request

        :return: The username of this RequestOutputV1.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this RequestOutputV1.
        The username of the user that created this request

        :param username: The username of this RequestOutputV1.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

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
        if not isinstance(other, RequestOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
