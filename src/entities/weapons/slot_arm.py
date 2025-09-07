from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class SlotMachineHandle(BaseWeapon):
    """A balanced sword-like weapon with a ranged energy slash ability."""
    
    def __init__(self):
        super().__init__(name="Slot Arm", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=0.0,          # No health bonus
            stamina=15.0,        # Decent stamina
            movement_speed=0.0,   # Normal speed
            strength=15.0,        # Good damage
            dexterity=10.0,      # Decent attack speed
            crit_chance=7.5,     # Average crit
            defense=10.0,        # Average defense
            mana=15.0,           # Some mana for abilities
            knockback=0.5        # Light knockback
        )
        
        # Attack properties
        self.attack_range = 80   # Medium range
        self.slash_damage = 1.2  # 120% of base damage for energy slash
        
        # Load sprite (placeholder)
        self.image = pg.Surface((48, 8))
        self.image.fill((192, 192, 192))  # Silver
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Standard sword swing"""
        # Get enemies in swing arc
        hit_enemies = self._get_enemies_in_arc()
        
        # Apply damage
        for enemy in hit_enemies:
            damage = self.stat_modifiers.strength
            enemy.take_damage(damage)
            self._apply_light_knockback(enemy)
    
    def _do_special_ability(self) -> None:
        """Energy slash projectile"""
        if hasattr(self, 'owner') and self.owner.stats.mana >= 25:
            self.owner.stats.mana -= 25
            self._create_energy_slash()
            
    def get_attack_cooldown(self) -> float:
        """Balanced attack speed"""
        return 0.5
        
    def get_ability_cooldown(self) -> float:
        """Medium cooldown for energy slash"""
        return 4.0
        
    def _get_enemies_in_arc(self) -> list:
        """Helper to find enemies in sword swing arc"""
        # Will implement enemy detection logic
        return []
        
    def _create_energy_slash(self) -> None:
        """Create and launch energy slash projectile"""
        # Will implement projectile logic
        pass
        
    def _apply_light_knockback(self, enemy) -> None:
        """Apply small knockback force"""
        # Will implement knockback physics
