from typing import List
from dataclasses import dataclass
from datetime import date, timedelta
from pandas import DataFrame
import uuid
from pledger.account.money import Money
from pledger.interest import Interest, Interval
from pledger.account.transfer import Transfer
from pledger.account.transfers import Transfers, transfers as trans


@dataclass
class Account:
    """The account model contains transfers and methods to interact with them."""

    transfers: Transfers

    interest: Interest | None

    length_months: int

    opened: date

    day_from_opened: int

    id: str = None

    name: str = ""

    def __init__(
        self,
        transfers: Transfers = None,
        interest: Interest = None,
        length_months: int = 12,
        name: str = "",
    ) -> None:

        self.id = str(uuid.uuid4())
        self.accrued_interest = Transfers()
        self.opened = date.today()
        self.length_months = length_months
        self.day_from_opened = 0

        if transfers is not None:
            assert isinstance(transfers, Transfers), "transfers variable incorrect type"

        self.transfers = transfers if transfers is not None else trans()
        self.name = name
        self.interest = interest

    def get_transfers(self) -> Transfers:
        """Get all transfers in account."""
        return self.transfers

    def set_transfers(self, transfers: List[Transfer]) -> None:
        self.transfers += trans(transfers)

    def get_balance(self) -> int:
        """Get total account balance. Initial balance plus the balance of all transfers."""
        return self.transfers.get_balance().amount

    def get_interest_balance(self) -> int:
        """Get total account balance. Initial balance plus the balance of all transfers."""
        return self.transfers.get_interest()

    def calculate_final_balance(self) -> None:
        """Payout the interest if this is an interest bearing account."""
        assert self.interest is not None, "This account does not pay interest."

        for _ in range(self.length_months * 30):
            self.calculate_daily_balance()

    def calculate_daily_balance(self) -> None:
        """Calculate the total balance per day, includig initial balance, payed and accrued interest."""
        # Get the total account balance, with or without the interest.
        # If the interest is not compounded, total balance will not include interest transfers.
        balance = self.transfers.get_balance()
        if self.interest.is_compounded() is False:
            balance -= self.transfers.get_interest()

        interest = Transfer.interest(
            self.interest.calculate_daily_interest(balance.amount),
            date=self.get_current_day().strftime("%d/%m/%Y"),
        )

        match self.interest.payout_interval:
            case Interval.DAILY:
                self.transfers.append(interest)
            case Interval.MONTHLY:
                self.accrued_interest.append(interest)
                if self.get_total_days_opened() % 30 == 0:
                    self.payout()
            case Interval.YEARLY:
                self.accrued_interest.append(interest)
                if self.get_total_days_opened() % 360 == 0:
                    self.payout()

        self.day_from_opened += 1

    def payout(self) -> None:
        """Payout the interest accrued into the main account balance."""
        interest = self.accrued_interest.get_interest()
        self.transfers.append(Transfer.interest(interest.amount))
        self.accrued_interest = Transfers()

    def get_current_day(self) -> date:
        return self.opened + timedelta(days=self.day_from_opened)

    def get_total_days_opened(self) -> int:
        """Get the total days that the account has been opened for."""
        return 1 + self.day_from_opened

    def get_statement(self) -> DataFrame:
        """Get statement of account activity per month. Includes account growth, balance, transactions and tax."""

        def calc_percentage_diff(initial: float, current: float) -> float:
            return abs(initial - current) / current

        def fmt_percentage(val: float) -> str:
            return f"{round(val * 100, 2)}%"

        def fmt_money(val: int) -> str:
            return f"£{val / 100:,}"

        data = []
        prev_balance = Money.zero()
        for transfers in self.transfers.group_by_month():
            date = transfers[0].get_datetime().strftime("%b-%Y")
            balance = prev_balance + transfers.get_balance()
            growth = round(
                calc_percentage_diff(prev_balance.get_amount(), balance.get_amount()),
                4,
            )

            data.append(
                [
                    date,
                    fmt_money(prev_balance.get_amount()),
                    fmt_money(balance.get_amount()),
                    fmt_money(transfers.get_balance().get_amount()),
                    fmt_percentage(growth),
                    len(transfers),
                ]
            )
            prev_balance = balance

        return DataFrame(
            data,
            columns=[
                "Date",
                "Start Balance",
                "End Balance",
                "Growth",
                "Growth %",
                "# transfers",
            ],
        )
