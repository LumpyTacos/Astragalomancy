from __future__ import annotations

from typing import Tuple
import pygame as pg


class BaseEntity(pg.sprite.Sprite):
    """Base class for all game entities.

    Provides a pygame Sprite with a rect and image, and basic update/draw hooks.
    Keep this simple and readable so specialized entities can extend it.
    """

    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], color: Tuple[int, int, int]):
        super().__init__()
        self.image = pg.Surface(size, pg.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)

    def update(self, dt: float) -> None:  # dt in seconds
        """Advance internal state. Override in subclasses."""
        return

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.image, self.rect)