"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from __future__ import annotations

from dataclasses import dataclass
import datetime
import zoneinfo

import ics  # type: ignore

from ..utils import data2hash
from .base import Date, Dates


@dataclass
class ExpressDate(Date):
    """
    Holds express service date
    """

    start: str
    end: str


class ExpressDates(Dates):
    """
    Holds express service dates
    """

    data: list[ExpressDate]

    def filter(self, query: list[str] | str) -> ExpressDates:
        """
        Filters court dates by search term(s)

        :param query: List[str] | str Search terms
        :return: ExpressDates Filtered court dates
        """

        return ExpressDates(self._filter(query))

    def data2ics(self) -> ics.Calendar:
        """
        Exports express service dates as ICS calendar object

        :return: ics.Calendar
        """

        # Create calendar
        calendar = ics.Calendar(creator=self.creator)

        # Define timezone
        timezone = zoneinfo.ZoneInfo(self.timezone)

        # Iterate over assignments
        for item in self.data:
            # Define timezone, date & times
            first_day = self.to_time(item.start)
            last_day = self.to_time(item.end)

            # Create event
            event = ics.Event(
                uid=data2hash(item),
                name="Eildienst (StA)",
                created=datetime.datetime.now(timezone),
                begin=first_day.replace(tzinfo=timezone),
                end=last_day.replace(tzinfo=timezone),
            )

            # Transform to all-day event
            event.make_all_day()

            # Add assignee(s) as attendee(s)
            self.add_attendees(item.who, event)

            # Add event to calendar
            calendar.events.add(event)

        return calendar
