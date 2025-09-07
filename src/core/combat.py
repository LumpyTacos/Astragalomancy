from __future__ import annotations
import pygame as pg
from typing import List, Tuple


class HitBox(pg.Rect):
    """A rectangle that represents an attack's area of effect."""
    
    def __init__(self, x: int, y: int, width: int, height: int, 
                 damage: float, knockback: float = 0, 
                 duration: float = 0.1, offset: Tuple[int, int] = (0, 0)):
        super().__init__(x, y, width, height)
        self.damage = damage
        self.knockback = knockback
        self.duration = duration
        self.time_alive = 0
        self.offset = pg.math.Vector2(offset)
        self.active = True
        
    def update(self, dt: float, owner_pos: Tuple[int, int], 
               owner_facing: pg.math.Vector2) -> None:
        """Update hitbox position and lifetime."""
        if not self.active:
            return
            
        # Update position based on owner and facing direction
        rotated_offset = pg.math.Vector2(self.offset).rotate_rad(
            owner_facing.angle_to(pg.math.Vector2(1, 0)))
        self.center = (owner_pos[0] + rotated_offset.x, 
                      owner_pos[1] + rotated_offset.y)
        
        # Update lifetime
        self.time_alive += dt
        if self.time_alive >= self.duration:
            self.active = False


class ProjectileHitBox(HitBox):
    """A hitbox that moves independently of its owner."""
    
    def __init__(self, x: int, y: int, width: int, height: int, 
                 damage: float, speed: float, direction: pg.math.Vector2,
                 max_distance: float = 400, **kwargs):
        super().__init__(x, y, width, height, damage, **kwargs)
        self.speed = speed
        self.direction = direction.normalize()
        self.max_distance = max_distance
        self.distance_traveled = 0
        
    def update(self, dt: float, owner_pos: Tuple[int, int], 
               owner_facing: pg.math.Vector2) -> None:
        """Update projectile position and check if it should despawn."""
        if not self.active:
            return
            
        # Move projectile
        movement = self.direction * self.speed * dt
        self.x += movement.x
        self.y += movement.y
        
        # Track distance
        self.distance_traveled += movement.length()
        if self.distance_traveled >= self.max_distance:
            self.active = False
            
        # Update lifetime
        self.time_alive += dt
        if self.time_alive >= self.duration:
            self.active = False


class HitBoxManager:
    """Manages active hitboxes for an entity."""
    
    def __init__(self):
        self.hitboxes: List[HitBox] = []
        
    def add_hitbox(self, hitbox: HitBox) -> None:
        """Add a new hitbox."""
        self.hitboxes.append(hitbox)
        
    def update(self, dt: float, owner_pos: Tuple[int, int], 
               owner_facing: pg.math.Vector2) -> None:
        """Update all hitboxes and remove inactive ones."""
        for hitbox in self.hitboxes[:]:  # Create copy for safe removal
            hitbox.update(dt, owner_pos, owner_facing)
            if not hitbox.active:
                self.hitboxes.remove(hitbox)
                
    def clear(self) -> None:
        """Remove all hitboxes."""
        self.hitboxes.clear()
        
    def get_active_hitboxes(self) -> List[HitBox]:
        """Get list of active hitboxes."""
        return [h for h in self.hitboxes if h.active]
