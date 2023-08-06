#   calct: Easily do calculations on hours and minutes using the command line
#   Copyright (C) 2022  Philippe Warren
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from datetime import timedelta
from functools import total_ordering
from itertools import chain

from calct._common import (
    CANT_BE_CUSTOM_SEPARATOR,
    DEFAULT_HOUR_SEPARATOR,
    DEFAULT_MINUTE_SEPARATOR,
    Number,
)
from calct._divmod import duration_friendly_divmod
from calct._duration_parser import compile_matcher, parse_duration


@total_ordering
class Duration:
    """Representation of a duration as hours and minutes."""

    str_hour_sep: str = DEFAULT_HOUR_SEPARATOR[0]
    str_minute_sep = DEFAULT_MINUTE_SEPARATOR[0]

    @classmethod
    def get_string_hour_minute_separator(cls) -> str:
        """Return the character used to separate hours and minutes."""
        return cls.str_hour_sep

    @classmethod
    def set_string_hour_minute_separator(cls, sep: str) -> None:
        """Set the character used to separate hours and minutes."""
        if not isinstance(sep, str) or not len(sep) == 1:  # type:ignore
            raise TypeError("Separator needs to be a one-character string")
        if set(sep) & set(CANT_BE_CUSTOM_SEPARATOR + DEFAULT_MINUTE_SEPARATOR) != set():
            raise ValueError(
                "Separator can't contain a character from "
                f"`{''.join(set(CANT_BE_CUSTOM_SEPARATOR + DEFAULT_MINUTE_SEPARATOR))}`"
                "or it would break the parser"
            )
        cls.str_hour_sep = sep

    @classmethod
    def del_string_hour_minute_separator(cls) -> None:
        """Restore the default separator for hours and minutes."""
        cls.str_hour_sep = DEFAULT_HOUR_SEPARATOR[0]

    def __init__(self, hours: Number = 0, minutes: int = 0) -> None:
        self.total_minutes: int = int(hours * 60) + minutes

    @property
    def hours(self) -> int:
        """The `hours` part of the duration, truncated"""
        sign, hours, _ = duration_friendly_divmod(self.total_minutes, 60)
        return sign * hours

    @hours.setter
    def hours(self, new_hours: Number) -> None:
        self.total_minutes = int(new_hours * 60)

    @property
    def minutes(self) -> int:
        """The `minutes` part of the duration, truncated"""
        sign, _, minutes = duration_friendly_divmod(self.total_minutes, 60)
        return sign * minutes

    @minutes.setter
    def minutes(self, new_minutes: int) -> None:
        self.total_minutes = self.hours * 60 + new_minutes

    @staticmethod
    def from_timedelta(time_delta: timedelta) -> Duration:
        """Create a Duration from a timedelta."""
        return Duration(minutes=int(time_delta.total_seconds() / 60))

    @classmethod
    def get_hour_seps(cls) -> set[str]:
        """Return the set of characters used to separate hours and minutes."""
        return set(DEFAULT_HOUR_SEPARATOR) | {cls.str_hour_sep}

    @classmethod
    def get_minute_seps(cls) -> set[str]:
        """Return the set of characters used to indicate minutes."""
        return set(DEFAULT_MINUTE_SEPARATOR) | {cls.str_minute_sep}

    @classmethod
    def get_hour_and_minute_seps(cls) -> set[str]:
        """Return the set of characters used to separate hours and minutes, or indicate minutes."""
        return cls.get_hour_seps() | cls.get_minute_seps()

    @classmethod
    def get_matchers(cls) -> set[str]:
        """Return the set of strings matchers that can be used to parse a duration."""
        matchers_hours = chain.from_iterable((f"%H{sep}%M", f"%H{sep}", f"{sep}%M") for sep in cls.get_hour_seps())
        matchers_minutes = chain.from_iterable((f"%M{sep}",) for sep in cls.get_minute_seps())

        return set(matchers_hours) | set(matchers_minutes)

    @classmethod
    def parse(cls, time_str: str) -> Duration:
        """Create a Duration from a string."""
        for matcher in cls.get_matchers():
            pattern = compile_matcher(matcher)
            try:
                time = parse_duration(time_str, pattern)
                return Duration(hours=time.hours, minutes=time.minutes)
            except ValueError:
                pass
        raise ValueError(f"Invalid time: {time_str}")

    def __str__(self) -> str:
        sign, hours, minutes = duration_friendly_divmod(self.total_minutes, 60)
        return f"{'-' if sign == -1 else ''}{hours}{self.str_hour_sep}{minutes:02}"

    def __repr__(self) -> str:
        return f"Duration(hours={self.hours}, minutes={self.minutes})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Duration):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for ==: '{type(self)}' and '{type(other)}'")
        return self.total_minutes == other.total_minutes

    def __lt__(self, other: Duration) -> bool:
        if not isinstance(other, Duration):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for <: '{type(self)}' and '{type(other)}'")
        return self.total_minutes < other.total_minutes

    def __add__(self, other: Duration) -> Duration:
        if not isinstance(other, Duration):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")
        return Duration(minutes=self.total_minutes + other.total_minutes)

    def __sub__(self, other: Duration) -> Duration:
        if not isinstance(other, Duration):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for -: '{type(self)}' and '{type(other)}'")
        return Duration(minutes=self.total_minutes - other.total_minutes)

    def __mul__(self, other: Number) -> Duration:
        if not isinstance(other, (int, float)):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for *: '{type(self)}' and '{type(other)}'")
        return Duration(minutes=int(self.total_minutes * other))

    def __rmul__(self, other: Number) -> Duration:
        return self.__mul__(other)

    def __truediv__(self, other: Number) -> Duration:
        if not isinstance(other, (int, float)):  # type: ignore
            raise TypeError(f"unsupported operand type(s) for /: '{type(self)}' and '{type(other)}'")
        return Duration(minutes=int(self.total_minutes / other))

    @property
    def as_timedelta(self) -> timedelta:
        """Return the duration as a timedelta."""
        return timedelta(minutes=self.total_minutes)
