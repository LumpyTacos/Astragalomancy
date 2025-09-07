from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class SpadeDeck(BaseWeapon):
    """A deck of spade cards focused on high damage and critical hits."""
    
    def __init__(self):
        super().__init__(name="Spade Suit Deck", weapon_type="ranged")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=-5.0,         # Glass cannon penalty
            stamina=10.0,        # Some stamina
            movement_speed=0.3,   # Slight speed boost
            strength=0.0,         # No base strength
            dexterity=20.0,      # Very fast attacks
            crit_chance=25.0,    # Highest crit chance
            defense=-10.0,       # Low defense
            mana=15.0,           # Some mana
            knockback=0.0        # No knockback
        )
        
        # Attack properties
        self.attack_range = 400  # Long range
        self.max_cards = 52
        self.current_cards = 52
        self.piercing_chance = 0.3  # 30% chance for cards to pierce
        
        # Load sprite (placeholder)
        self.image = pg.Surface((32, 48))
        self.image.fill((0, 0, 0))  # Black
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Throw a card with high crit chance"""
        if self.current_cards > 0:
            self.current_cards -= 1
            self._throw_card()
        else:
            self._reload_deck()
    
    def _do_special_ability(self) -> None:
        """Rain of piercing cards"""
        if self.current_cards >= 10 and hasattr(self, 'owner'):
            self.current_cards -= 10
            # Create multiple piercing projectiles
            for _ in range(10):
                self._throw_piercing_card()
            
    def get_attack_cooldown(self) -> float:
        """Fast attack speed"""
        return 0.25
        
    def get_ability_cooldown(self) -> float:
        """Long cooldown for powerful ability"""
        return 12.0
        
    def _throw_card(self) -> None:
        """Create and launch a card projectile"""
        # Will implement projectile logic
        pass
        
    def _throw_piercing_card(self) -> None:
        """Create and launch a piercing card projectile"""
        # Will implement piercing projectile logic
        pass
        
    def _reload_deck(self) -> None:
        """Reload the deck when empty"""
        self.current_cards = self.max_cards
        # Add reload animation/delay here
