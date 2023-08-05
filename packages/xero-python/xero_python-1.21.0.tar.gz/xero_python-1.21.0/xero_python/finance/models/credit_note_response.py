# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CreditNoteResponse(BaseModel):
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
        "credit_note_id": "str",
        "contact": "ContactResponse",
        "total": "float",
        "line_items": "list[LineItemResponse]",
    }

    attribute_map = {
        "credit_note_id": "creditNoteId",
        "contact": "contact",
        "total": "total",
        "line_items": "lineItems",
    }

    def __init__(
        self, credit_note_id=None, contact=None, total=None, line_items=None
    ):  # noqa: E501
        """CreditNoteResponse - a model defined in OpenAPI"""  # noqa: E501

        self._credit_note_id = None
        self._contact = None
        self._total = None
        self._line_items = None
        self.discriminator = None

        if credit_note_id is not None:
            self.credit_note_id = credit_note_id
        if contact is not None:
            self.contact = contact
        if total is not None:
            self.total = total
        if line_items is not None:
            self.line_items = line_items

    @property
    def credit_note_id(self):
        """Gets the credit_note_id of this CreditNoteResponse.  # noqa: E501

        Xero Identifier of credit note  # noqa: E501

        :return: The credit_note_id of this CreditNoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, credit_note_id):
        """Sets the credit_note_id of this CreditNoteResponse.

        Xero Identifier of credit note  # noqa: E501

        :param credit_note_id: The credit_note_id of this CreditNoteResponse.  # noqa: E501
        :type: str
        """

        self._credit_note_id = credit_note_id

    @property
    def contact(self):
        """Gets the contact of this CreditNoteResponse.  # noqa: E501


        :return: The contact of this CreditNoteResponse.  # noqa: E501
        :rtype: ContactResponse
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CreditNoteResponse.


        :param contact: The contact of this CreditNoteResponse.  # noqa: E501
        :type: ContactResponse
        """

        self._contact = contact

    @property
    def total(self):
        """Gets the total of this CreditNoteResponse.  # noqa: E501

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode  # noqa: E501

        :return: The total of this CreditNoteResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CreditNoteResponse.

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode  # noqa: E501

        :param total: The total of this CreditNoteResponse.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def line_items(self):
        """Gets the line_items of this CreditNoteResponse.  # noqa: E501

        Not included in summary mode  # noqa: E501

        :return: The line_items of this CreditNoteResponse.  # noqa: E501
        :rtype: list[LineItemResponse]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this CreditNoteResponse.

        Not included in summary mode  # noqa: E501

        :param line_items: The line_items of this CreditNoteResponse.  # noqa: E501
        :type: list[LineItemResponse]
        """

        self._line_items = line_items
