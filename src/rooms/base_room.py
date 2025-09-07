from __future__ import annotations

from typing import List
import pygame as pg


class BaseRoom:
    """Base class for a room (a single area the player can explore).

    Rooms own their local sprites and handle their own update/draw.
    """

    def __init__(self, name: str):
        self.name = name
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.exits = {
            "north": None,
            "south": None,
            "east": None,
            "west": None
        }
        self.connected_rooms = {}

    def enter(self) -> None:
        """Called when the room becomes active."""
        return

    def exit(self) -> None:
        """Called when the room is deactivated."""
        return

    def update(self, dt: float) -> None:
        self.all_sprites.update(dt)

    def draw(self, surface: pg.Surface) -> None:
        self.all_sprites.draw(surface)