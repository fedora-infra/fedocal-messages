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

import datetime

import dateutil.relativedelta

from .base import SCHEMA_URL, fedocalMessage, CALENDAR, MEETING


def _casual_timedelta_string(meeting):
    """Return a casual timedelta string.
    If a meeting starts in 2 hours, 15 minutes, and 32 seconds from now, then
    return just "in 2 hours".
    If a meeting starts in 7 minutes and 40 seconds from now, return just "in 7
    minutes".
    If a meeting starts 56 seconds from now, just return "right now".
    """

    now = datetime.datetime.utcnow()
    mdate = meeting["meeting_date"]
    mtime = meeting["meeting_time_start"]
    dt_string = "%s %s" % (mdate, mtime)
    meeting_dt = datetime.datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
    relative_td = dateutil.relativedelta.relativedelta(meeting_dt, now)

    denominations = ["years", "months", "days", "hours", "minutes"]
    for denomination in denominations:
        value = getattr(relative_td, denomination)
        if value:
            # If the value is only one, then strip off the plural suffix.
            if value == 1:
                denomination = denomination[:-1]
            return "in %i %s" % (value, denomination)

    return "right now"


class ReminderV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a reminder is sent.
    """

    topic = "fedocal.reminder"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a reminder is sent",
        "type": "object",
        "properties": {"calendar": CALENDAR, "meeting": MEETING},
        "required": ["calendar", "meeting"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return (
            "Friendly reminder!  The '{meeting}' meeting from "
            "the '{calendar}' calendar starts {timestring}".format(
                meeting=self.body["meeting"]["meeting_name"],
                calendar=self.body["calendar"]["calendar_name"],
                timestring=_casual_timedelta_string(self.body["meeting"]),
            )
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return (
            "Remember about the meeting '{meeting}' from "
            "the '{calendar}' calendar".format(
                meeting=self.body["meeting"]["meeting_name"],
                calendar=self.body["calendar"]["calendar_name"],
            )
        )


class CalendarNewV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a calendar is created.
    """

    topic = "fedocal.calendar.new"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a calendar is created",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "calendar": CALENDAR},
        "required": ["calendar", "agent"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has created a new calendar {calendar}".format(
            user=self.body["agent"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class CalendarUpdateV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a calendar is updated.
    """

    topic = "fedocal.calendar.update"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a calendar is updated",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "calendar": CALENDAR},
        "required": ["calendar", "agent"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has updated a calendar {calendar}".format(
            user=self.body["agent"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class CalendarUploadV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when meetings have been uploaded into the calendar.
    """

    topic = "fedocal.calendar.upload"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when meetings have been "
        "uploaded into the calendar",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "calendar": CALENDAR},
        "required": ["calendar", "agent"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has uploaded meetings in the calendar {calendar}".format(
            user=self.body["agent"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class CalendarDeleteV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a calendar is deleted.
    """

    topic = "fedocal.calendar.delete"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a calendar is deleted",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "calendar": CALENDAR},
        "required": ["calendar", "agent"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has deleted the calendar {calendar}".format(
            user=self.body["agent"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class CalendarClearV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a calendar is cleared.
    """

    topic = "fedocal.calendar.clear"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a calendar is cleared",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "calendar": CALENDAR},
        "required": ["calendar", "agent"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has cleared the calendar {calendar}".format(
            user=self.body["agent"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class MeetingNewV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a meeting is created.
    """

    topic = "fedocal.meeting.new"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a meeting is created",
        "type": "object",
        "properties": {
            "agent": {"type": "string"},
            "calendar": CALENDAR,
            "meeting": MEETING,
        },
        "required": ["agent", "calendar", "meeting"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return (
            "{user} has created a new meeting {meeting} in calendar"
            " {calendar}".format(
                user=self.body["agent"],
                meeting=self.body["meeting"]["meeting_name"],
                calendar=self.body["calendar"]["calendar_name"],
            )
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class MeetingUpdateV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a meeting is updated.
    """

    topic = "fedocal.meeting.update"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a meeting is updated",
        "type": "object",
        "properties": {
            "agent": {"type": "string"},
            "calendar": CALENDAR,
            "meeting": MEETING,
        },
        "required": ["agent", "calendar", "meeting"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "{user} has updated meeting {meeting} in calendar" " {calendar}".format(
            user=self.body["agent"],
            meeting=self.body["meeting"]["meeting_name"],
            calendar=self.body["calendar"]["calendar_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)


class MeetingDeleteV1(fedocalMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal when a meeting is deleted.
    """

    topic = "fedocal.meeting.deleted"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a meeting is deleted",
        "type": "object",
        "properties": {
            "agent": {"type": "string"},
            "calendar": CALENDAR,
            "meeting": MEETING,
        },
        "required": ["agent", "calendar", "meeting"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return (
            "{user} has deleted the meeting {meeting} from the calendar"
            " {calendar}".format(
                user=self.body["agent"],
                meeting=self.body["meeting"]["meeting_name"],
                calendar=self.body["calendar"]["calendar_name"],
            )
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return str(self)
