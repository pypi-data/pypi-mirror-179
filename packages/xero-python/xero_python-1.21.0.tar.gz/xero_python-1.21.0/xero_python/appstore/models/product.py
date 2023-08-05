# coding: utf-8

"""
    Xero AppStore API

    These endpoints are for Xero Partners to interact with the App Store Billing platform  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Product(BaseModel):
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
        "id": "str",
        "name": "str",
        "seat_unit": "str",
        "type": "str",
        "usage_unit": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "seat_unit": "seatUnit",
        "type": "type",
        "usage_unit": "usageUnit",
    }

    def __init__(
        self, id=None, name=None, seat_unit=None, type=None, usage_unit=None
    ):  # noqa: E501
        """Product - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._seat_unit = None
        self._type = None
        self._usage_unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if seat_unit is not None:
            self.seat_unit = seat_unit
        if type is not None:
            self.type = type
        if usage_unit is not None:
            self.usage_unit = usage_unit

    @property
    def id(self):
        """Gets the id of this Product.  # noqa: E501

        The unique identifier for the product  # noqa: E501

        :return: The id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Product.

        The unique identifier for the product  # noqa: E501

        :param id: The id of this Product.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501

        The name of the product  # noqa: E501

        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        The name of the product  # noqa: E501

        :param name: The name of this Product.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def seat_unit(self):
        """Gets the seat_unit of this Product.  # noqa: E501

        The unit of the per seat product. e.g. \"user\", \"organisation\", \"SMS\", etc  # noqa: E501

        :return: The seat_unit of this Product.  # noqa: E501
        :rtype: str
        """
        return self._seat_unit

    @seat_unit.setter
    def seat_unit(self, seat_unit):
        """Sets the seat_unit of this Product.

        The unit of the per seat product. e.g. \"user\", \"organisation\", \"SMS\", etc  # noqa: E501

        :param seat_unit: The seat_unit of this Product.  # noqa: E501
        :type: str
        """

        self._seat_unit = seat_unit

    @property
    def type(self):
        """Gets the type of this Product.  # noqa: E501

        The pricing model of the product: * FIXED: Customers are charged a fixed amount for each billing period * PER_SEAT: Customers are charged based on the number of units they purchase * METERED: Customers are charged per use of this product   # noqa: E501

        :return: The type of this Product.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Product.

        The pricing model of the product: * FIXED: Customers are charged a fixed amount for each billing period * PER_SEAT: Customers are charged based on the number of units they purchase * METERED: Customers are charged per use of this product   # noqa: E501

        :param type: The type of this Product.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIXED", "PER_SEAT", "METERED", "None"]  # noqa: E501

        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                        type, allowed_values
                    )
                )

        self._type = type

    @property
    def usage_unit(self):
        """Gets the usage_unit of this Product.  # noqa: E501

        The unit of the usage product. e.g. \"user\", \"minutes\", \"SMS\", etc  # noqa: E501

        :return: The usage_unit of this Product.  # noqa: E501
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """Sets the usage_unit of this Product.

        The unit of the usage product. e.g. \"user\", \"minutes\", \"SMS\", etc  # noqa: E501

        :param usage_unit: The usage_unit of this Product.  # noqa: E501
        :type: str
        """

        self._usage_unit = usage_unit
