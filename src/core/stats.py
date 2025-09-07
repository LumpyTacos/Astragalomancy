from dataclasses import dataclass

@dataclass
class EntityStats:
    """Base stats for game entities"""
    health: float = 100.0
    stamina: float = 50.0
    movement_speed: float = 2.0
    strength: float = 10.0
    dexterity: float = 10.0
    crit_chance: float = 5.0
    defense: float = 10.0
    mana: float = 100.0
    knockback: float = 0.0  # Only used by player

    def copy(self):
        """Create a deep copy of stats"""
        return EntityStats(**self.__dict__)