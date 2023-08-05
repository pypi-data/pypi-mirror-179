# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ValidationError(BaseModel):
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
    openapi_types = {"message": "str"}

    attribute_map = {"message": "Message"}

    def __init__(self, message=None):  # noqa: E501
        """ValidationError - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self.discriminator = None

        if message is not None:
            self.message = message

    @property
    def message(self):
        """Gets the message of this ValidationError.  # noqa: E501

        Validation error message  # noqa: E501

        :return: The message of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationError.

        Validation error message  # noqa: E501

        :param message: The message of this ValidationError.  # noqa: E501
        :type: str
        """

        self._message = message
