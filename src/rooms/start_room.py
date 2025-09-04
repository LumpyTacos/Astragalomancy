from __future__ import annotations

import pygame as pg

from src.core import config
from src.entities.player import Player
from .base_room import BaseRoom


class StartRoom(BaseRoom):
    """A simple starting room with a player and border walls."""

    def __init__(self):
        super().__init__(name="StartRoom")

        # Create simple border walls as static sprites (visual + collision-ready)
        thickness = 24
        width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT

        # Create wall surfaces
        top = pg.Surface((width, thickness))
        top.fill(config.WALL_COLOR)
        bottom = pg.Surface((width, thickness))
        bottom.fill(config.WALL_COLOR)
        left = pg.Surface((thickness, height))
        left.fill(config.WALL_COLOR)
        right = pg.Surface((thickness, height))
        right.fill(config.WALL_COLOR)

        self.top_wall = pg.sprite.Sprite()
        self.top_wall.image = top
        self.top_wall.rect = top.get_rect(topleft=(0, 0))
        self.bottom_wall = pg.sprite.Sprite()
        self.bottom_wall.image = bottom
        self.bottom_wall.rect = bottom.get_rect(bottomleft=(0, height))
        self.left_wall = pg.sprite.Sprite()
        self.left_wall.image = left
        self.left_wall.rect = left.get_rect(topleft=(0, 0))
        self.right_wall = pg.sprite.Sprite()
        self.right_wall.image = right
        self.right_wall.rect = right.get_rect(topright=(width, 0))

        self.walls.add(self.top_wall, self.bottom_wall, self.left_wall, self.right_wall)
        self.all_sprites.add(self.walls)

        # Spawn player near center
        start_x = width // 2 - config.TILE_SIZE // 2
        start_y = height // 2 - config.TILE_SIZE // 2
        self.player = Player((start_x, start_y))
        self.all_sprites.add(self.player)

    def update(self, dt: float) -> None:
        super().update(dt)
        # Future: resolve collisions between player and walls, enemies, pickups