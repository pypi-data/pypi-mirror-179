# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class OnlineInvoices(BaseModel):
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
    openapi_types = {"online_invoices": "list[OnlineInvoice]"}

    attribute_map = {"online_invoices": "OnlineInvoices"}

    def __init__(self, online_invoices=None):  # noqa: E501
        """OnlineInvoices - a model defined in OpenAPI"""  # noqa: E501

        self._online_invoices = None
        self.discriminator = None

        if online_invoices is not None:
            self.online_invoices = online_invoices

    @property
    def online_invoices(self):
        """Gets the online_invoices of this OnlineInvoices.  # noqa: E501


        :return: The online_invoices of this OnlineInvoices.  # noqa: E501
        :rtype: list[OnlineInvoice]
        """
        return self._online_invoices

    @online_invoices.setter
    def online_invoices(self, online_invoices):
        """Sets the online_invoices of this OnlineInvoices.


        :param online_invoices: The online_invoices of this OnlineInvoices.  # noqa: E501
        :type: list[OnlineInvoice]
        """

        self._online_invoices = online_invoices
