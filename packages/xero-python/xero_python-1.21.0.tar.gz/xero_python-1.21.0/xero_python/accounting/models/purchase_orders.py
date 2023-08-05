# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PurchaseOrders(BaseModel):
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
    openapi_types = {"purchase_orders": "list[PurchaseOrder]"}

    attribute_map = {"purchase_orders": "PurchaseOrders"}

    def __init__(self, purchase_orders=None):  # noqa: E501
        """PurchaseOrders - a model defined in OpenAPI"""  # noqa: E501

        self._purchase_orders = None
        self.discriminator = None

        if purchase_orders is not None:
            self.purchase_orders = purchase_orders

    @property
    def purchase_orders(self):
        """Gets the purchase_orders of this PurchaseOrders.  # noqa: E501


        :return: The purchase_orders of this PurchaseOrders.  # noqa: E501
        :rtype: list[PurchaseOrder]
        """
        return self._purchase_orders

    @purchase_orders.setter
    def purchase_orders(self, purchase_orders):
        """Sets the purchase_orders of this PurchaseOrders.


        :param purchase_orders: The purchase_orders of this PurchaseOrders.  # noqa: E501
        :type: list[PurchaseOrder]
        """

        self._purchase_orders = purchase_orders
