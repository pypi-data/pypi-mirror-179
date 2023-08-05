# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class User(BaseModel):
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
        "user_id": "str",
        "email_address": "str",
        "first_name": "str",
        "last_name": "str",
        "updated_date_utc": "datetime[ms-format]",
        "is_subscriber": "bool",
        "organisation_role": "str",
    }

    attribute_map = {
        "user_id": "UserID",
        "email_address": "EmailAddress",
        "first_name": "FirstName",
        "last_name": "LastName",
        "updated_date_utc": "UpdatedDateUTC",
        "is_subscriber": "IsSubscriber",
        "organisation_role": "OrganisationRole",
    }

    def __init__(
        self,
        user_id=None,
        email_address=None,
        first_name=None,
        last_name=None,
        updated_date_utc=None,
        is_subscriber=None,
        organisation_role=None,
    ):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._updated_date_utc = None
        self._is_subscriber = None
        self._organisation_role = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_subscriber is not None:
            self.is_subscriber = is_subscriber
        if organisation_role is not None:
            self.organisation_role = organisation_role

    @property
    def user_id(self):
        """Gets the user_id of this User.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The user_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.

        Xero identifier  # noqa: E501

        :param user_id: The user_id of this User.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def email_address(self):
        """Gets the email_address of this User.  # noqa: E501

        Email address of user  # noqa: E501

        :return: The email_address of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this User.

        Email address of user  # noqa: E501

        :param email_address: The email_address of this User.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        First name of user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        First name of user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        Last name of user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        Last name of user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this User.  # noqa: E501

        Timestamp of last change to user  # noqa: E501

        :return: The updated_date_utc of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this User.

        Timestamp of last change to user  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this User.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def is_subscriber(self):
        """Gets the is_subscriber of this User.  # noqa: E501

        Boolean to indicate if user is the subscriber  # noqa: E501

        :return: The is_subscriber of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscriber

    @is_subscriber.setter
    def is_subscriber(self, is_subscriber):
        """Sets the is_subscriber of this User.

        Boolean to indicate if user is the subscriber  # noqa: E501

        :param is_subscriber: The is_subscriber of this User.  # noqa: E501
        :type: bool
        """

        self._is_subscriber = is_subscriber

    @property
    def organisation_role(self):
        """Gets the organisation_role of this User.  # noqa: E501

        User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc)  # noqa: E501

        :return: The organisation_role of this User.  # noqa: E501
        :rtype: str
        """
        return self._organisation_role

    @organisation_role.setter
    def organisation_role(self, organisation_role):
        """Sets the organisation_role of this User.

        User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc)  # noqa: E501

        :param organisation_role: The organisation_role of this User.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "READONLY",
            "INVOICEONLY",
            "STANDARD",
            "FINANCIALADVISER",
            "MANAGEDCLIENT",
            "CASHBOOKCLIENT",
            "UNKNOWN",
            "None",
        ]  # noqa: E501

        if organisation_role:
            if organisation_role not in allowed_values:
                raise ValueError(
                    "Invalid value for `organisation_role` ({0}), must be one of {1}".format(  # noqa: E501
                        organisation_role, allowed_values
                    )
                )

        self._organisation_role = organisation_role
