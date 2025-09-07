from __future__ import annotations
import pygame as pg
from core.stats import EntityStats
from core.animation import AnimationManager, create_placeholder_animation
from core.combat import HitBoxManager, HitBox, ProjectileHitBox


class BaseWeapon(pg.sprite.Sprite):
    """Base class for all weapons in the game.
    
    Weapons modify player stats and provide special abilities.
    Both melee and ranged weapons inherit from this class.
    Handles animations and hitboxes for attacks.
    """
    
    def __init__(self, name: str, weapon_type: str = "melee"):
        super().__init__()
        self.name = name
        self.weapon_type = weapon_type  # "melee" or "ranged"
        
        # Base stats modifiers (will be added to player's base stats)
        self.stat_modifiers = EntityStats()
        
        # Cooldown tracking
        self.attack_cooldown = 0.0
        self.ability_cooldown = 0.0
        
        # Animation system
        self.animation_manager = AnimationManager()
        self._setup_animations()
        
        # Combat system
        self.hitbox_manager = HitBoxManager()
        
        # Default rectangle for collision
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        
        # Orientation
        self.facing = pg.math.Vector2(1, 0)  # Default facing right
        
    def update(self, dt: float) -> None:
        """Update weapon state"""
        # Update cooldowns
        self.attack_cooldown = max(0.0, self.attack_cooldown - dt)
        self.ability_cooldown = max(0.0, self.ability_cooldown - dt)
        
        # Update animations
        new_frame = self.animation_manager.update(dt)
        if new_frame:
            self.image = new_frame
            
        # Update hitboxes
        if hasattr(self, 'owner'):
            self.hitbox_manager.update(dt, self.owner.rect.center, self.facing)
            
        # Update facing direction from owner
        if hasattr(self, 'owner'):
            self.facing = self.owner.facing
    
    def primary_attack(self) -> None:
        """Perform the weapon's primary attack"""
        if self.attack_cooldown <= 0:
            self._do_primary_attack()
            self.attack_cooldown = self.get_attack_cooldown()
    
    def special_ability(self) -> None:
        """Perform the weapon's special ability"""
        if self.ability_cooldown <= 0:
            self._do_special_ability()
            self.ability_cooldown = self.get_ability_cooldown()
    
    def get_attack_cooldown(self) -> float:
        """Return the cooldown time for primary attack"""
        return 0.5  # Default half second cooldown
        
    def get_ability_cooldown(self) -> float:
        """Return the cooldown time for special ability"""
        return 5.0  # Default 5 second cooldown
        
    def _setup_animations(self) -> None:
        """Setup weapon animations. Override in child classes."""
        # Create placeholder animations until we have assets
        idle = create_placeholder_animation(
            (200, 200, 200), (32, 32), frames=1)
        attack = create_placeholder_animation(
            (255, 0, 0), (48, 32), frames=4)
        special = create_placeholder_animation(
            (0, 255, 0), (64, 32), frames=6)
            
        self.animation_manager.add_animation("idle", idle, 0.1, True)
        self.animation_manager.add_animation("attack", attack, 0.05, False)
        self.animation_manager.add_animation("special", special, 0.08, False)
        
        # Start with idle animation
        self.animation_manager.play("idle")
        
    def create_melee_hitbox(self, damage: float, width: int, height: int,
                         offset: tuple[int, int] = (0, 0), duration: float = 0.1) -> None:
        """Create a melee attack hitbox."""
        hitbox = HitBox(
            self.rect.centerx, self.rect.centery,
            width, height, damage,
            knockback=self.stat_modifiers.knockback,
            duration=duration,
            offset=offset
        )
        self.hitbox_manager.add_hitbox(hitbox)
        
    def create_projectile(self, damage: float, width: int, height: int,
                       speed: float, direction: pg.math.Vector2,
                       max_distance: float = 400, duration: float = 2.0) -> None:
        """Create a projectile hitbox."""
        projectile = ProjectileHitBox(
            self.rect.centerx, self.rect.centery,
            width, height, damage, speed, direction,
            max_distance=max_distance, duration=duration
        )
        self.hitbox_manager.add_hitbox(projectile)
        """Return the cooldown time for special ability"""
        return 5.0  # Default 5 second cooldown
    
    def _do_primary_attack(self) -> None:
        """Implement in child classes"""
        raise NotImplementedError
        
    def _do_special_ability(self) -> None:
        """Implement in child classes"""
        raise NotImplementedError

    def get_stat_modifiers(self) -> EntityStats:
        """Get the stat modifications this weapon provides"""
        return self.stat_modifiers.copy()
