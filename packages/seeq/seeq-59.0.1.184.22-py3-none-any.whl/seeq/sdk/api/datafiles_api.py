# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 59.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from ..models import *

class DatafilesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def archive_datafile(self, **kwargs):
        """
        Archive a datafile and all of its signals
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_datafile(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile to archive (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.archive_datafile_with_http_info(**kwargs)
        else:
            (data) = self.archive_datafile_with_http_info(**kwargs)
            return data

    def archive_datafile_with_http_info(self, **kwargs):
        """
        Archive a datafile and all of its signals
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_datafile_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile to archive (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_datafile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `archive_datafile`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'StatusMessageBase'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_datafile(self, **kwargs):
        """
        Create a datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_datafile(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DatafileInputV1 body: Datafile information (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_datafile_with_http_info(**kwargs)
        else:
            (data) = self.create_datafile_with_http_info(**kwargs)
            return data

    def create_datafile_with_http_info(self, **kwargs):
        """
        Create a datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_datafile_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DatafileInputV1 body: Datafile information (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_datafile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_datafile`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DatafileOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_datafile(self, **kwargs):
        """
        Get a Datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_datafile(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile to retrieve (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_datafile_with_http_info(**kwargs)
        else:
            (data) = self.get_datafile_with_http_info(**kwargs)
            return data

    def get_datafile_with_http_info(self, **kwargs):
        """
        Get a Datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_datafile_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile to retrieve (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datafile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_datafile`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DatafileOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_datafiles(self, **kwargs):
        """
        Get a collection of datafiles
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_datafiles(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: ItemPreviewListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ItemPreviewListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_datafiles_with_http_info(**kwargs)
        else:
            (data) = self.get_datafiles_with_http_info(**kwargs)
            return data

    def get_datafiles_with_http_info(self, **kwargs):
        """
        Get a collection of datafiles
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_datafiles_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: ItemPreviewListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ItemPreviewListV1
        """

        all_params = ['offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datafiles" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ItemPreviewListV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_items_hosted_by_datafile(self, **kwargs):
        """
        Get a list of the items hosted by this datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_items_hosted_by_datafile(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile (required)
        :param str data_id: The dataId for a specific hosted item
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: ItemPreviewListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ItemPreviewListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_items_hosted_by_datafile_with_http_info(**kwargs)
        else:
            (data) = self.get_items_hosted_by_datafile_with_http_info(**kwargs)
            return data

    def get_items_hosted_by_datafile_with_http_info(self, **kwargs):
        """
        Get a list of the items hosted by this datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_items_hosted_by_datafile_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the datafile (required)
        :param str data_id: The dataId for a specific hosted item
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: ItemPreviewListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ItemPreviewListV1
        """

        all_params = ['id', 'data_id', 'offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_items_hosted_by_datafile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_items_hosted_by_datafile`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'data_id' in params:
            query_params.append(('dataId', params['data_id']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles/{id}/items', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ItemPreviewListV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def import_csv(self, **kwargs):
        """
        Import a CSV file that can be used to create or update a Datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_csv(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file:
        :return: CsvDatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CsvDatafileOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_csv_with_http_info(**kwargs)
        else:
            (data) = self.import_csv_with_http_info(**kwargs)
            return data

    def import_csv_with_http_info(self, **kwargs):
        """
        Import a CSV file that can be used to create or update a Datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_csv_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file:
        :return: CsvDatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CsvDatafileOutputV1
        """

        all_params = ['file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_csv" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles/csv', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'CsvDatafileOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_datafile(self, **kwargs):
        """
        Update a datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_datafile(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DatafileInputV1 body: Datafile information (required)
        :param str id: ID of the datafile to retrieve (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_datafile_with_http_info(**kwargs)
        else:
            (data) = self.update_datafile_with_http_info(**kwargs)
            return data

    def update_datafile_with_http_info(self, **kwargs):
        """
        Update a datafile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_datafile_with_http_info(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DatafileInputV1 body: Datafile information (required)
        :param str id: ID of the datafile to retrieve (required)
        :return: DatafileOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DatafileOutputV1
        """

        all_params = ['body', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_datafile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_datafile`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_datafile`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/datafiles/{id}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DatafileOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
