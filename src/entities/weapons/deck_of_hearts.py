from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from .base_weapon import BaseWeapon


class HeartDeck(BaseWeapon):
    """A deck of heart suit cards that provides healing and life-steal."""
    
    def __init__(self):
        super().__init__(name="Heart Suit Deck", weapon_type="ranged")
        
        # Set stat modifiers for this weapon
        self.stat_modifiers = EntityStats(
            health=10.0,         # Small HP bonus
            stamina=20.0,        # Better sustain
            movement_speed=0.5,   # Slightly faster
            strength=-5.0,        # Lower base damage
            dexterity=15.0,      # Fast attacks
            crit_chance=10.0,    # Good crit
            defense=-5.0,        # Lower defense
            mana=25.0,           # More mana
            knockback=0.0        # No knockback
        )
        
        # Attack properties
        self.attack_range = 400  # Long range
        self.life_steal = 0.2    # 20% of damage dealt
        self.max_cards = 52      # Full deck
        self.current_cards = 52
        
        # Load sprite (placeholder)
        self.image = pg.Surface((32, 48))
        self.image.fill((255, 192, 203))  # Pink
        self.rect = self.image.get_rect()
        
    def _do_primary_attack(self) -> None:
        """Throw a card that deals damage and heals on hit"""
        if self.current_cards > 0:
            self.current_cards -= 1
            self._throw_card()
        else:
            self._reload_deck()
    
    def _do_special_ability(self) -> None:
        """Fan of cards that provides burst healing"""
        if self.current_cards >= 5:
            self.current_cards -= 5
            self._throw_card_fan()
            # Burst heal for 25% of max health
            if hasattr(self, 'owner'):
                heal_amount = self.owner.stats.health * 0.25
                self.owner.heal(heal_amount)
            
    def get_attack_cooldown(self) -> float:
        """Fast attack speed"""
        return 0.3
        
    def get_ability_cooldown(self) -> float:
        """Medium cooldown for fan ability"""
        return 6.0
        
    def _throw_card(self) -> None:
        """Create and launch a card projectile"""
        # Will implement projectile logic
        pass
        
    def _throw_card_fan(self) -> None:
        """Create and launch multiple card projectiles"""
        # Will implement multi-projectile logic
        pass
        
    def _reload_deck(self) -> None:
        """Reload the deck when empty"""
        self.current_cards = self.max_cards
        # Add reload animation/delay here
