from __future__ import annotations

from typing import Tuple
import pygame as pg

from src.core import config
from .base import BaseEntity


class Player(BaseEntity):
    """Controllable player character.

    Movement is velocity-based with simple screen bounds clamping for now.
    Extend this with stats, dice/cards, and item effects later.
    """

    def __init__(self, position: Tuple[int, int]):
        size = (config.TILE_SIZE, config.TILE_SIZE)
        super().__init__(position, size, config.PLAYER_COLOR)

        self.speed_pixels_per_second = 240.0
        self.velocity = pg.Vector2(0, 0)

    def handle_input(self) -> None:
        keys = pg.key.get_pressed()
        x = 0
        y = 0
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            x -= 1
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            x += 1
        if keys[pg.K_w] or keys[pg.K_UP]:
            y -= 1
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            y += 1

        self.velocity.update(x, y)
        if self.velocity.length_squared() > 0:
            self.velocity = self.velocity.normalize()
        
    def update(self, dt: float) -> None:
        self.handle_input()
        displacement = self.velocity * self.speed_pixels_per_second * dt
        self.rect.x += int(displacement.x)
        self.rect.y += int(displacement.y)

        # Clamp to screen bounds for now (until we have collision with walls)
        self.rect.clamp_ip(pg.Rect(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

