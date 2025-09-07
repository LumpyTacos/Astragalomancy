from __future__ import annotations

from typing import Tuple
import pygame as pg

from core import config
from core.stats import EntityStats
from .base import BaseEntity
from .weapons.base_weapon import BaseWeapon


class Player(BaseEntity):
    """Controllable player character.
    
    Has stats, can equip weapons, and handles combat interactions.
    Movement is velocity-based with simple screen bounds clamping for now.
    """

    def __init__(self, position: Tuple[int, int]):
        size = (config.TILE_SIZE, config.TILE_SIZE)
        super().__init__(position, size, config.PLAYER_COLOR)

        # Stats setup
        self.base_stats = config.PLAYER_STATS.copy()
        self.stats = self.base_stats.copy()  # Current stats with modifiers
        
        # Movement
        self.velocity = pg.Vector2(0, 0)
        self.facing = pg.Vector2(1, 0)  # Default facing right
        
        # Combat
        self.weapon: BaseWeapon | None = None
        self.attack_pressed = False
        self.special_pressed = False

    def handle_input(self) -> None:
        # Movement input
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
            self.facing = self.velocity.copy()
            
        # Combat input
        mouse_buttons = pg.mouse.get_pressed()
        if mouse_buttons[0]:  # Left click
            if not self.attack_pressed and self.weapon:
                self.weapon.primary_attack()
                self.attack_pressed = True
        else:
            self.attack_pressed = False
            
        if mouse_buttons[2]:  # Right click
            if not self.special_pressed and self.weapon:
                self.weapon.special_ability()
                self.special_pressed = True
        else:
            self.special_pressed = False
        
    def update(self, dt: float) -> None:
        """Update player state"""
        self.handle_input()
        
        # Movement update
        speed = self.stats.movement_speed * config.TILE_SIZE * 5  # Base speed conversion
        displacement = self.velocity * speed * dt
        self.rect.x += int(displacement.x)
        self.rect.y += int(displacement.y)
        
        # Clamp to screen bounds for now
        self.rect.clamp_ip(pg.Rect(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        
        # Update weapon if equipped
        if self.weapon:
            self.weapon.update(dt)
            # Update weapon position to follow player
            self.weapon.rect.center = self.rect.center
            
    def equip_weapon(self, weapon: BaseWeapon) -> None:
        """Equip a new weapon and apply its stat modifiers"""
        # Remove old weapon modifiers if exists
        if self.weapon:
            self._remove_weapon_modifiers(self.weapon)
            
        # Set new weapon
        self.weapon = weapon
        self.weapon.owner = self  # Give weapon reference to player
        
        # Apply new weapon modifiers
        self._apply_weapon_modifiers(weapon)
        
    def _apply_weapon_modifiers(self, weapon: BaseWeapon) -> None:
        """Apply weapon stat modifiers to player stats"""
        modifiers = weapon.get_stat_modifiers()
        self.stats.health += modifiers.health
        self.stats.stamina += modifiers.stamina
        self.stats.movement_speed += modifiers.movement_speed
        self.stats.strength += modifiers.strength
        self.stats.dexterity += modifiers.dexterity
        self.stats.crit_chance += modifiers.crit_chance
        self.stats.defense += modifiers.defense
        self.stats.mana += modifiers.mana
        self.stats.knockback += modifiers.knockback
        
    def _remove_weapon_modifiers(self, weapon: BaseWeapon) -> None:
        """Remove weapon stat modifiers from player stats"""
        modifiers = weapon.get_stat_modifiers()
        self.stats.health -= modifiers.health
        self.stats.stamina -= modifiers.stamina
        self.stats.movement_speed -= modifiers.movement_speed
        self.stats.strength -= modifiers.strength
        self.stats.dexterity -= modifiers.dexterity
        self.stats.crit_chance -= modifiers.crit_chance
        self.stats.defense -= modifiers.defense
        self.stats.mana -= modifiers.mana
        self.stats.knockback -= modifiers.knockback
        
    def heal(self, amount: float) -> None:
        """Heal the player"""
        self.stats.health = min(self.base_stats.health, self.stats.health + amount)
        
    def take_damage(self, amount: float) -> None:
        """Take damage, considering defense"""
        if self.weapon and hasattr(self.weapon, 'take_damage'):
            # Let weapon handle damage first (e.g., shields)
            amount = self.weapon.take_damage(amount)
            
        actual_damage = max(0, amount - self.stats.defense * 0.5)
        self.stats.health -= actual_damage