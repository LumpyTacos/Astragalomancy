from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class ClubDeck(BaseWeapon):
    """A deck of club cards specializing in crowd control and knockback."""
    
    def __init__(self):
        super().__init__(name="Club Suit Deck", weapon_type="ranged")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=0.0,          # No health mod
            stamina=15.0,        # Decent stamina
            movement_speed=0.2,   # Small speed boost
            strength=-5.0,        # Low damage
            dexterity=15.0,      # Good attack speed
            crit_chance=5.0,     # Low crit
            defense=5.0,         # Some defense
            mana=20.0,           # Good mana
            knockback=2.0        # High knockback
        )
        
        # Attack properties
        self.attack_range = 350  # Good range
        self.max_cards = 52
        self.current_cards = 52
        self.stun_chance = 0.2   # 20% chance to stun
        self.stun_duration = 1.0 # 1 second stun
        
        # Load sprite (placeholder)
        self.image = pg.Surface((32, 48))
        self.image.fill((0, 100, 0))  # Dark green
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Throw a stunning card"""
        if self.current_cards > 0:
            self.current_cards -= 1
            self._throw_card()
        else:
            self._reload_deck()
    
    def _do_special_ability(self) -> None:
        """Create a tornado of cards"""
        if self.current_cards >= 15 and hasattr(self, 'owner'):
            self.current_cards -= 15
            self._create_card_tornado()
            
    def get_attack_cooldown(self) -> float:
        """Moderate attack speed"""
        return 0.4
        
    def get_ability_cooldown(self) -> float:
        """Long cooldown for tornado"""
        return 10.0
        
    def _throw_card(self) -> None:
        """Create and launch a stunning card projectile"""
        # Will implement projectile logic with stun chance
        pass
        
    def _create_card_tornado(self) -> None:
        """Create a damaging tornado that pulls enemies in"""
        # Will implement tornado entity
        pass
        
    def _reload_deck(self) -> None:
        """Reload the deck when empty"""
        self.current_cards = self.max_cards
        # Add reload animation/delay here
