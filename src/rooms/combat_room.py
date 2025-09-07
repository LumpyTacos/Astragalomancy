from __future__ import annotations
import random
import pygame as pg

from core import config
from entities.enemy import Enemy  # You'll need to create this
from .base_room import BaseRoom


class CombatRoom(BaseRoom):
    """A room where combat encounters take place."""
    
    def __init__(self):
        super().__init__(name="CombatRoom")
        self.enemies = pg.sprite.Group()
        self.spawn_points = []
        
        # Create the basic room layout
        self._create_walls()
        self._create_spawn_points()
        
        # Spawn initial enemies
        self.spawn_enemies(3)  # Start with 3 enemies
        
        # Add to sprite groups
        self.all_sprites.add(self.enemies)
    
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
    
    def _create_spawn_points(self):
        """Create potential enemy spawn locations."""
        margin = 100  # Keep enemies away from walls
        width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        
        # Create a grid of spawn points
        for x in range(margin, width - margin, 100):
            for y in range(margin, height - margin, 100):
                self.spawn_points.append((x, y))
    
    def spawn_enemies(self, count: int):
        """Spawn a mix of different enemy types"""
        enemy_types = ["dealer", "mafia_boss", "thug"]  # Example enemy types
        available_points = self.spawn_points.copy()
        
        for _ in range(count):
            if not available_points:
                break
                
            pos = random.choice(available_points)
            available_points.remove(pos)
            
            enemy_type = random.choice(enemy_types)
            enemy = Enemy(pos, enemy_type)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def update(self, dt: float):
        super().update(dt)
        
        # Check for defeated enemies
        for enemy in self.enemies:
            if enemy.health <= 0:
                enemy.kill()
        
        # Spawn new enemies if room is empty
        if len(self.enemies) == 0:
            self.spawn_enemies(random.randint(2, 4))