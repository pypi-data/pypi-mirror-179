# coding: utf-8

"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    OpenAPI spec version: 2.0.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiException(OpenApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        self._status = status
        self._reason = reason
        self.http_resp = http_resp

    @property
    def status(self):
        return self._status or getattr(self.http_resp, "status", None)

    @property
    def reason(self):
        return self._reason or getattr(self.http_resp, "reason", None)

    @property
    def body(self):
        return getattr(self.http_resp, "data", None)

    @property
    def headers(self):
        return self.http_resp.getheaders() if self.http_resp else None

    @property
    def error_message(self):
        return "({0})\n" "Reason: {1}".format(self.status, self.reason)

    def __str__(self):
        """Custom error messages for exception"""
        error_message = self.error_message + "\n"
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class ApiSSLException(ApiException):
    """Exception in case there is SSL related error"""


class OAuth2Error(OpenApiException):
    """The base exception class for all OAuth2 exception"""


# import all HTTP status exceptions
from .http_status_exceptions import *  # noqa


class AccessTokenExpiredError(OAuth2Error):
    """
    Exception for invalid access token
    """


class OAuth2TokenGetterError(OAuth2Error):
    """
    Exception for invalid oauth2 token getter function
    """


class OAuth2TokenSaverError(OAuth2Error):
    """
    Exception for invalid oauth2 token saver function
    """


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        """Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
