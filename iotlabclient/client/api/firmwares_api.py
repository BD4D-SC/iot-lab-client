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


class FirmwaresApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def firmwares_get(self, **kwargs):  # noqa: E501
        """get a list of stored firmware metadatas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourceType type: Filter by type (userde
        :param ArchiString archi: Filter by archi
        :return: list[Firmware]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def firmwares_get_with_http_info(self, **kwargs):  # noqa: E501
        """get a list of stored firmware metadatas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResourceType type: Filter by type (userde
        :param ArchiString archi: Filter by archi
        :return: list[Firmware]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['type', 'archi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method firmwares_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'archi' in local_var_params:
            query_params.append(('archi', local_var_params['archi']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'list[Firmware]',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type='list[Firmware]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def firmwares_name_delete(self, name, **kwargs):  # noqa: E501
        """Delete a user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_name_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_name_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def firmwares_name_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete a user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_delete_with_http_info(name, async_req=True)
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
                    " to method firmwares_name_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `firmwares_name_delete`")  # noqa: E501

        if 'name' in local_var_params and not re.search(r'^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$', local_var_params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `firmwares_name_delete`, must conform to the pattern `/^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: '',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def firmwares_name_file_get(self, name, **kwargs):  # noqa: E501
        """get a stored firmaware file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_file_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_name_file_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_name_file_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def firmwares_name_file_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """get a stored firmaware file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_file_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: file
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
                    " to method firmwares_name_file_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `firmwares_name_file_get`")  # noqa: E501

        if 'name' in local_var_params and not re.search(r'^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$', local_var_params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `firmwares_name_file_get`, must conform to the pattern `/^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'file',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares/{name}/file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def firmwares_name_get(self, name, **kwargs):  # noqa: E501
        """get a stored firmware metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: Firmware
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def firmwares_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """get a stored firmware metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: Firmware
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
                    " to method firmwares_name_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `firmwares_name_get`")  # noqa: E501

        if 'name' in local_var_params and not re.search(r'^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$', local_var_params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `firmwares_name_get`, must conform to the pattern `/^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'Firmware',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type='Firmware',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def firmwares_name_put(self, name, **kwargs):  # noqa: E501
        """modify a stored user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_put(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param file firmware: firmware binary file
        :param Firmware metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_name_put_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_name_put_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def firmwares_name_put_with_http_info(self, name, **kwargs):  # noqa: E501
        """modify a stored user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_name_put_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param file firmware: firmware binary file
        :param Firmware metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'firmware', 'metadata']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method firmwares_name_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `firmwares_name_put`")  # noqa: E501

        if 'name' in local_var_params and not re.search(r'^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$', local_var_params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `firmwares_name_put`, must conform to the pattern `/^[0-9A-Za-z_-]+(\.[0-9A-Za-z_-]+)?$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'firmware' in local_var_params:
            local_var_files['firmware'] = local_var_params['firmware']  # noqa: E501
        if 'metadata' in local_var_params:
            form_params.append(('metadata', local_var_params['metadata']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: '',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def firmwares_post(self, **kwargs):  # noqa: E501
        """save a user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file firmware: firmware binary file
        :param Firmware metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.firmwares_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.firmwares_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def firmwares_post_with_http_info(self, **kwargs):  # noqa: E501
        """save a user firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.firmwares_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file firmware: firmware binary file
        :param Firmware metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['firmware', 'metadata']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method firmwares_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'firmware' in local_var_params:
            local_var_files['firmware'] = local_var_params['firmware']  # noqa: E501
        if 'metadata' in local_var_params:
            form_params.append(('metadata', local_var_params['metadata']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: '',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_firmware_format(self, **kwargs):  # noqa: E501
        """Returns firwmare format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firmware_format(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file firmware: firmware binary file
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_firmware_format_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_firmware_format_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_firmware_format_with_http_info(self, **kwargs):  # noqa: E501
        """Returns firwmare format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firmware_format_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file firmware: firmware binary file
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['firmware']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firmware_format" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'firmware' in local_var_params:
            local_var_files['firmware'] = local_var_params['firmware']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = ', '.join(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'InlineResponse2002',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/firmwares/checker', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types=response_types,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
