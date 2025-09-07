from __future__ import annotations
import random
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class Greatsword(BaseWeapon):
    """A massive sword with high risk-reward mechanics."""
    
    def __init__(self):
        super().__init__(name="Gambler's Greatsword", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=-20.0,        # High risk
            stamina=10.0,        # Some stamina
            movement_speed=-1.0,  # Very slow
            strength=35.0,        # Extremely high damage
            dexterity=-10.0,     # Very slow attacks
            crit_chance=25.0,    # Massive crit chance
            defense=0.0,         # No defense bonus
            mana=0.0,            # No mana needed
            knockback=2.0        # Strong knockback
        )
        
        # Attack properties
        self.attack_range = 120  # Very long range
        self.charge_level = 0.0  # For charged attacks
        self.max_charge = 2.0    # Maximum charge time
        self.charge_multiplier = 2.5  # Damage multiplier at max charge
        
        # Load sprite (placeholder)
        self.image = pg.Surface((96, 16))
        self.image.fill((64, 64, 64))  # Dark gray
        self.rect = self.image.get_rect()
        
    def update(self, dt: float) -> None:
        """Update charge state"""
        super().update(dt)
        if hasattr(self, 'is_charging') and self.is_charging:
            self.charge_level = min(self.max_charge, self.charge_level + dt)
    
    def _do_primary_attack(self) -> None:
        """Heavy sword swing with charge mechanic"""
        # Calculate damage multiplier based on charge
        multiplier = 1.0 + (self.charge_level / self.max_charge * (self.charge_multiplier - 1.0))
        
        # Get enemies in wide arc
        hit_enemies = self._get_enemies_in_arc()
        
        # Apply massive damage
        for enemy in hit_enemies:
            damage = self.stat_modifiers.strength * multiplier
            # 50% chance to deal double damage
            if random.random() < 0.5:
                damage *= 2
            enemy.take_damage(damage)
            self._apply_heavy_knockback(enemy)
        
        # Reset charge
        self.charge_level = 0.0
        self.is_charging = False
    
    def _do_special_ability(self) -> None:
        """All-in attack that risks self-damage"""
        if hasattr(self, 'owner') and self.owner.stats.health > 10:
            # Risk 20% of current health for massive damage
            health_cost = self.owner.stats.health * 0.2
            self.owner.take_damage(health_cost)
            
            # Get enemies in 360-degree area
            hit_enemies = self._get_enemies_in_radius(150)
            
            # Deal massive damage based on health sacrificed
            for enemy in hit_enemies:
                damage = health_cost * 3  # 300% of sacrificed health as damage
                enemy.take_damage(damage)
                self._apply_heavy_knockback(enemy)
            
    def get_attack_cooldown(self) -> float:
        """Very slow attack speed"""
        return 1.2
        
    def get_ability_cooldown(self) -> float:
        """Long cooldown for all-in attack"""
        return 15.0
        
    def start_charging(self) -> None:
        """Begin charging an attack"""
        self.is_charging = True
        self.charge_level = 0.0
        
    def _get_enemies_in_arc(self) -> list:
        """Helper to find enemies in massive swing arc"""
        # Will implement enemy detection logic
        return []
        
    def _get_enemies_in_radius(self, radius: float) -> list:
        """Helper to find enemies in circular radius"""
        # Will implement enemy detection logic
        return []
        
    def _apply_heavy_knockback(self, enemy) -> None:
        """Apply massive knockback force"""
        # Will implement knockback physics
