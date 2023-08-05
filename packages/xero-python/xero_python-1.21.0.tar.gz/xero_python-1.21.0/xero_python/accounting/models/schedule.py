# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Schedule(BaseModel):
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
        "period": "int",
        "unit": "str",
        "due_date": "int",
        "due_date_type": "str",
        "start_date": "date[ms-format]",
        "next_scheduled_date": "date[ms-format]",
        "end_date": "date[ms-format]",
    }

    attribute_map = {
        "period": "Period",
        "unit": "Unit",
        "due_date": "DueDate",
        "due_date_type": "DueDateType",
        "start_date": "StartDate",
        "next_scheduled_date": "NextScheduledDate",
        "end_date": "EndDate",
    }

    def __init__(
        self,
        period=None,
        unit=None,
        due_date=None,
        due_date_type=None,
        start_date=None,
        next_scheduled_date=None,
        end_date=None,
    ):  # noqa: E501
        """Schedule - a model defined in OpenAPI"""  # noqa: E501

        self._period = None
        self._unit = None
        self._due_date = None
        self._due_date_type = None
        self._start_date = None
        self._next_scheduled_date = None
        self._end_date = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if unit is not None:
            self.unit = unit
        if due_date is not None:
            self.due_date = due_date
        if due_date_type is not None:
            self.due_date_type = due_date_type
        if start_date is not None:
            self.start_date = start_date
        if next_scheduled_date is not None:
            self.next_scheduled_date = next_scheduled_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def period(self):
        """Gets the period of this Schedule.  # noqa: E501

        Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months)  # noqa: E501

        :return: The period of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Schedule.

        Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months)  # noqa: E501

        :param period: The period of this Schedule.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def unit(self):
        """Gets the unit of this Schedule.  # noqa: E501

        One of the following - WEEKLY or MONTHLY  # noqa: E501

        :return: The unit of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Schedule.

        One of the following - WEEKLY or MONTHLY  # noqa: E501

        :param unit: The unit of this Schedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["WEEKLY", "MONTHLY", "None"]  # noqa: E501

        if unit:
            if unit not in allowed_values:
                raise ValueError(
                    "Invalid value for `unit` ({0}), must be one of {1}".format(  # noqa: E501
                        unit, allowed_values
                    )
                )

        self._unit = unit

    @property
    def due_date(self):
        """Gets the due_date of this Schedule.  # noqa: E501

        Integer used with due date type e.g 20 (of following month), 31 (of current month)  # noqa: E501

        :return: The due_date of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Schedule.

        Integer used with due date type e.g 20 (of following month), 31 (of current month)  # noqa: E501

        :param due_date: The due_date of this Schedule.  # noqa: E501
        :type: int
        """

        self._due_date = due_date

    @property
    def due_date_type(self):
        """Gets the due_date_type of this Schedule.  # noqa: E501

        the payment terms  # noqa: E501

        :return: The due_date_type of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._due_date_type

    @due_date_type.setter
    def due_date_type(self, due_date_type):
        """Sets the due_date_type of this Schedule.

        the payment terms  # noqa: E501

        :param due_date_type: The due_date_type of this Schedule.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "DAYSAFTERINVOICEDATE",
            "DAYSAFTERINVOICEMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
            "None",
        ]  # noqa: E501

        if due_date_type:
            if due_date_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `due_date_type` ({0}), must be one of {1}".format(  # noqa: E501
                        due_date_type, allowed_values
                    )
                )

        self._due_date_type = due_date_type

    @property
    def start_date(self):
        """Gets the start_date of this Schedule.  # noqa: E501

        Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited)  # noqa: E501

        :return: The start_date of this Schedule.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Schedule.

        Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited)  # noqa: E501

        :param start_date: The start_date of this Schedule.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def next_scheduled_date(self):
        """Gets the next_scheduled_date of this Schedule.  # noqa: E501

        The calendar date of the next invoice in the schedule to be generated  # noqa: E501

        :return: The next_scheduled_date of this Schedule.  # noqa: E501
        :rtype: date
        """
        return self._next_scheduled_date

    @next_scheduled_date.setter
    def next_scheduled_date(self, next_scheduled_date):
        """Sets the next_scheduled_date of this Schedule.

        The calendar date of the next invoice in the schedule to be generated  # noqa: E501

        :param next_scheduled_date: The next_scheduled_date of this Schedule.  # noqa: E501
        :type: date
        """

        self._next_scheduled_date = next_scheduled_date

    @property
    def end_date(self):
        """Gets the end_date of this Schedule.  # noqa: E501

        Invoice end date – only returned if the template has an end date set  # noqa: E501

        :return: The end_date of this Schedule.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Schedule.

        Invoice end date – only returned if the template has an end date set  # noqa: E501

        :param end_date: The end_date of this Schedule.  # noqa: E501
        :type: date
        """

        self._end_date = end_date
