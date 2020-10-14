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
from fedora_messaging.schema_utils import user_avatar_url


SCHEMA_URL = "http://fedoraproject.org/message-schema/"

MEETING = {
    "type": "object",
    "properties": {
        "meeting_id": {"type": "number"},
        "meeting_name": {"type": "string"},
        "meeting_manager": {"type": "array", "items": {"type": ["string", "null"]}},
        "meeting_date": {"type": "string"},
        "meeting_date_end": {"type": "string"},
        "meeting_time_start": {"type": "string"},
        "meeting_time_stop": {"type": "string"},
        "meeting_timezone": {"type": "string"},
        "meeting_information": {"type": ["string", "null"]},
        "meeting_location": {"type": ["string", "null"]},
        "calendar_name": {"type": "string"},
    },
    "required": [
        "meeting_id",
        "meeting_name",
        "meeting_manager",
        "meeting_date",
        "meeting_date_end",
        "meeting_time_start",
        "meeting_time_stop",
        "meeting_timezone",
        "meeting_information",
        "meeting_location",
        "calendar_name",
    ],
}

CALENDAR = {
    "type": "object",
    "properties": {
        "calendar_name": {"type": "string"},
        "calendar_contact": {"type": "string"},
        "calendar_description": {"type": ["string", "null"]},
        "calendar_editor_group": {"type": ["string", "null"]},
        "calendar_admin_group": {"type": ["string", "null"]},
        "calendar_status": {"type": "string"},
    },
    "required": [
        "calendar_name",
        "calendar_contact",
        "calendar_description",
        "calendar_editor_group",
        "calendar_admin_group",
        "calendar_status",
    ],
}


class fedocalMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by fedocal.
    """

    @property
    def app_name(self):
        return "fedocal"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/fedocal.png"

    @property
    def agent(self):
        return self.body.get("agent")

    @property
    def agent_avatar(self):
        return user_avatar_url(self.agent)

    @property
    def usernames(self):
        if self.agent:
            return [self.agent]
        else:
            return []

    @property
    def url(self):
        try:
            return self.body["thing"]["url"]
        except KeyError:
            return None
