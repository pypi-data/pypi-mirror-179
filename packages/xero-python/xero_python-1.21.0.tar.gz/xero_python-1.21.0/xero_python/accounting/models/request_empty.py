# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class RequestEmpty(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"status": "str"}

    attribute_map = {"status": "Status"}

    def __init__(self, status=None):  # noqa: E501
        """RequestEmpty - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        """Gets the status of this RequestEmpty.  # noqa: E501

        Need at least one field to create an empty JSON payload  # noqa: E501

        :return: The status of this RequestEmpty.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestEmpty.

        Need at least one field to create an empty JSON payload  # noqa: E501

        :param status: The status of this RequestEmpty.  # noqa: E501
        :type: str
        """

        self._status = status
