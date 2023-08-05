# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EarningsRate(BaseModel):
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
        "earnings_rate_id": "str",
        "name": "str",
        "earnings_type": "str",
        "rate_type": "str",
        "type_of_units": "str",
        "current_record": "bool",
        "expense_account_id": "str",
        "rate_per_unit": "float",
        "multiple_of_ordinary_earnings_rate": "float",
        "fixed_amount": "float",
    }

    attribute_map = {
        "earnings_rate_id": "earningsRateID",
        "name": "name",
        "earnings_type": "earningsType",
        "rate_type": "rateType",
        "type_of_units": "typeOfUnits",
        "current_record": "currentRecord",
        "expense_account_id": "expenseAccountID",
        "rate_per_unit": "ratePerUnit",
        "multiple_of_ordinary_earnings_rate": "multipleOfOrdinaryEarningsRate",
        "fixed_amount": "fixedAmount",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        name=None,
        earnings_type=None,
        rate_type=None,
        type_of_units=None,
        current_record=None,
        expense_account_id=None,
        rate_per_unit=None,
        multiple_of_ordinary_earnings_rate=None,
        fixed_amount=None,
    ):  # noqa: E501
        """EarningsRate - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_rate_id = None
        self._name = None
        self._earnings_type = None
        self._rate_type = None
        self._type_of_units = None
        self._current_record = None
        self._expense_account_id = None
        self._rate_per_unit = None
        self._multiple_of_ordinary_earnings_rate = None
        self._fixed_amount = None
        self.discriminator = None

        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        self.name = name
        self.earnings_type = earnings_type
        self.rate_type = rate_type
        self.type_of_units = type_of_units
        if current_record is not None:
            self.current_record = current_record
        self.expense_account_id = expense_account_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if multiple_of_ordinary_earnings_rate is not None:
            self.multiple_of_ordinary_earnings_rate = multiple_of_ordinary_earnings_rate
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this EarningsRate.  # noqa: E501

        Xero unique identifier for an earning rate  # noqa: E501

        :return: The earnings_rate_id of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this EarningsRate.

        Xero unique identifier for an earning rate  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this EarningsRate.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def name(self):
        """Gets the name of this EarningsRate.  # noqa: E501

        Name of the earning rate  # noqa: E501

        :return: The name of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EarningsRate.

        Name of the earning rate  # noqa: E501

        :param name: The name of this EarningsRate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def earnings_type(self):
        """Gets the earnings_type of this EarningsRate.  # noqa: E501

        Indicates how an employee will be paid when taking this type of earning  # noqa: E501

        :return: The earnings_type of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._earnings_type

    @earnings_type.setter
    def earnings_type(self, earnings_type):
        """Sets the earnings_type of this EarningsRate.

        Indicates how an employee will be paid when taking this type of earning  # noqa: E501

        :param earnings_type: The earnings_type of this EarningsRate.  # noqa: E501
        :type: str
        """
        if earnings_type is None:
            raise ValueError(
                "Invalid value for `earnings_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "Allowance",
            "Backpay",
            "Bonus",
            "Commission",
            "LumpSum",
            "OtherEarnings",
            "OvertimeEarnings",
            "RegularEarnings",
            "StatutoryAdoptionPay",
            "StatutoryAdoptionPayNonPensionable",
            "StatutoryBereavementPay",
            "StatutoryMaternityPay",
            "StatutoryMaternityPayNonPensionable",
            "StatutoryPaternityPay",
            "StatutoryPaternityPayNonPensionable",
            "StatutoryParentalBereavementPayNonPensionable",
            "StatutorySharedParentalPay",
            "StatutorySharedParentalPayNonPensionable",
            "StatutorySickPay",
            "StatutorySickPayNonPensionable",
            "TipsNonDirect",
            "TipsDirect",
            "TerminationPay",
            "None",
        ]  # noqa: E501

        if earnings_type:
            if earnings_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `earnings_type` ({0}), must be one of {1}".format(  # noqa: E501
                        earnings_type, allowed_values
                    )
                )

        self._earnings_type = earnings_type

    @property
    def rate_type(self):
        """Gets the rate_type of this EarningsRate.  # noqa: E501

        Indicates the type of the earning rate  # noqa: E501

        :return: The rate_type of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this EarningsRate.

        Indicates the type of the earning rate  # noqa: E501

        :param rate_type: The rate_type of this EarningsRate.  # noqa: E501
        :type: str
        """
        if rate_type is None:
            raise ValueError(
                "Invalid value for `rate_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "RatePerUnit",
            "MultipleOfOrdinaryEarningsRate",
            "FixedAmount",
            "None",
        ]  # noqa: E501

        if rate_type:
            if rate_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `rate_type` ({0}), must be one of {1}".format(  # noqa: E501
                        rate_type, allowed_values
                    )
                )

        self._rate_type = rate_type

    @property
    def type_of_units(self):
        """Gets the type_of_units of this EarningsRate.  # noqa: E501

        The type of units used to record earnings  # noqa: E501

        :return: The type_of_units of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        """Sets the type_of_units of this EarningsRate.

        The type of units used to record earnings  # noqa: E501

        :param type_of_units: The type_of_units of this EarningsRate.  # noqa: E501
        :type: str
        """
        if type_of_units is None:
            raise ValueError(
                "Invalid value for `type_of_units`, must not be `None`"
            )  # noqa: E501

        self._type_of_units = type_of_units

    @property
    def current_record(self):
        """Gets the current_record of this EarningsRate.  # noqa: E501

        Indicates whether an earning type is active  # noqa: E501

        :return: The current_record of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this EarningsRate.

        Indicates whether an earning type is active  # noqa: E501

        :param current_record: The current_record of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def expense_account_id(self):
        """Gets the expense_account_id of this EarningsRate.  # noqa: E501

        The account that will be used for the earnings rate  # noqa: E501

        :return: The expense_account_id of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_id

    @expense_account_id.setter
    def expense_account_id(self, expense_account_id):
        """Sets the expense_account_id of this EarningsRate.

        The account that will be used for the earnings rate  # noqa: E501

        :param expense_account_id: The expense_account_id of this EarningsRate.  # noqa: E501
        :type: str
        """
        if expense_account_id is None:
            raise ValueError(
                "Invalid value for `expense_account_id`, must not be `None`"
            )  # noqa: E501

        self._expense_account_id = expense_account_id

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this EarningsRate.  # noqa: E501

        Default rate per unit (optional). Only applicable if RateType is RatePerUnit  # noqa: E501

        :return: The rate_per_unit of this EarningsRate.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this EarningsRate.

        Default rate per unit (optional). Only applicable if RateType is RatePerUnit  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this EarningsRate.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def multiple_of_ordinary_earnings_rate(self):
        """Gets the multiple_of_ordinary_earnings_rate of this EarningsRate.  # noqa: E501

        This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MultipleOfOrdinaryEarningsRate  # noqa: E501

        :return: The multiple_of_ordinary_earnings_rate of this EarningsRate.  # noqa: E501
        :rtype: float
        """
        return self._multiple_of_ordinary_earnings_rate

    @multiple_of_ordinary_earnings_rate.setter
    def multiple_of_ordinary_earnings_rate(self, multiple_of_ordinary_earnings_rate):
        """Sets the multiple_of_ordinary_earnings_rate of this EarningsRate.

        This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MultipleOfOrdinaryEarningsRate  # noqa: E501

        :param multiple_of_ordinary_earnings_rate: The multiple_of_ordinary_earnings_rate of this EarningsRate.  # noqa: E501
        :type: float
        """

        self._multiple_of_ordinary_earnings_rate = multiple_of_ordinary_earnings_rate

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this EarningsRate.  # noqa: E501

        Optional Fixed Rate Amount. Applicable for FixedAmount Rate  # noqa: E501

        :return: The fixed_amount of this EarningsRate.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this EarningsRate.

        Optional Fixed Rate Amount. Applicable for FixedAmount Rate  # noqa: E501

        :param fixed_amount: The fixed_amount of this EarningsRate.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount
