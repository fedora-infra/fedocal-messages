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

from fedora_messaging import message

import pkg_resources

from .messages import (  # noqa: F401
    CalendarClearV1,
    CalendarDeleteV1,
    CalendarNewV1,
    CalendarUpdateV1,
    CalendarUploadV1,
    MeetingDeleteV1,
    MeetingNewV1,
    MeetingUpdateV1,
    ReminderV1,
)


def get_message_object_from_topic(topic):
    """Returns the Message class corresponding to the topic."""

    output = None

    for entry_point in pkg_resources.iter_entry_points("fedora.messages"):
        cls = entry_point.load()
        if cls().topic == topic:
            output = cls
            break

    if output is None:
        output = message.Message

    return output
