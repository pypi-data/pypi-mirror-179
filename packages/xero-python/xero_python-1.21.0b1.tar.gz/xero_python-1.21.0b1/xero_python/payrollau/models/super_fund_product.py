# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperFundProduct(BaseModel):
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
    openapi_types = {"abn": "str", "usi": "str", "spin": "str", "product_name": "str"}

    attribute_map = {
        "abn": "ABN",
        "usi": "USI",
        "spin": "SPIN",
        "product_name": "ProductName",
    }

    def __init__(self, abn=None, usi=None, spin=None, product_name=None):  # noqa: E501
        """SuperFundProduct - a model defined in OpenAPI"""  # noqa: E501

        self._abn = None
        self._usi = None
        self._spin = None
        self._product_name = None
        self.discriminator = None

        if abn is not None:
            self.abn = abn
        if usi is not None:
            self.usi = usi
        if spin is not None:
            self.spin = spin
        if product_name is not None:
            self.product_name = product_name

    @property
    def abn(self):
        """Gets the abn of this SuperFundProduct.  # noqa: E501

        The ABN of the Regulated SuperFund  # noqa: E501

        :return: The abn of this SuperFundProduct.  # noqa: E501
        :rtype: str
        """
        return self._abn

    @abn.setter
    def abn(self, abn):
        """Sets the abn of this SuperFundProduct.

        The ABN of the Regulated SuperFund  # noqa: E501

        :param abn: The abn of this SuperFundProduct.  # noqa: E501
        :type: str
        """

        self._abn = abn

    @property
    def usi(self):
        """Gets the usi of this SuperFundProduct.  # noqa: E501

        The USI of the Regulated SuperFund  # noqa: E501

        :return: The usi of this SuperFundProduct.  # noqa: E501
        :rtype: str
        """
        return self._usi

    @usi.setter
    def usi(self, usi):
        """Sets the usi of this SuperFundProduct.

        The USI of the Regulated SuperFund  # noqa: E501

        :param usi: The usi of this SuperFundProduct.  # noqa: E501
        :type: str
        """

        self._usi = usi

    @property
    def spin(self):
        """Gets the spin of this SuperFundProduct.  # noqa: E501

        The SPIN of the Regulated SuperFund. This field has been deprecated. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN  # noqa: E501

        :return: The spin of this SuperFundProduct.  # noqa: E501
        :rtype: str
        """
        return self._spin

    @spin.setter
    def spin(self, spin):
        """Sets the spin of this SuperFundProduct.

        The SPIN of the Regulated SuperFund. This field has been deprecated. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN  # noqa: E501

        :param spin: The spin of this SuperFundProduct.  # noqa: E501
        :type: str
        """

        self._spin = spin

    @property
    def product_name(self):
        """Gets the product_name of this SuperFundProduct.  # noqa: E501

        The name of the Regulated SuperFund  # noqa: E501

        :return: The product_name of this SuperFundProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SuperFundProduct.

        The name of the Regulated SuperFund  # noqa: E501

        :param product_name: The product_name of this SuperFundProduct.  # noqa: E501
        :type: str
        """

        self._product_name = product_name
