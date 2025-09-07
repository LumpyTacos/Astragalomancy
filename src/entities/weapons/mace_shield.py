from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class MaceShield(BaseWeapon):
    """A heavy mace shaped like dice that provides high knockback."""
    
    def __init__(self):
        super().__init__(name="Dice Mace & Poker Chip Shield", weapon_type="melee")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=20.0,        # Bonus HP for tank playstyle
            stamina=0.0,
            movement_speed=-0.5, # Slower due to weight
            strength=25.0,       # High damage
            dexterity=-5.0,     # Slower attack speed
            crit_chance=0.0,
            defense=15.0,       # Good defense
            mana=0.0,
            knockback=2.0       # High knockback
        )
        
        # Attack properties
        self.attack_range = 64  # Pixels
        self.attack_arc = 90    # Degrees
        self.swing_speed = 0.3  # Seconds
        
        # Load sprite (placeholder)
        self.image = pg.Surface((48, 48))
        self.image.fill((200, 200, 200))  # Light gray
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Heavy swing that damages and knocks back enemies"""
        # Play attack animation
        self.animation_manager.play("attack", force=True)
        
        # Create hitbox in front of player
        self.create_melee_hitbox(
            damage=self.stat_modifiers.strength,
            width=80,  # Wide arc
            height=60,
            offset=(40, 0),  # Offset forward
            duration=0.15    # Short duration
        )
    
    def _do_special_ability(self) -> None:
        """Ground pound that stuns enemies"""
        # Play special animation
        self.animation_manager.play("special", force=True)
        
        # Create circular AOE hitbox
        self.create_melee_hitbox(
            damage=self.stat_modifiers.strength * 1.5,
            width=256,  # Large circular area
            height=256,
            offset=(0, 0),  # Centered on player
            duration=0.3    # Longer duration for AOE
        )
            
    def get_attack_cooldown(self) -> float:
        """Slower attack speed for heavy weapon"""
        return 1.0
        
    def get_ability_cooldown(self) -> float:
        """Long cooldown for powerful ground pound"""
        return 8.0
        
    def _get_enemies_in_arc(self) -> list:
        """Helper to find enemies in attack arc"""
        # Will implement enemy detection logic
        return []
        
    def _get_enemies_in_radius(self, radius: float) -> list:
        """Helper to find enemies in circular radius"""
        # Will implement enemy detection logic
        return []
        
    def _apply_knockback(self, enemy) -> None:
        """Apply knockback force to enemy"""
        # Will implement knockback physics
