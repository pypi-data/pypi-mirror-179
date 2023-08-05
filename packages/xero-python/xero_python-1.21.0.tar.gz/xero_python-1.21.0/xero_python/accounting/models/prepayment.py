# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Prepayment(BaseModel):
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
        "type": "str",
        "contact": "Contact",
        "date": "date[ms-format]",
        "status": "str",
        "line_amount_types": "LineAmountTypes",
        "line_items": "list[LineItem]",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "reference": "str",
        "updated_date_utc": "datetime[ms-format]",
        "currency_code": "CurrencyCode",
        "prepayment_id": "str",
        "currency_rate": "float",
        "remaining_credit": "float",
        "allocations": "list[Allocation]",
        "payments": "list[Payment]",
        "applied_amount": "float",
        "has_attachments": "bool",
        "attachments": "list[Attachment]",
    }

    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "date": "Date",
        "status": "Status",
        "line_amount_types": "LineAmountTypes",
        "line_items": "LineItems",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "reference": "Reference",
        "updated_date_utc": "UpdatedDateUTC",
        "currency_code": "CurrencyCode",
        "prepayment_id": "PrepaymentID",
        "currency_rate": "CurrencyRate",
        "remaining_credit": "RemainingCredit",
        "allocations": "Allocations",
        "payments": "Payments",
        "applied_amount": "AppliedAmount",
        "has_attachments": "HasAttachments",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        date=None,
        status=None,
        line_amount_types=None,
        line_items=None,
        sub_total=None,
        total_tax=None,
        total=None,
        reference=None,
        updated_date_utc=None,
        currency_code=None,
        prepayment_id=None,
        currency_rate=None,
        remaining_credit=None,
        allocations=None,
        payments=None,
        applied_amount=None,
        has_attachments=False,
        attachments=None,
    ):  # noqa: E501
        """Prepayment - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._contact = None
        self._date = None
        self._status = None
        self._line_amount_types = None
        self._line_items = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._reference = None
        self._updated_date_utc = None
        self._currency_code = None
        self._prepayment_id = None
        self._currency_rate = None
        self._remaining_credit = None
        self._allocations = None
        self._payments = None
        self._applied_amount = None
        self._has_attachments = None
        self._attachments = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if status is not None:
            self.status = status
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if line_items is not None:
            self.line_items = line_items
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if reference is not None:
            self.reference = reference
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if currency_code is not None:
            self.currency_code = currency_code
        if prepayment_id is not None:
            self.prepayment_id = prepayment_id
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if remaining_credit is not None:
            self.remaining_credit = remaining_credit
        if allocations is not None:
            self.allocations = allocations
        if payments is not None:
            self.payments = payments
        if applied_amount is not None:
            self.applied_amount = applied_amount
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if attachments is not None:
            self.attachments = attachments

    @property
    def type(self):
        """Gets the type of this Prepayment.  # noqa: E501

        See Prepayment Types  # noqa: E501

        :return: The type of this Prepayment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Prepayment.

        See Prepayment Types  # noqa: E501

        :param type: The type of this Prepayment.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "RECEIVE-PREPAYMENT",
            "SPEND-PREPAYMENT",
            "ARPREPAYMENT",
            "APPREPAYMENT",
            "None",
        ]  # noqa: E501

        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                        type, allowed_values
                    )
                )

        self._type = type

    @property
    def contact(self):
        """Gets the contact of this Prepayment.  # noqa: E501


        :return: The contact of this Prepayment.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Prepayment.


        :param contact: The contact of this Prepayment.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def date(self):
        """Gets the date of this Prepayment.  # noqa: E501

        The date the prepayment is created YYYY-MM-DD  # noqa: E501

        :return: The date of this Prepayment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Prepayment.

        The date the prepayment is created YYYY-MM-DD  # noqa: E501

        :param date: The date of this Prepayment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def status(self):
        """Gets the status of this Prepayment.  # noqa: E501

        See Prepayment Status Codes  # noqa: E501

        :return: The status of this Prepayment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Prepayment.

        See Prepayment Status Codes  # noqa: E501

        :param status: The status of this Prepayment.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORISED", "PAID", "VOIDED", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this Prepayment.  # noqa: E501


        :return: The line_amount_types of this Prepayment.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this Prepayment.


        :param line_amount_types: The line_amount_types of this Prepayment.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def line_items(self):
        """Gets the line_items of this Prepayment.  # noqa: E501

        See Prepayment Line Items  # noqa: E501

        :return: The line_items of this Prepayment.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Prepayment.

        See Prepayment Line Items  # noqa: E501

        :param line_items: The line_items of this Prepayment.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def sub_total(self):
        """Gets the sub_total of this Prepayment.  # noqa: E501

        The subtotal of the prepayment excluding taxes  # noqa: E501

        :return: The sub_total of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this Prepayment.

        The subtotal of the prepayment excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this Prepayment.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this Prepayment.  # noqa: E501

        The total tax on the prepayment  # noqa: E501

        :return: The total_tax of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this Prepayment.

        The total tax on the prepayment  # noqa: E501

        :param total_tax: The total_tax of this Prepayment.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this Prepayment.  # noqa: E501

        The total of the prepayment(subtotal + total tax)  # noqa: E501

        :return: The total of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Prepayment.

        The total of the prepayment(subtotal + total tax)  # noqa: E501

        :param total: The total of this Prepayment.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def reference(self):
        """Gets the reference of this Prepayment.  # noqa: E501

        Returns Invoice number field. Reference field isn't available.  # noqa: E501

        :return: The reference of this Prepayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Prepayment.

        Returns Invoice number field. Reference field isn't available.  # noqa: E501

        :param reference: The reference of this Prepayment.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Prepayment.  # noqa: E501

        UTC timestamp of last update to the prepayment  # noqa: E501

        :return: The updated_date_utc of this Prepayment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Prepayment.

        UTC timestamp of last update to the prepayment  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Prepayment.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def currency_code(self):
        """Gets the currency_code of this Prepayment.  # noqa: E501


        :return: The currency_code of this Prepayment.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Prepayment.


        :param currency_code: The currency_code of this Prepayment.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def prepayment_id(self):
        """Gets the prepayment_id of this Prepayment.  # noqa: E501

        Xero generated unique identifier  # noqa: E501

        :return: The prepayment_id of this Prepayment.  # noqa: E501
        :rtype: str
        """
        return self._prepayment_id

    @prepayment_id.setter
    def prepayment_id(self, prepayment_id):
        """Sets the prepayment_id of this Prepayment.

        Xero generated unique identifier  # noqa: E501

        :param prepayment_id: The prepayment_id of this Prepayment.  # noqa: E501
        :type: str
        """

        self._prepayment_id = prepayment_id

    @property
    def currency_rate(self):
        """Gets the currency_rate of this Prepayment.  # noqa: E501

        The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used  # noqa: E501

        :return: The currency_rate of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this Prepayment.

        The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used  # noqa: E501

        :param currency_rate: The currency_rate of this Prepayment.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def remaining_credit(self):
        """Gets the remaining_credit of this Prepayment.  # noqa: E501

        The remaining credit balance on the prepayment  # noqa: E501

        :return: The remaining_credit of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._remaining_credit

    @remaining_credit.setter
    def remaining_credit(self, remaining_credit):
        """Sets the remaining_credit of this Prepayment.

        The remaining credit balance on the prepayment  # noqa: E501

        :param remaining_credit: The remaining_credit of this Prepayment.  # noqa: E501
        :type: float
        """

        self._remaining_credit = remaining_credit

    @property
    def allocations(self):
        """Gets the allocations of this Prepayment.  # noqa: E501

        See Allocations  # noqa: E501

        :return: The allocations of this Prepayment.  # noqa: E501
        :rtype: list[Allocation]
        """
        return self._allocations

    @allocations.setter
    def allocations(self, allocations):
        """Sets the allocations of this Prepayment.

        See Allocations  # noqa: E501

        :param allocations: The allocations of this Prepayment.  # noqa: E501
        :type: list[Allocation]
        """

        self._allocations = allocations

    @property
    def payments(self):
        """Gets the payments of this Prepayment.  # noqa: E501

        See Payments  # noqa: E501

        :return: The payments of this Prepayment.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Prepayment.

        See Payments  # noqa: E501

        :param payments: The payments of this Prepayment.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def applied_amount(self):
        """Gets the applied_amount of this Prepayment.  # noqa: E501

        The amount of applied to an invoice  # noqa: E501

        :return: The applied_amount of this Prepayment.  # noqa: E501
        :rtype: float
        """
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        """Sets the applied_amount of this Prepayment.

        The amount of applied to an invoice  # noqa: E501

        :param applied_amount: The applied_amount of this Prepayment.  # noqa: E501
        :type: float
        """

        self._applied_amount = applied_amount

    @property
    def has_attachments(self):
        """Gets the has_attachments of this Prepayment.  # noqa: E501

        boolean to indicate if a prepayment has an attachment  # noqa: E501

        :return: The has_attachments of this Prepayment.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this Prepayment.

        boolean to indicate if a prepayment has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this Prepayment.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def attachments(self):
        """Gets the attachments of this Prepayment.  # noqa: E501

        See Attachments  # noqa: E501

        :return: The attachments of this Prepayment.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Prepayment.

        See Attachments  # noqa: E501

        :param attachments: The attachments of this Prepayment.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments
