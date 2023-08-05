# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ImportSummary(BaseModel):
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
    openapi_types = {
        "accounts": "ImportSummaryAccounts",
        "organisation": "ImportSummaryOrganisation",
    }

    attribute_map = {"accounts": "Accounts", "organisation": "Organisation"}

    def __init__(self, accounts=None, organisation=None):  # noqa: E501
        """ImportSummary - a model defined in OpenAPI"""  # noqa: E501

        self._accounts = None
        self._organisation = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if organisation is not None:
            self.organisation = organisation

    @property
    def accounts(self):
        """Gets the accounts of this ImportSummary.  # noqa: E501


        :return: The accounts of this ImportSummary.  # noqa: E501
        :rtype: ImportSummaryAccounts
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this ImportSummary.


        :param accounts: The accounts of this ImportSummary.  # noqa: E501
        :type: ImportSummaryAccounts
        """

        self._accounts = accounts

    @property
    def organisation(self):
        """Gets the organisation of this ImportSummary.  # noqa: E501


        :return: The organisation of this ImportSummary.  # noqa: E501
        :rtype: ImportSummaryOrganisation
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this ImportSummary.


        :param organisation: The organisation of this ImportSummary.  # noqa: E501
        :type: ImportSummaryOrganisation
        """

        self._organisation = organisation
