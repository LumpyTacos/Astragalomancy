from __future__ import annotations
import pygame as pg
from .base import BaseEntity


class Enemy(BaseEntity):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        
        # Create simple enemy sprite
        self.image = pg.Surface((32, 32))
        self.image.fill((255, 0, 0))  # Red square for now
        self.rect = self.image.get_rect(center=pos)
        
        # Enemy properties
        self.health = 100
        self.speed = 2
        self.damage = 10
        
    def update(self, dt: float):
        # Basic AI: Move towards player if in range
        if hasattr(self.room, 'player'):
            player = self.room.player
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            
            # Normalize movement
            length = (dx * dx + dy * dy) ** 0.5
            if length > 0:
                dx = dx / length * self.speed
                dy = dy / length * self.speed
                
                self.rect.x += dx
                self.rect.y += dy
    
    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            self.kill()