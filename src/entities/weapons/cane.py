from __future__ import annotations
import random
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class Cane(BaseWeapon):
    """A stylish cane that excels at crowd control."""
    
    def __init__(self):
        super().__init__(name="Swagger Scepter", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=15.0,         # Decent health
            stamina=20.0,        # Good stamina
            movement_speed=0.5,   # Slightly faster
            strength=12.0,        # Average damage
            dexterity=5.0,       # Average speed
            crit_chance=10.0,    # Decent crit
            defense=15.0,        # Good defense
            mana=25.0,           # High mana for abilities
            knockback=1.5        # Strong knockback
        )
        
        # Attack properties
        self.attack_range = 72   # Good range for a cane
        self.stun_duration = 1.5 # Base stun duration
        self.trip_chance = 0.3   # 30% chance to trip enemies
        
        # Load sprite (placeholder)
        self.image = pg.Surface((8, 64))
        self.image.fill((255, 215, 0))  # Gold color
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Elegant cane strike with chance to trip"""
        # Get enemies in arc
        hit_enemies = self._get_enemies_in_arc()
        
        # Apply damage and effects
        for enemy in hit_enemies:
            damage = self.stat_modifiers.strength
            enemy.take_damage(damage)
            
            # Chance to trip
            if random.random() < self.trip_chance:
                enemy.apply_trip(1.0)  # 1 second trip duration
            
            self._apply_knockback(enemy)
    
    def _do_special_ability(self) -> None:
        """Ground-slam AOE stun"""
        if hasattr(self, 'owner') and self.owner.stats.mana >= 35:
            self.owner.stats.mana -= 35
            
            # Get enemies in radius
            hit_enemies = self._get_enemies_in_radius(120)
            
            # Apply effects
            for enemy in hit_enemies:
                damage = self.stat_modifiers.strength * 0.8
                enemy.take_damage(damage)
                enemy.apply_stun(self.stun_duration)
                self._apply_strong_knockback(enemy)
            
    def get_attack_cooldown(self) -> float:
        """Moderate attack speed"""
        return 0.6
        
    def get_ability_cooldown(self) -> float:
        """Medium cooldown for AOE stun"""
        return 8.0
        
    def _get_enemies_in_arc(self) -> list:
        """Helper to find enemies in cane swing arc"""
        # Will implement enemy detection logic
        return []
        
    def _get_enemies_in_radius(self, radius: float) -> list:
        """Helper to find enemies in circular radius"""
        # Will implement enemy detection logic
        return []
        
    def _apply_knockback(self, enemy) -> None:
        """Apply moderate knockback force"""
        # Will implement knockback physics
        
    def _apply_strong_knockback(self, enemy) -> None:
        """Apply heavy knockback force"""
        # Will implement knockback physics
