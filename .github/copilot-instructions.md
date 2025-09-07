# Astragalomancy AI Development Guide

## Project Overview
Astragalomancy is a roguelike dungeon crawler that combines gambling mechanics (dice, cards) with action combat. The game features a unified weapon system where player abilities and stats are determined by equipped weapons and modifiers.

## Core Systems Architecture

### Weapon System
- All weapons inherit from `BaseWeapon` class
- Weapons modify the entity's base stats (defined in `core/stats.py`)
- Two main categories implemented through same interface:
  - Melee (e.g., Dice Mace, Slot Machine Handle)
  - Ranged (e.g., Card Decks)

### Stats System (`core/stats.py`)
Core stats affected by weapons and modifiers:
```python
EntityStats(
    health=100.0,        # Base health
    stamina=100.0,       # Energy for special moves
    movement_speed=3.0,  # Base movement
    strength=10.0,       # Base damage
    dexterity=10.0,     # Attack speed/damage for ranged
    crit_chance=5.0,    # Accuracy and crit
    defense=10.0,       # Damage reduction
    mana=100.0,         # Special ability resource
    knockback=0.0       # Melee pushback force
)
```

### Gambling Mechanics

#### Dice System
- Dice are consumable power-ups with risk/reward effects
- Each die has 6 faces with unique effects
- Effects can modify:
  - Player stats
  - Room properties
  - Enemy behaviors
  - Card draw chances

#### Card System
- Cards provide passive and active abilities
- Four suits with different specialties:
  - ♥ Hearts: Healing/Life-steal
  - ♠ Spades: Damage/Critical hits
  - ♣ Clubs: Crowd control
  - ♦ Diamonds: Defense/Buffs

### Room Management
- Rooms handle their own state and entities
- Combat rooms spawn enemies and manage encounters
- Treasure rooms handle loot distribution
- Shop rooms manage weapon/item purchases

## Development Workflows

### Running the Game
```bash
# Development
make run    # Uses MSYS2 Python

# Build executable
make build  # Creates dist/Astragalomancy.exe
```

### Adding New Content

#### New Weapons
1. Inherit from `BaseWeapon`
2. Define stat modifications
3. Implement special abilities
4. Add to weapon pool in `core/config.py`

#### New Enemy Types
1. Add stats to `ENEMY_TYPES` in `core/config.py`
2. Implement AI behavior in enemy class
3. Add spawn logic to combat rooms

## Project Structure
```
src/
  core/
    config.py     # Game constants, enemy types, weapon stats
    stats.py      # Core stat system
  entities/
    base.py       # Base entity class
    player.py     # Player implementation
    weapons/      # Weapon implementations
  rooms/          # Room types (combat, shop, etc)
  systems/        # Core game systems
    dice.py       # Dice mechanics
    cards.py      # Card system
    combat.py     # Combat resolution
```

## Testing
- Run unit tests: `make test`
- Debug mode: `make debug`
