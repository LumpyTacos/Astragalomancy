from __future__ import annotations

import pygame as pg
from core import config
from .base_room import BaseRoom


class TreasureRoom(BaseRoom):
    """A room containing treasure and rewards."""
    
    def __init__(self):
        super().__init__(name="TreasureRoom")
        self.treasures = pg.sprite.Group()
        
        # Create the basic room layout
        self._create_walls()
        
        # Add to sprite groups
        self.all_sprites.add(self.treasures)
    
    def _create_walls(self):
        """Create the room's border walls."""
        thickness = 24
        width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        
        # Create wall surfaces
        walls = {
            "top": pg.Surface((width, thickness)),
            "bottom": pg.Surface((width, thickness)),
            "left": pg.Surface((thickness, height)),
            "right": pg.Surface((thickness, height))
        }
        
        for wall in walls.values():
            wall.fill(config.WALL_COLOR)