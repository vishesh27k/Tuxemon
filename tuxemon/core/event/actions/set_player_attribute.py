#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from tuxemon.core.event.actions.common import CommonAction
from tuxemon.core.event.eventaction import EventAction


class SetPlayerAttributeAction(EventAction):
    """Sets the given attribute of the player character to the given value.

    Valid Parameters: attribute, value
    """

    name = "set_player_attribute"
    valid_parameters = [(str, "npc_slug"), (str, "name"), (str, "value")]

    def start(self):
        attribute = self.parameters[0]
        value = self.parameters[1]
        CommonAction.set_character_attribute(self.session.player, attribute, value)