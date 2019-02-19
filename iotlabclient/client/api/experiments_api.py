# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from iotlabclient.client.api_client import ApiClient


class ExperimentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_experiments(self, **kwargs):  # noqa: E501
        """Returns experiments list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_experiments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: Filter with state
        :param int limit: Filter with number
        :param int offset: Filter with index
        :return: ExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_experiments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_experiments_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_experiments_with_http_info(self, **kwargs):  # noqa: E501
        """Returns experiments list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_experiments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: Filter with state
        :param int limit: Filter with number
        :param int offset: Filter with index
        :return: ExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['state', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_experiments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'ExperimentsResponse',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/experiments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='ExperimentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_experiments_total(self, **kwargs):  # noqa: E501
        """Returns total number of experiments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_experiments_total(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TotalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_experiments_total_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_experiments_total_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_experiments_total_with_http_info(self, **kwargs):  # noqa: E501
        """Returns total number of experiments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_experiments_total_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TotalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_experiments_total" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'TotalResponse',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/experiments/total', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='TotalResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_running_experiments(self, **kwargs):  # noqa: E501
        """Returns running testbed experiments list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_running_experiments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Filter with number
        :param int offset: Filter with index
        :return: ExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_running_experiments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_running_experiments_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_running_experiments_with_http_info(self, **kwargs):  # noqa: E501
        """Returns running testbed experiments list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_running_experiments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Filter with number
        :param int offset: Filter with index
        :return: ExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_running_experiments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'ExperimentsResponse',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/experiments/running', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='ExperimentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_experiment(self, **kwargs):  # noqa: E501
        """Submit an experiment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_experiment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExperimentRequest experiment:
        :param list[file] files: firmware/script/scriptconfig files
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.submit_experiment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.submit_experiment_with_http_info(**kwargs)  # noqa: E501
            return data

    def submit_experiment_with_http_info(self, **kwargs):  # noqa: E501
        """Submit an experiment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_experiment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExperimentRequest experiment:
        :param list[file] files: firmware/script/scriptconfig files
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['experiment', 'files']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_experiment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}
        if 'experiment' in local_var_params:
            form_params.append(('experiment', local_var_params['experiment']))
            post_content_types['experiment'] = 'application/json'
        if 'files' in local_var_params:
            local_var_files['files'] = local_var_params['files']  # noqa: E501
            collection_formats['files'] = 'csv' # noqa: E501 

        body_params = None


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/mixed'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'InlineResponse200',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/experiments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            multipart_header_params=multipart_header_params,
            post_content_types=post_content_types,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
