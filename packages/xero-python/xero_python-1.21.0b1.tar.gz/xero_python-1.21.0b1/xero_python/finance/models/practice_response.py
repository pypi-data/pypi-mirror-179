# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PracticeResponse(BaseModel):
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
        "xero_partner_since": "int",
        "tier": "str",
        "location": "str",
        "organisation_count": "int",
        "staff_certified": "bool",
    }

    attribute_map = {
        "xero_partner_since": "xeroPartnerSince",
        "tier": "tier",
        "location": "location",
        "organisation_count": "organisationCount",
        "staff_certified": "staffCertified",
    }

    def __init__(
        self,
        xero_partner_since=None,
        tier=None,
        location=None,
        organisation_count=None,
        staff_certified=None,
    ):  # noqa: E501
        """PracticeResponse - a model defined in OpenAPI"""  # noqa: E501

        self._xero_partner_since = None
        self._tier = None
        self._location = None
        self._organisation_count = None
        self._staff_certified = None
        self.discriminator = None

        if xero_partner_since is not None:
            self.xero_partner_since = xero_partner_since
        if tier is not None:
            self.tier = tier
        if location is not None:
            self.location = location
        if organisation_count is not None:
            self.organisation_count = organisation_count
        if staff_certified is not None:
            self.staff_certified = staff_certified

    @property
    def xero_partner_since(self):
        """Gets the xero_partner_since of this PracticeResponse.  # noqa: E501

        Year of becoming a partner.  # noqa: E501

        :return: The xero_partner_since of this PracticeResponse.  # noqa: E501
        :rtype: int
        """
        return self._xero_partner_since

    @xero_partner_since.setter
    def xero_partner_since(self, xero_partner_since):
        """Sets the xero_partner_since of this PracticeResponse.

        Year of becoming a partner.  # noqa: E501

        :param xero_partner_since: The xero_partner_since of this PracticeResponse.  # noqa: E501
        :type: int
        """

        self._xero_partner_since = xero_partner_since

    @property
    def tier(self):
        """Gets the tier of this PracticeResponse.  # noqa: E501

        Customer tier e.g. Silver  # noqa: E501

        :return: The tier of this PracticeResponse.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this PracticeResponse.

        Customer tier e.g. Silver  # noqa: E501

        :param tier: The tier of this PracticeResponse.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def location(self):
        """Gets the location of this PracticeResponse.  # noqa: E501

        Country of location.  # noqa: E501

        :return: The location of this PracticeResponse.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PracticeResponse.

        Country of location.  # noqa: E501

        :param location: The location of this PracticeResponse.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def organisation_count(self):
        """Gets the organisation_count of this PracticeResponse.  # noqa: E501

        Organisation count.  # noqa: E501

        :return: The organisation_count of this PracticeResponse.  # noqa: E501
        :rtype: int
        """
        return self._organisation_count

    @organisation_count.setter
    def organisation_count(self, organisation_count):
        """Sets the organisation_count of this PracticeResponse.

        Organisation count.  # noqa: E501

        :param organisation_count: The organisation_count of this PracticeResponse.  # noqa: E501
        :type: int
        """

        self._organisation_count = organisation_count

    @property
    def staff_certified(self):
        """Gets the staff_certified of this PracticeResponse.  # noqa: E501

        Staff certified (true/false).  # noqa: E501

        :return: The staff_certified of this PracticeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._staff_certified

    @staff_certified.setter
    def staff_certified(self, staff_certified):
        """Sets the staff_certified of this PracticeResponse.

        Staff certified (true/false).  # noqa: E501

        :param staff_certified: The staff_certified of this PracticeResponse.  # noqa: E501
        :type: bool
        """

        self._staff_certified = staff_certified
