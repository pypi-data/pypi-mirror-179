# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PaymentDelete(BaseModel):
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

    def __init__(self, status="DELETED"):  # noqa: E501
        """PaymentDelete - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self.discriminator = None

        self.status = status

    @property
    def status(self):
        """Gets the status of this PaymentDelete.  # noqa: E501

        The status of the payment.  # noqa: E501

        :return: The status of this PaymentDelete.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentDelete.

        The status of the payment.  # noqa: E501

        :param status: The status of this PaymentDelete.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError(
                "Invalid value for `status`, must not be `None`"
            )  # noqa: E501

        self._status = status
