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
class CourtDate(Date):
    """
    Holds court date
    """

    date: str
    when: str
    where: str
    what: str


class CourtDates(Dates):
    """
    Holds court dates
    """

    data: list[CourtDate]

    def filter(self, query: list[str] | str) -> CourtDates:
        """
        Filters court dates by search term(s)

        :param query: List[str] | str Search terms
        :return: CourtDates Filtered court dates
        """

        return CourtDates(self._filter(query))

    def data2ics(self, duration: int = 1) -> ics.Calendar:
        """
        Exports court dates as ICS calendar object

        :param duration: int Duration of each assignment (in hours)
        :return: ics.Calendar
        """

        # Create calendar
        calendar = ics.Calendar(creator=self.creator)

        # Define timezone
        timezone = zoneinfo.ZoneInfo(self.timezone)

        # Iterate over assignments
        for item in self.data:
            # Define timezone, date & times
            time = self.to_time(item.date + item.when, "%Y-%m-%d%H:%M")
            begin = time.replace(tzinfo=timezone)
            end = begin + datetime.timedelta(hours=duration)

            # Create event
            event = ics.Event(
                uid=data2hash(item),
                name=f"Sitzungsdienst ({item.what})",
                created=datetime.datetime.now(timezone),
                begin=begin,
                end=end,
                location=item.where,
            )

            # Add assignee(s) as attendee(s)
            self.add_attendees(item.who, event)

            # Add event to calendar
            calendar.events.add(event)

        return calendar
