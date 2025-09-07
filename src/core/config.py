from .stats import EntityStats

# Display configuration settings
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
WINDOW_TITLE = "Astragalomancy"

TARGET_FPS = 60

# Visuals
BACKGROUND_COLOR = (16, 16, 24)
UI_COLOR = (220, 220, 220)
PLAYER_COLOR = (90, 200, 250)
WALL_COLOR = (80, 80, 100)

TILE_SIZE = 48

# Player base stats
PLAYER_STATS = EntityStats(
    health=150.0,
    stamina=100.0,
    movement_speed=3.0,
    strength=15.0,
    dexterity=10.0,
    crit_chance=5.0,
    defense=15.0,
    mana=100.0,
    knockback=1.0
)

# Enemy base stats
ENEMY_TYPES = {
    "goblin": EntityStats(
        health=75.0,
        stamina=30.0,
        movement_speed=2.5,
        strength=8.0,
        dexterity=12.0,
        crit_chance=3.0,
        defense=5.0,
        mana=0.0
    ),
    "ogre": EntityStats(
        health=200.0,
        stamina=80.0,
        movement_speed=1.5,
        strength=20.0,
        dexterity=5.0,
        crit_chance=2.0,
        defense=20.0,
        mana=0.0
    ),
    "rogue": EntityStats(
        health=90.0,
        stamina=60.0,
        movement_speed=3.0,
        strength=10.0,
        dexterity=18.0,
        crit_chance=15.0,
        defense=8.0,
        mana=50.0
    )
}

# Other existing config values...