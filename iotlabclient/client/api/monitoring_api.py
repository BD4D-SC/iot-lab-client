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


class MonitoringApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_profile(self, name, **kwargs):  # noqa: E501
        """Delete monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_profile(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_profile_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_profile_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def delete_profile_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_profile_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

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
            204: '',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/monitoring/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_profile(self, name, **kwargs):  # noqa: E501
        """Returns monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profile(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: Profile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_profile_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_profile_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_profile_with_http_info(self, name, **kwargs):  # noqa: E501
        """Returns monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profile_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: Profile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

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
            200: 'Profile',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/monitoring/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='Profile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_profiles(self, **kwargs):  # noqa: E501
        """Returns monitoring profiles list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str archi: Filter by archi
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_profiles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_profiles_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_profiles_with_http_info(self, **kwargs):  # noqa: E501
        """Returns monitoring profiles list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str archi: Filter by archi
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['archi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_profiles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'archi' in local_var_params:
            query_params.append(('archi', local_var_params['archi']))  # noqa: E501

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
            200: 'list[Profile]',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/monitoring', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='list[Profile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_profile(self, name, **kwargs):  # noqa: E501
        """Modify monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_profile(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param Profile profile:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_profile_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_profile_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def modify_profile_with_http_info(self, name, **kwargs):  # noqa: E501
        """Modify monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_profile_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param Profile profile:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'profile']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `modify_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        if 'profile' in local_var_params:
            body_params = local_var_params['profile']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            204: '',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/monitoring/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_profile(self, **kwargs):  # noqa: E501
        """Create monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_profile(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Profile profile:
        :return: Profile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_profile_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_profile_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_profile_with_http_info(self, **kwargs):  # noqa: E501
        """Create monitoring profile.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_profile_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Profile profile:
        :return: Profile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['profile']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_profile" % key
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
        if 'profile' in local_var_params:
            body_params = local_var_params['profile']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'Profile',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/monitoring', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            post_content_types=post_content_types,
            response_type='Profile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
