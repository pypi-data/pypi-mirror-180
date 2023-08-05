# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_rpm.api_client import ApiClient
from pulpcore.client.pulp_rpm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RepositoriesRpmVersionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete(self, rpm_rpm_repository_version_href, **kwargs):  # noqa: E501
        """Delete a repository version  # noqa: E501

        Trigger an asynchronous task to delete a repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(rpm_rpm_repository_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_with_http_info(rpm_rpm_repository_version_href, **kwargs)  # noqa: E501

    def delete_with_http_info(self, rpm_rpm_repository_version_href, **kwargs):  # noqa: E501
        """Delete a repository version  # noqa: E501

        Trigger an asynchronous task to delete a repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(rpm_rpm_repository_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_rpm_repository_version_href'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_rpm_repository_version_href' is set
        if self.api_client.client_side_validation and ('rpm_rpm_repository_version_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_rpm_repository_version_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_rpm_repository_version_href` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_rpm_repository_version_href' in local_var_params:
            path_params['rpm_rpm_repository_version_href'] = local_var_params['rpm_rpm_repository_version_href']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_rpm_repository_version_href}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, rpm_rpm_repository_href, **kwargs):  # noqa: E501
        """List repository versions  # noqa: E501

        RpmRepositoryVersion represents a single rpm repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(rpm_rpm_repository_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_href: (required)
        :param str content: Content Unit referenced by HREF
        :param str content__in: Content Unit referenced by HREF
        :param int limit: Number of results to return per page.
        :param int number: Filter results where number matches value
        :param int number__gt: Filter results where number is greater than value
        :param int number__gte: Filter results where number is greater than or equal to value
        :param int number__lt: Filter results where number is less than value
        :param int number__lte: Filter results where number is less than or equal to value
        :param list[int] number__range: Filter results where number is between two comma separated values
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering
        :param datetime pulp_created: Filter results where pulp_created matches value
        :param datetime pulp_created__gt: Filter results where pulp_created is greater than value
        :param datetime pulp_created__gte: Filter results where pulp_created is greater than or equal to value
        :param datetime pulp_created__lt: Filter results where pulp_created is less than value
        :param datetime pulp_created__lte: Filter results where pulp_created is less than or equal to value
        :param list[datetime] pulp_created__range: Filter results where pulp_created is between two comma separated values
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedRepositoryVersionResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(rpm_rpm_repository_href, **kwargs)  # noqa: E501

    def list_with_http_info(self, rpm_rpm_repository_href, **kwargs):  # noqa: E501
        """List repository versions  # noqa: E501

        RpmRepositoryVersion represents a single rpm repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(rpm_rpm_repository_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_href: (required)
        :param str content: Content Unit referenced by HREF
        :param str content__in: Content Unit referenced by HREF
        :param int limit: Number of results to return per page.
        :param int number: Filter results where number matches value
        :param int number__gt: Filter results where number is greater than value
        :param int number__gte: Filter results where number is greater than or equal to value
        :param int number__lt: Filter results where number is less than value
        :param int number__lte: Filter results where number is less than or equal to value
        :param list[int] number__range: Filter results where number is between two comma separated values
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering
        :param datetime pulp_created: Filter results where pulp_created matches value
        :param datetime pulp_created__gt: Filter results where pulp_created is greater than value
        :param datetime pulp_created__gte: Filter results where pulp_created is greater than or equal to value
        :param datetime pulp_created__lt: Filter results where pulp_created is less than value
        :param datetime pulp_created__lte: Filter results where pulp_created is less than or equal to value
        :param list[datetime] pulp_created__range: Filter results where pulp_created is between two comma separated values
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedRepositoryVersionResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_rpm_repository_href',
            'content',
            'content__in',
            'limit',
            'number',
            'number__gt',
            'number__gte',
            'number__lt',
            'number__lte',
            'number__range',
            'offset',
            'ordering',
            'pulp_created',
            'pulp_created__gt',
            'pulp_created__gte',
            'pulp_created__lt',
            'pulp_created__lte',
            'pulp_created__range',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_rpm_repository_href' is set
        if self.api_client.client_side_validation and ('rpm_rpm_repository_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_rpm_repository_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_rpm_repository_href` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_rpm_repository_href' in local_var_params:
            path_params['rpm_rpm_repository_href'] = local_var_params['rpm_rpm_repository_href']  # noqa: E501

        query_params = []
        if 'content' in local_var_params and local_var_params['content'] is not None:  # noqa: E501
            query_params.append(('content', local_var_params['content']))  # noqa: E501
        if 'content__in' in local_var_params and local_var_params['content__in'] is not None:  # noqa: E501
            query_params.append(('content__in', local_var_params['content__in']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'number' in local_var_params and local_var_params['number'] is not None:  # noqa: E501
            query_params.append(('number', local_var_params['number']))  # noqa: E501
        if 'number__gt' in local_var_params and local_var_params['number__gt'] is not None:  # noqa: E501
            query_params.append(('number__gt', local_var_params['number__gt']))  # noqa: E501
        if 'number__gte' in local_var_params and local_var_params['number__gte'] is not None:  # noqa: E501
            query_params.append(('number__gte', local_var_params['number__gte']))  # noqa: E501
        if 'number__lt' in local_var_params and local_var_params['number__lt'] is not None:  # noqa: E501
            query_params.append(('number__lt', local_var_params['number__lt']))  # noqa: E501
        if 'number__lte' in local_var_params and local_var_params['number__lte'] is not None:  # noqa: E501
            query_params.append(('number__lte', local_var_params['number__lte']))  # noqa: E501
        if 'number__range' in local_var_params and local_var_params['number__range'] is not None:  # noqa: E501
            query_params.append(('number__range', local_var_params['number__range']))  # noqa: E501
            collection_formats['number__range'] = 'csv'  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
            collection_formats['ordering'] = 'csv'  # noqa: E501
        if 'pulp_created' in local_var_params and local_var_params['pulp_created'] is not None:  # noqa: E501
            query_params.append(('pulp_created', local_var_params['pulp_created']))  # noqa: E501
        if 'pulp_created__gt' in local_var_params and local_var_params['pulp_created__gt'] is not None:  # noqa: E501
            query_params.append(('pulp_created__gt', local_var_params['pulp_created__gt']))  # noqa: E501
        if 'pulp_created__gte' in local_var_params and local_var_params['pulp_created__gte'] is not None:  # noqa: E501
            query_params.append(('pulp_created__gte', local_var_params['pulp_created__gte']))  # noqa: E501
        if 'pulp_created__lt' in local_var_params and local_var_params['pulp_created__lt'] is not None:  # noqa: E501
            query_params.append(('pulp_created__lt', local_var_params['pulp_created__lt']))  # noqa: E501
        if 'pulp_created__lte' in local_var_params and local_var_params['pulp_created__lte'] is not None:  # noqa: E501
            query_params.append(('pulp_created__lte', local_var_params['pulp_created__lte']))  # noqa: E501
        if 'pulp_created__range' in local_var_params and local_var_params['pulp_created__range'] is not None:  # noqa: E501
            query_params.append(('pulp_created__range', local_var_params['pulp_created__range']))  # noqa: E501
            collection_formats['pulp_created__range'] = 'csv'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_rpm_repository_href}versions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedRepositoryVersionResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, rpm_rpm_repository_version_href, **kwargs):  # noqa: E501
        """Inspect a repository version  # noqa: E501

        RpmRepositoryVersion represents a single rpm repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(rpm_rpm_repository_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RepositoryVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(rpm_rpm_repository_version_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, rpm_rpm_repository_version_href, **kwargs):  # noqa: E501
        """Inspect a repository version  # noqa: E501

        RpmRepositoryVersion represents a single rpm repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(rpm_rpm_repository_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RepositoryVersionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_rpm_repository_version_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_rpm_repository_version_href' is set
        if self.api_client.client_side_validation and ('rpm_rpm_repository_version_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_rpm_repository_version_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_rpm_repository_version_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_rpm_repository_version_href' in local_var_params:
            path_params['rpm_rpm_repository_version_href'] = local_var_params['rpm_rpm_repository_version_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_rpm_repository_version_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoryVersionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repair(self, rpm_rpm_repository_version_href, repair, **kwargs):  # noqa: E501
        """repair  # noqa: E501

        Trigger an asynchronous task to repair a repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repair(rpm_rpm_repository_version_href, repair, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param Repair repair: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.repair_with_http_info(rpm_rpm_repository_version_href, repair, **kwargs)  # noqa: E501

    def repair_with_http_info(self, rpm_rpm_repository_version_href, repair, **kwargs):  # noqa: E501
        """repair  # noqa: E501

        Trigger an asynchronous task to repair a repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repair_with_http_info(rpm_rpm_repository_version_href, repair, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_rpm_repository_version_href: (required)
        :param Repair repair: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_rpm_repository_version_href',
            'repair'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repair" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_rpm_repository_version_href' is set
        if self.api_client.client_side_validation and ('rpm_rpm_repository_version_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_rpm_repository_version_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_rpm_repository_version_href` when calling `repair`")  # noqa: E501
        # verify the required parameter 'repair' is set
        if self.api_client.client_side_validation and ('repair' not in local_var_params or  # noqa: E501
                                                        local_var_params['repair'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `repair` when calling `repair`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_rpm_repository_version_href' in local_var_params:
            path_params['rpm_rpm_repository_version_href'] = local_var_params['rpm_rpm_repository_version_href']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'repair' in local_var_params:
            body_params = local_var_params['repair']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_rpm_repository_version_href}repair/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
