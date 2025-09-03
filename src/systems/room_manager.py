from __future__ import annotations

from typing import Dict
import pygame as pg

from src.rooms.base_room import BaseRoom


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

