# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeStatutorySickLeave(BaseModel):
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
        "statutory_leave_id": "str",
        "employee_id": "str",
        "leave_type_id": "str",
        "start_date": "date",
        "end_date": "date",
        "type": "str",
        "status": "str",
        "work_pattern": "list[str]",
        "is_pregnancy_related": "bool",
        "sufficient_notice": "bool",
        "is_entitled": "bool",
        "entitlement_weeks_requested": "float",
        "entitlement_weeks_qualified": "float",
        "entitlement_weeks_remaining": "float",
        "overlaps_with_other_leave": "bool",
        "entitlement_failure_reasons": "list[str]",
    }

    attribute_map = {
        "statutory_leave_id": "statutoryLeaveID",
        "employee_id": "employeeID",
        "leave_type_id": "leaveTypeID",
        "start_date": "startDate",
        "end_date": "endDate",
        "type": "type",
        "status": "status",
        "work_pattern": "workPattern",
        "is_pregnancy_related": "isPregnancyRelated",
        "sufficient_notice": "sufficientNotice",
        "is_entitled": "isEntitled",
        "entitlement_weeks_requested": "entitlementWeeksRequested",
        "entitlement_weeks_qualified": "entitlementWeeksQualified",
        "entitlement_weeks_remaining": "entitlementWeeksRemaining",
        "overlaps_with_other_leave": "overlapsWithOtherLeave",
        "entitlement_failure_reasons": "entitlementFailureReasons",
    }

    def __init__(
        self,
        statutory_leave_id=None,
        employee_id=None,
        leave_type_id=None,
        start_date=None,
        end_date=None,
        type=None,
        status=None,
        work_pattern=None,
        is_pregnancy_related=None,
        sufficient_notice=None,
        is_entitled=None,
        entitlement_weeks_requested=None,
        entitlement_weeks_qualified=None,
        entitlement_weeks_remaining=None,
        overlaps_with_other_leave=None,
        entitlement_failure_reasons=None,
    ):  # noqa: E501
        """EmployeeStatutorySickLeave - a model defined in OpenAPI"""  # noqa: E501

        self._statutory_leave_id = None
        self._employee_id = None
        self._leave_type_id = None
        self._start_date = None
        self._end_date = None
        self._type = None
        self._status = None
        self._work_pattern = None
        self._is_pregnancy_related = None
        self._sufficient_notice = None
        self._is_entitled = None
        self._entitlement_weeks_requested = None
        self._entitlement_weeks_qualified = None
        self._entitlement_weeks_remaining = None
        self._overlaps_with_other_leave = None
        self._entitlement_failure_reasons = None
        self.discriminator = None

        if statutory_leave_id is not None:
            self.statutory_leave_id = statutory_leave_id
        self.employee_id = employee_id
        self.leave_type_id = leave_type_id
        self.start_date = start_date
        self.end_date = end_date
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        self.work_pattern = work_pattern
        self.is_pregnancy_related = is_pregnancy_related
        self.sufficient_notice = sufficient_notice
        if is_entitled is not None:
            self.is_entitled = is_entitled
        if entitlement_weeks_requested is not None:
            self.entitlement_weeks_requested = entitlement_weeks_requested
        if entitlement_weeks_qualified is not None:
            self.entitlement_weeks_qualified = entitlement_weeks_qualified
        if entitlement_weeks_remaining is not None:
            self.entitlement_weeks_remaining = entitlement_weeks_remaining
        if overlaps_with_other_leave is not None:
            self.overlaps_with_other_leave = overlaps_with_other_leave
        if entitlement_failure_reasons is not None:
            self.entitlement_failure_reasons = entitlement_failure_reasons

    @property
    def statutory_leave_id(self):
        """Gets the statutory_leave_id of this EmployeeStatutorySickLeave.  # noqa: E501

        The unique identifier (guid) of a statutory leave  # noqa: E501

        :return: The statutory_leave_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: str
        """
        return self._statutory_leave_id

    @statutory_leave_id.setter
    def statutory_leave_id(self, statutory_leave_id):
        """Sets the statutory_leave_id of this EmployeeStatutorySickLeave.

        The unique identifier (guid) of a statutory leave  # noqa: E501

        :param statutory_leave_id: The statutory_leave_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: str
        """

        self._statutory_leave_id = statutory_leave_id

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeeStatutorySickLeave.  # noqa: E501

        The unique identifier (guid) of the employee  # noqa: E501

        :return: The employee_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeeStatutorySickLeave.

        The unique identifier (guid) of the employee  # noqa: E501

        :param employee_id: The employee_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: str
        """
        if employee_id is None:
            raise ValueError(
                "Invalid value for `employee_id`, must not be `None`"
            )  # noqa: E501

        self._employee_id = employee_id

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this EmployeeStatutorySickLeave.  # noqa: E501

        The unique identifier (guid) of the \"Statutory Sick Leave (non-pensionable)\" pay item  # noqa: E501

        :return: The leave_type_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this EmployeeStatutorySickLeave.

        The unique identifier (guid) of the \"Statutory Sick Leave (non-pensionable)\" pay item  # noqa: E501

        :param leave_type_id: The leave_type_id of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: str
        """
        if leave_type_id is None:
            raise ValueError(
                "Invalid value for `leave_type_id`, must not be `None`"
            )  # noqa: E501

        self._leave_type_id = leave_type_id

    @property
    def start_date(self):
        """Gets the start_date of this EmployeeStatutorySickLeave.  # noqa: E501

        The date when the leave starts  # noqa: E501

        :return: The start_date of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EmployeeStatutorySickLeave.

        The date when the leave starts  # noqa: E501

        :param start_date: The start_date of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError(
                "Invalid value for `start_date`, must not be `None`"
            )  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EmployeeStatutorySickLeave.  # noqa: E501

        The date when the leave ends  # noqa: E501

        :return: The end_date of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EmployeeStatutorySickLeave.

        The date when the leave ends  # noqa: E501

        :param end_date: The end_date of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError(
                "Invalid value for `end_date`, must not be `None`"
            )  # noqa: E501

        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this EmployeeStatutorySickLeave.  # noqa: E501

        the type of statutory leave  # noqa: E501

        :return: The type of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmployeeStatutorySickLeave.

        the type of statutory leave  # noqa: E501

        :param type: The type of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this EmployeeStatutorySickLeave.  # noqa: E501

        the type of statutory leave  # noqa: E501

        :return: The status of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmployeeStatutorySickLeave.

        the type of statutory leave  # noqa: E501

        :param status: The status of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def work_pattern(self):
        """Gets the work_pattern of this EmployeeStatutorySickLeave.  # noqa: E501

        The days of the work week the employee is scheduled to work at the time the leave is taken  # noqa: E501

        :return: The work_pattern of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: list[str]
        """
        return self._work_pattern

    @work_pattern.setter
    def work_pattern(self, work_pattern):
        """Sets the work_pattern of this EmployeeStatutorySickLeave.

        The days of the work week the employee is scheduled to work at the time the leave is taken  # noqa: E501

        :param work_pattern: The work_pattern of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: list[str]
        """
        if work_pattern is None:
            raise ValueError(
                "Invalid value for `work_pattern`, must not be `None`"
            )  # noqa: E501

        self._work_pattern = work_pattern

    @property
    def is_pregnancy_related(self):
        """Gets the is_pregnancy_related of this EmployeeStatutorySickLeave.  # noqa: E501

        Whether the sick leave was pregnancy related  # noqa: E501

        :return: The is_pregnancy_related of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: bool
        """
        return self._is_pregnancy_related

    @is_pregnancy_related.setter
    def is_pregnancy_related(self, is_pregnancy_related):
        """Sets the is_pregnancy_related of this EmployeeStatutorySickLeave.

        Whether the sick leave was pregnancy related  # noqa: E501

        :param is_pregnancy_related: The is_pregnancy_related of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: bool
        """
        if is_pregnancy_related is None:
            raise ValueError(
                "Invalid value for `is_pregnancy_related`, must not be `None`"
            )  # noqa: E501

        self._is_pregnancy_related = is_pregnancy_related

    @property
    def sufficient_notice(self):
        """Gets the sufficient_notice of this EmployeeStatutorySickLeave.  # noqa: E501

        Whether the employee provided sufficient notice and documentation as required by the employer supporting the sick leave request  # noqa: E501

        :return: The sufficient_notice of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: bool
        """
        return self._sufficient_notice

    @sufficient_notice.setter
    def sufficient_notice(self, sufficient_notice):
        """Sets the sufficient_notice of this EmployeeStatutorySickLeave.

        Whether the employee provided sufficient notice and documentation as required by the employer supporting the sick leave request  # noqa: E501

        :param sufficient_notice: The sufficient_notice of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: bool
        """
        if sufficient_notice is None:
            raise ValueError(
                "Invalid value for `sufficient_notice`, must not be `None`"
            )  # noqa: E501

        self._sufficient_notice = sufficient_notice

    @property
    def is_entitled(self):
        """Gets the is_entitled of this EmployeeStatutorySickLeave.  # noqa: E501

        Whether the leave was entitled to receive payment  # noqa: E501

        :return: The is_entitled of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: bool
        """
        return self._is_entitled

    @is_entitled.setter
    def is_entitled(self, is_entitled):
        """Sets the is_entitled of this EmployeeStatutorySickLeave.

        Whether the leave was entitled to receive payment  # noqa: E501

        :param is_entitled: The is_entitled of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: bool
        """

        self._is_entitled = is_entitled

    @property
    def entitlement_weeks_requested(self):
        """Gets the entitlement_weeks_requested of this EmployeeStatutorySickLeave.  # noqa: E501

        The amount of requested time (in weeks)  # noqa: E501

        :return: The entitlement_weeks_requested of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: float
        """
        return self._entitlement_weeks_requested

    @entitlement_weeks_requested.setter
    def entitlement_weeks_requested(self, entitlement_weeks_requested):
        """Sets the entitlement_weeks_requested of this EmployeeStatutorySickLeave.

        The amount of requested time (in weeks)  # noqa: E501

        :param entitlement_weeks_requested: The entitlement_weeks_requested of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: float
        """

        self._entitlement_weeks_requested = entitlement_weeks_requested

    @property
    def entitlement_weeks_qualified(self):
        """Gets the entitlement_weeks_qualified of this EmployeeStatutorySickLeave.  # noqa: E501

        The amount of statutory sick leave time off (in weeks) that is available to take at the time the leave was requested  # noqa: E501

        :return: The entitlement_weeks_qualified of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: float
        """
        return self._entitlement_weeks_qualified

    @entitlement_weeks_qualified.setter
    def entitlement_weeks_qualified(self, entitlement_weeks_qualified):
        """Sets the entitlement_weeks_qualified of this EmployeeStatutorySickLeave.

        The amount of statutory sick leave time off (in weeks) that is available to take at the time the leave was requested  # noqa: E501

        :param entitlement_weeks_qualified: The entitlement_weeks_qualified of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: float
        """

        self._entitlement_weeks_qualified = entitlement_weeks_qualified

    @property
    def entitlement_weeks_remaining(self):
        """Gets the entitlement_weeks_remaining of this EmployeeStatutorySickLeave.  # noqa: E501

        A calculated amount of time (in weeks) that remains for the statutory sick leave period  # noqa: E501

        :return: The entitlement_weeks_remaining of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: float
        """
        return self._entitlement_weeks_remaining

    @entitlement_weeks_remaining.setter
    def entitlement_weeks_remaining(self, entitlement_weeks_remaining):
        """Sets the entitlement_weeks_remaining of this EmployeeStatutorySickLeave.

        A calculated amount of time (in weeks) that remains for the statutory sick leave period  # noqa: E501

        :param entitlement_weeks_remaining: The entitlement_weeks_remaining of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: float
        """

        self._entitlement_weeks_remaining = entitlement_weeks_remaining

    @property
    def overlaps_with_other_leave(self):
        """Gets the overlaps_with_other_leave of this EmployeeStatutorySickLeave.  # noqa: E501

        Whether another leave (Paternity, Shared Parental specifically) occurs during the requested leave's period. While this is allowed it could affect payment amounts  # noqa: E501

        :return: The overlaps_with_other_leave of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: bool
        """
        return self._overlaps_with_other_leave

    @overlaps_with_other_leave.setter
    def overlaps_with_other_leave(self, overlaps_with_other_leave):
        """Sets the overlaps_with_other_leave of this EmployeeStatutorySickLeave.

        Whether another leave (Paternity, Shared Parental specifically) occurs during the requested leave's period. While this is allowed it could affect payment amounts  # noqa: E501

        :param overlaps_with_other_leave: The overlaps_with_other_leave of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: bool
        """

        self._overlaps_with_other_leave = overlaps_with_other_leave

    @property
    def entitlement_failure_reasons(self):
        """Gets the entitlement_failure_reasons of this EmployeeStatutorySickLeave.  # noqa: E501

        If the leave requested was considered \"not entitled\", the reasons why are listed here.  # noqa: E501

        :return: The entitlement_failure_reasons of this EmployeeStatutorySickLeave.  # noqa: E501
        :rtype: list[str]
        """
        return self._entitlement_failure_reasons

    @entitlement_failure_reasons.setter
    def entitlement_failure_reasons(self, entitlement_failure_reasons):
        """Sets the entitlement_failure_reasons of this EmployeeStatutorySickLeave.

        If the leave requested was considered \"not entitled\", the reasons why are listed here.  # noqa: E501

        :param entitlement_failure_reasons: The entitlement_failure_reasons of this EmployeeStatutorySickLeave.  # noqa: E501
        :type: list[str]
        """
        allowed_values = [
            "UnableToCalculateAwe",
            "AweLowerThanLel",
            "NotQualifiedInPreviousPiw",
            "ExceededMaximumEntitlementWeeksOfSsp",
            "ExceededMaximumDurationOfPiw",
            "SufficientNoticeNotGiven",
            "None",
        ]  # noqa: E501
        if not set(entitlement_failure_reasons).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entitlement_failure_reasons` [{0}], must be a subset of [{1}]".format(  # noqa: E501
                    ", ".join(
                        map(str, set(entitlement_failure_reasons) - set(allowed_values))
                    ),  # noqa: E501
                    ", ".join(map(str, allowed_values)),
                )
            )

        self._entitlement_failure_reasons = entitlement_failure_reasons
