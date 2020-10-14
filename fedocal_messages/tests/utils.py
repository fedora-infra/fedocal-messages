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

"""Utilities for the unit tests."""


DUMMY_CALENDAR = {
    "calendar_name": "test_calendar",
    "calendar_contact": "foo@example.com",
    "calendar_description": "A test calendar",
    "calendar_editor_group": None,
    "calendar_admin_group": "syadmin",
    "calendar_status": "active",
}

DUMMY_MEETING = {
    "meeting_time_start": "12:00:00",
    "meeting_name": "wat",
    "meeting_id": 42,
    "meeting_time_stop": "12:00:00",
    "calendar_name": "awesome",
    "meeting_location": None,
    "meeting_date_end": "2013-09-21",
    "meeting_timezone": "UTC",
    "meeting_manager": ["ralph"],
    "meeting_date": "2013-09-20",
    "meeting_information": "awesome",
    "meeting_region": None,
}
