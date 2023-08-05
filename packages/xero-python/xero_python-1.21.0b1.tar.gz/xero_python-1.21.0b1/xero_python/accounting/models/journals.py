# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Journals(BaseModel):
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
    openapi_types = {"journals": "list[Journal]"}

    attribute_map = {"journals": "Journals"}

    def __init__(self, journals=None):  # noqa: E501
        """Journals - a model defined in OpenAPI"""  # noqa: E501

        self._journals = None
        self.discriminator = None

        if journals is not None:
            self.journals = journals

    @property
    def journals(self):
        """Gets the journals of this Journals.  # noqa: E501


        :return: The journals of this Journals.  # noqa: E501
        :rtype: list[Journal]
        """
        return self._journals

    @journals.setter
    def journals(self, journals):
        """Sets the journals of this Journals.


        :param journals: The journals of this Journals.  # noqa: E501
        :type: list[Journal]
        """

        self._journals = journals
