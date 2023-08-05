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


class ChannelOutputV1(object):
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
        'created_at': 'str',
        'id': 'str',
        'last_published_at': 'str',
        'published_count': 'int',
        'subscriptions': 'list[SubscriptionOutputV1]',
        'type': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'last_published_at': 'lastPublishedAt',
        'published_count': 'publishedCount',
        'subscriptions': 'subscriptions',
        'type': 'type'
    }

    def __init__(self, created_at=None, id=None, last_published_at=None, published_count=None, subscriptions=None, type=None):
        """
        ChannelOutputV1 - a model defined in Swagger
        """

        self._created_at = None
        self._id = None
        self._last_published_at = None
        self._published_count = None
        self._subscriptions = None
        self._type = None

        if created_at is not None:
          self.created_at = created_at
        if id is not None:
          self.id = id
        if last_published_at is not None:
          self.last_published_at = last_published_at
        if published_count is not None:
          self.published_count = published_count
        if subscriptions is not None:
          self.subscriptions = subscriptions
        if type is not None:
          self.type = type

    @property
    def created_at(self):
        """
        Gets the created_at of this ChannelOutputV1.
        The time, as an ISO timestamp, that the channel was created

        :return: The created_at of this ChannelOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ChannelOutputV1.
        The time, as an ISO timestamp, that the channel was created

        :param created_at: The created_at of this ChannelOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """
        Gets the id of this ChannelOutputV1.
        The URI that uniquely identifies the channel

        :return: The id of this ChannelOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ChannelOutputV1.
        The URI that uniquely identifies the channel

        :param id: The id of this ChannelOutputV1.
        :type: str
        """

        self._id = id

    @property
    def last_published_at(self):
        """
        Gets the last_published_at of this ChannelOutputV1.
        The time, as an ISO timestamp, that the most recent message was published

        :return: The last_published_at of this ChannelOutputV1.
        :rtype: str
        """
        return self._last_published_at

    @last_published_at.setter
    def last_published_at(self, last_published_at):
        """
        Sets the last_published_at of this ChannelOutputV1.
        The time, as an ISO timestamp, that the most recent message was published

        :param last_published_at: The last_published_at of this ChannelOutputV1.
        :type: str
        """

        self._last_published_at = last_published_at

    @property
    def published_count(self):
        """
        Gets the published_count of this ChannelOutputV1.
        The number of messages published on the channel

        :return: The published_count of this ChannelOutputV1.
        :rtype: int
        """
        return self._published_count

    @published_count.setter
    def published_count(self, published_count):
        """
        Sets the published_count of this ChannelOutputV1.
        The number of messages published on the channel

        :param published_count: The published_count of this ChannelOutputV1.
        :type: int
        """

        self._published_count = published_count

    @property
    def subscriptions(self):
        """
        Gets the subscriptions of this ChannelOutputV1.
        The list of subscriptions

        :return: The subscriptions of this ChannelOutputV1.
        :rtype: list[SubscriptionOutputV1]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """
        Sets the subscriptions of this ChannelOutputV1.
        The list of subscriptions

        :param subscriptions: The subscriptions of this ChannelOutputV1.
        :type: list[SubscriptionOutputV1]
        """

        self._subscriptions = subscriptions

    @property
    def type(self):
        """
        Gets the type of this ChannelOutputV1.
        The type of channel this is

        :return: The type of this ChannelOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ChannelOutputV1.
        The type of channel this is

        :param type: The type of this ChannelOutputV1.
        :type: str
        """

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
        if not isinstance(other, ChannelOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
