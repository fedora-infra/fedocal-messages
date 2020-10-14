# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Unit tests for the message schema."""

import datetime

import pytest

from jsonschema import ValidationError
from ..messages import ReminderV1
from .utils import DUMMY_CALENDAR, DUMMY_MEETING


def test_minimal():
    """
    Assert the message schema validates a message with the required fields.
    """
    body = {
        "meeting": DUMMY_MEETING,
        "calendar": DUMMY_CALENDAR,
    }
    message = ReminderV1(body=body)
    message.validate()
    assert message.url is None


def test_full():
    """
    Assert the message schema validates a message with the required fields.
    """
    body = {
        "meeting": DUMMY_MEETING,
        "calendar": DUMMY_CALENDAR,
    }
    message = ReminderV1(body=body)
    message.validate()
    assert message.url is None


def test_missing_fields():
    """Assert an exception is actually raised on validation failure."""
    minimal_message = {
        "calendar": DUMMY_CALENDAR,
    }
    message = ReminderV1(body=minimal_message)
    with pytest.raises(ValidationError):
        message.validate()


def test_str_now():
    """Assert __str__ produces a human-readable message."""
    meeting = DUMMY_MEETING.copy()
    meeting["meeting_date"] = (datetime.datetime.utcnow()).strftime("%Y-%m-%d")
    meeting["meeting_time_start"] = (datetime.datetime.utcnow()).strftime("%H:%M:%S")
    body = {
        "meeting": meeting,
        "calendar": DUMMY_CALENDAR,
    }
    expected_str = (
        "Friendly reminder!  The 'wat' meeting from the "
        "'test_calendar' calendar starts right now"
    )
    message = ReminderV1(body=body)
    message.validate()
    assert expected_str == str(message)


def test_str_thirty_minutes():
    """Assert __str__ produces a human-readable message."""
    meeting = DUMMY_MEETING.copy()
    meeting["meeting_date"] = (
        datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    ).strftime("%Y-%m-%d")
    meeting["meeting_time_start"] = (
        datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    ).strftime("%H:%M:%S")
    body = {
        "meeting": meeting,
        "calendar": DUMMY_CALENDAR,
    }
    expected_str = (
        "Friendly reminder!  The 'wat' meeting from the "
        "'test_calendar' calendar starts in 29 minutes"
    )
    message = ReminderV1(body=body)
    message.validate()
    assert expected_str == str(message)


def test_str_two_hours():
    """Assert __str__ produces a human-readable message."""
    meeting = DUMMY_MEETING.copy()
    meeting["meeting_date"] = (
        datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    ).strftime("%Y-%m-%d")
    meeting["meeting_time_start"] = (
        datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    ).strftime("%H:%M:%S")
    body = {
        "meeting": meeting,
        "calendar": DUMMY_CALENDAR,
    }
    expected_str = (
        "Friendly reminder!  The 'wat' meeting from the "
        "'test_calendar' calendar starts in 1 hour"
    )
    message = ReminderV1(body=body)
    message.validate()
    assert expected_str == str(message)


def test_str_five_days():
    """Assert __str__ produces a human-readable message."""
    meeting = DUMMY_MEETING.copy()
    meeting["meeting_date"] = (
        datetime.datetime.utcnow() + datetime.timedelta(days=5)
    ).strftime("%Y-%m-%d")
    meeting["meeting_time_start"] = (
        datetime.datetime.utcnow() + datetime.timedelta(days=5)
    ).strftime("%H:%M:%S")
    body = {
        "meeting": meeting,
        "calendar": DUMMY_CALENDAR,
    }
    expected_str = (
        "Friendly reminder!  The 'wat' meeting from the "
        "'test_calendar' calendar starts in 4 days"
    )
    message = ReminderV1(body=body)
    message.validate()
    assert expected_str == str(message)


def test_summary():
    """Assert the summary is correct."""
    body = {
        "meeting": DUMMY_MEETING,
        "calendar": DUMMY_CALENDAR,
    }
    expected_summary = (
        "Remember about the meeting 'wat' from the 'test_calendar' calendar"
    )
    message = ReminderV1(body=body)
    assert expected_summary == message.summary
