from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class DualCigarKnives(BaseWeapon):
    """Dual-wielded knives that apply burning damage over time."""
    
    def __init__(self):
        super().__init__(name="Ciggy & Ciggs", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=-10.0,        # Glass cannon penalty
            stamina=25.0,        # Good stamina for mobility
            movement_speed=1.0,   # Fast movement
            strength=8.0,         # Low base damage
            dexterity=25.0,      # Very fast attacks
            crit_chance=20.0,    # High crit
            defense=-10.0,       # Low defense
            mana=15.0,           # Some mana
            knockback=0.0        # No knockback
        )
        
        # Attack properties
        self.attack_range = 48   # Short range
        self.burn_duration = 3.0 # DoT duration
        self.burn_damage = 5.0   # Damage per second
        self.dash_distance = 200 # Dash ability range
        
        # Load sprite (placeholder)
        self.image = pg.Surface((32, 32))
        self.image.fill((128, 70, 27))  # Dark brown
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Quick knife strikes that apply burn"""
        # Get enemies in close range
        hit_enemies = self._get_enemies_in_range()
        
        # Apply damage and burn
        for enemy in hit_enemies:
            damage = self.stat_modifiers.strength
            enemy.take_damage(damage)
            self._apply_burn(enemy)
    
    def _do_special_ability(self) -> None:
        """Dash through enemies, applying burn to all hit"""
        if hasattr(self, 'owner') and self.owner.stats.stamina >= 30:
            self.owner.stats.stamina -= 30
            self._perform_dash()
            
    def get_attack_cooldown(self) -> float:
        """Very fast attack speed"""
        return 0.2
        
    def get_ability_cooldown(self) -> float:
        """Short cooldown for dash"""
        return 3.0
        
    def _get_enemies_in_range(self) -> list:
        """Helper to find enemies in melee range"""
        # Will implement enemy detection logic
        return []
        
    def _apply_burn(self, enemy) -> None:
        """Apply burning status effect"""
        # Will implement DoT system
        pass
        
    def _perform_dash(self) -> None:
        """Execute dash attack"""
        # Will implement dash movement and damage
