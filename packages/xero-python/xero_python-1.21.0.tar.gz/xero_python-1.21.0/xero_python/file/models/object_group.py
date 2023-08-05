# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class ObjectGroup(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    ACCOUNT = "Account"
    BANKTRANSACTION = "BankTransaction"
    CONTACT = "Contact"
    CREDITNOTE = "CreditNote"
    INVOICE = "Invoice"
    ITEM = "Item"
    MANUALJOURNAL = "ManualJournal"
    OVERPAYMENT = "Overpayment"
    PAYMENT = "Payment"
    PREPAYMENT = "Prepayment"
    QUOTE = "Quote"
    RECEIPT = "Receipt"
