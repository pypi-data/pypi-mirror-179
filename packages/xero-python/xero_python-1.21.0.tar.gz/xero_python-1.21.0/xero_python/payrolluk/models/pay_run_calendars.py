# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayRunCalendars(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_run_calendars": "list[PayRunCalendar]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_run_calendars": "payRunCalendars",
    }

    def __init__(
        self, pagination=None, problem=None, pay_run_calendars=None
    ):  # noqa: E501
        """PayRunCalendars - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._pay_run_calendars = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_run_calendars is not None:
            self.pay_run_calendars = pay_run_calendars

    @property
    def pagination(self):
        """Gets the pagination of this PayRunCalendars.  # noqa: E501


        :return: The pagination of this PayRunCalendars.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PayRunCalendars.


        :param pagination: The pagination of this PayRunCalendars.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this PayRunCalendars.  # noqa: E501


        :return: The problem of this PayRunCalendars.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this PayRunCalendars.


        :param problem: The problem of this PayRunCalendars.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def pay_run_calendars(self):
        """Gets the pay_run_calendars of this PayRunCalendars.  # noqa: E501


        :return: The pay_run_calendars of this PayRunCalendars.  # noqa: E501
        :rtype: list[PayRunCalendar]
        """
        return self._pay_run_calendars

    @pay_run_calendars.setter
    def pay_run_calendars(self, pay_run_calendars):
        """Sets the pay_run_calendars of this PayRunCalendars.


        :param pay_run_calendars: The pay_run_calendars of this PayRunCalendars.  # noqa: E501
        :type: list[PayRunCalendar]
        """

        self._pay_run_calendars = pay_run_calendars
