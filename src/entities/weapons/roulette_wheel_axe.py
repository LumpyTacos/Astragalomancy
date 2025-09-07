from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class RouletteWheelAxe(BaseWeapon):
    """A heavy axe with spinning attacks and high AOE damage."""
    
    def __init__(self):
        super().__init__(name="Rota", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=0.0,          # No health bonus
            stamina=30.0,        # High stamina for spinning
            movement_speed=-0.3,  # Slightly slower
            strength=20.0,        # High damage
            dexterity=-5.0,      # Slower base attacks
            crit_chance=15.0,    # Good crit chance
            defense=5.0,         # Some defense
            mana=10.0,           # Some mana
            knockback=1.5        # Strong knockback
        )
        
        # Attack properties
        self.attack_range = 96   # Wide range
        self.spin_damage = 0.7   # 70% damage during spin
        self.is_spinning = False
        self.spin_duration = 0.0
        
        # Load sprite (placeholder)
        self.image = pg.Surface((64, 64))
        self.image.fill((139, 69, 19))  # Brown
        self.rect = self.image.get_rect()
        
    def update(self, dt: float) -> None:
        """Update spin state"""
        super().update(dt)
        
        if self.is_spinning:
            self.spin_duration -= dt
            if self.spin_duration <= 0:
                self.is_spinning = False
    
    def _do_primary_attack(self) -> None:
        """Heavy axe swing"""
        # Get enemies in wide arc
        hit_enemies = self._get_enemies_in_arc()
        
        # Apply heavy damage
        for enemy in hit_enemies:
            damage = self.stat_modifiers.strength * 1.2  # 120% damage
            enemy.take_damage(damage)
            self._apply_heavy_knockback(enemy)
    
    def _do_special_ability(self) -> None:
        """Start spinning attack"""
        if hasattr(self, 'owner') and self.owner.stats.stamina >= 40:
            self.owner.stats.stamina -= 40
            self.is_spinning = True
            self.spin_duration = 3.0  # Spin for 3 seconds
            
    def get_attack_cooldown(self) -> float:
        """Slow base attack speed"""
        return 0.8
        
    def get_ability_cooldown(self) -> float:
        """Long cooldown for spin"""
        return 10.0
        
    def _get_enemies_in_arc(self) -> list:
        """Helper to find enemies in axe swing arc"""
        # Will implement enemy detection logic
        return []
        
    def _apply_heavy_knockback(self, enemy) -> None:
        """Apply strong knockback force"""
        # Will implement knockback physics
