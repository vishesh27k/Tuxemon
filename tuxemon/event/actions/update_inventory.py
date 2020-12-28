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

from tuxemon.db import db
from tuxemon.event import get_npc
from tuxemon.event.eventaction import EventAction
from tuxemon.item.item import decode_inventory


class UpdateInventoryAction(EventAction):
    """Updates the inventory of the npc or player.
    Overwrites the quantity of an item if it's already present, but leaves other items alone.
    """

    name = "update_inventory"
    valid_parameters = [
        (str, "npc_slug"),
        (str, "inventory_slug"),
    ]

    def start(self):
        npc = get_npc(self.context, self.parameters.npc_slug)
        if self.parameters.inventory_slug is None:
            return

        npc.inventory.update(
            decode_inventory(self.context, npc, db.database["inventory"][self.parameters.inventory_slug])
        )
