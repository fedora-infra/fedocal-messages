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

"""Unit tests for common properties of the message schemas."""

from ..messages import ReminderV1
from .utils import DUMMY_CALENDAR, DUMMY_MEETING


def test_properties():
    """Assert some properties are correct."""
    body = {"meeting": DUMMY_MEETING, "calendar": DUMMY_CALENDAR, "agent": "dummy_user"}
    message = ReminderV1(body=body)

    assert message.app_name == "fedocal"
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/fedocal.png"
    assert message.agent == "dummy_user"
    assert (
        message.agent_avatar == "https://seccdn.libravatar.org/avatar/"
        "b0ec8f140ba7eee8f4bfc7955858bc43c14fdd83edadf7b3819459efcaa5c690?s=64&d=retro"
    )
    assert message.usernames == ["dummy_user"]
