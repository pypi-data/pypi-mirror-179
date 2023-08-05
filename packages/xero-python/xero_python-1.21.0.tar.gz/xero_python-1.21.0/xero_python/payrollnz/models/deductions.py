# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Deductions(BaseModel):
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
        "deductions": "list[Deduction]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "deductions": "deductions",
    }

    def __init__(self, pagination=None, problem=None, deductions=None):  # noqa: E501
        """Deductions - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._deductions = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if deductions is not None:
            self.deductions = deductions

    @property
    def pagination(self):
        """Gets the pagination of this Deductions.  # noqa: E501


        :return: The pagination of this Deductions.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Deductions.


        :param pagination: The pagination of this Deductions.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this Deductions.  # noqa: E501


        :return: The problem of this Deductions.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this Deductions.


        :param problem: The problem of this Deductions.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def deductions(self):
        """Gets the deductions of this Deductions.  # noqa: E501


        :return: The deductions of this Deductions.  # noqa: E501
        :rtype: list[Deduction]
        """
        return self._deductions

    @deductions.setter
    def deductions(self, deductions):
        """Sets the deductions of this Deductions.


        :param deductions: The deductions of this Deductions.  # noqa: E501
        :type: list[Deduction]
        """

        self._deductions = deductions
