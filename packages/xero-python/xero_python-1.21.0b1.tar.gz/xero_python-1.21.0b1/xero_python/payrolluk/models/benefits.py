# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Benefits(BaseModel):
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
        "benefits": "list[Benefit]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "benefits": "benefits",
    }

    def __init__(self, pagination=None, problem=None, benefits=None):  # noqa: E501
        """Benefits - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._benefits = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if benefits is not None:
            self.benefits = benefits

    @property
    def pagination(self):
        """Gets the pagination of this Benefits.  # noqa: E501


        :return: The pagination of this Benefits.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Benefits.


        :param pagination: The pagination of this Benefits.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this Benefits.  # noqa: E501


        :return: The problem of this Benefits.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this Benefits.


        :param problem: The problem of this Benefits.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def benefits(self):
        """Gets the benefits of this Benefits.  # noqa: E501


        :return: The benefits of this Benefits.  # noqa: E501
        :rtype: list[Benefit]
        """
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        """Sets the benefits of this Benefits.


        :param benefits: The benefits of this Benefits.  # noqa: E501
        :type: list[Benefit]
        """

        self._benefits = benefits
