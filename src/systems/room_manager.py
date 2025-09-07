from __future__ import annotations

from typing import Dict
import pygame as pg

from rooms.base_room import BaseRoom
from rooms.combat_room import CombatRoom
from rooms.treasure_room import TreasureRoom


class RoomManager:
    """Tracks and switches between rooms.

    Keeps a reference to the active room and forwards update/draw calls.
    """

    def __init__(self):
        self.rooms: Dict[str, BaseRoom] = {}
        self.active_room: BaseRoom | None = None

    def add_room(self, room: BaseRoom) -> None:
        self.rooms[room.name] = room
        if self.active_room is None:
            self.set_active(room.name)

    def set_active(self, name: str) -> None:
        if self.active_room is not None:
            self.active_room.exit()
        self.active_room = self.rooms[name]
        self.active_room.enter()

    def update(self, dt: float) -> None:
        if self.active_room:
            self.active_room.update(dt)

    def draw(self, surface: pg.Surface) -> None:
        if self.active_room:
            self.active_room.draw(surface)

    def create_dungeon_level(self):
        """Create a new dungeon level with different room types."""
        start_room = StartRoom()
        combat_room = CombatRoom()
        treasure_room = TreasureRoom()

        # Connect rooms
        start_room.exits["east"] = combat_room
        combat_room.exits["west"] = start_room
        combat_room.exits["north"] = treasure_room
        treasure_room.exits["south"] = combat_room

        self.add_room(start_room)
        self.add_room(combat_room)
        self.add_room(treasure_room)