# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayslipObject(BaseModel):
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
    openapi_types = {"payslip": "Payslip"}

    attribute_map = {"payslip": "Payslip"}

    def __init__(self, payslip=None):  # noqa: E501
        """PayslipObject - a model defined in OpenAPI"""  # noqa: E501

        self._payslip = None
        self.discriminator = None

        if payslip is not None:
            self.payslip = payslip

    @property
    def payslip(self):
        """Gets the payslip of this PayslipObject.  # noqa: E501


        :return: The payslip of this PayslipObject.  # noqa: E501
        :rtype: Payslip
        """
        return self._payslip

    @payslip.setter
    def payslip(self, payslip):
        """Sets the payslip of this PayslipObject.


        :param payslip: The payslip of this PayslipObject.  # noqa: E501
        :type: Payslip
        """

        self._payslip = payslip
