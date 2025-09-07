from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class DiamondDeck(BaseWeapon):
    """A deck of diamond cards focusing on defense and buffs."""
    
    def __init__(self):
        super().__init__(name="Diamond Suit Deck", weapon_type="ranged")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=25.0,         # High health
            stamina=15.0,        # Good stamina
            movement_speed=0.0,   # Normal speed
            strength=-10.0,       # Low damage
            dexterity=10.0,      # Average speed
            crit_chance=5.0,     # Low crit
            defense=25.0,        # High defense
            mana=30.0,           # High mana
            knockback=0.0        # No knockback
        )
        
        # Attack properties
        self.attack_range = 300  # Medium range
        self.max_cards = 52
        self.current_cards = 52
        self.shield_health = 50  # Shield hit points
        self.has_shield = False
        
        # Load sprite (placeholder)
        self.image = pg.Surface((32, 48))
        self.image.fill((135, 206, 235))  # Sky blue
        self.rect = self.image.get_rect()
        
    def update(self, dt: float) -> None:
        """Update shield state"""
        super().update(dt)
        if self.shield_health <= 0:
            self.has_shield = False
    
    def _do_primary_attack(self) -> None:
        """Throw a card that creates temporary shield on hit"""
        if self.current_cards > 0:
            self.current_cards -= 1
            self._throw_card()
        else:
            self._reload_deck()
    
    def _do_special_ability(self) -> None:
        """Create a reflective shield"""
        if hasattr(self, 'owner') and self.owner.stats.mana >= 40:
            self.owner.stats.mana -= 40
            self.has_shield = True
            self.shield_health = 50
            
    def get_attack_cooldown(self) -> float:
        """Average attack speed"""
        return 0.5
        
    def get_ability_cooldown(self) -> float:
        """Medium cooldown for shield"""
        return 8.0
        
    def take_damage(self, amount: float) -> float:
        """Handle damage reduction with shield"""
        if self.has_shield:
            # Shield absorbs damage
            self.shield_health -= amount
            if self.shield_health > 0:
                return 0  # No damage taken
            else:
                # Shield breaks, return remaining damage
                overflow = abs(self.shield_health)
                self.has_shield = False
                return overflow
        return amount
        
    def _throw_card(self) -> None:
        """Create and launch a defensive card projectile"""
        # Will implement projectile logic
        pass
        
    def _reload_deck(self) -> None:
        """Reload the deck when empty"""
        self.current_cards = self.max_cards
        # Add reload animation/delay here
