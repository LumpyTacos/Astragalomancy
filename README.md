# Astragalomancy

A pygame-based roguelike dungeon crawler where dice and cards empower the player. This repository starts with a clean, scalable foundation: rooms, entities, systems, and a simple controllable player. We'll layer in dice, cards, enemies, and items next.

## Quickstart

1. Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -U pip
pip install -r requirements.txt
```

2. Run the game:

```bash
python -m src.main
```

Controls: WASD or Arrow Keys to move. Esc to quit.

## Project Structure

```text
src/
  core/
    config.py           # Screen, colors, constants
  entities/
    base.py             # BaseEntity class
    player.py           # Player entity
  rooms/
    base_room.py        # BaseRoom class
    start_room.py       # Initial room
  systems/
    room_manager.py     # Room switching and forwarding
  main.py               # Game entry point & loop
assets/                 # Art, audio, data
```

## Extending

- Create new entities by subclassing `BaseEntity` and placing them in `src/entities/`.
- Add new rooms by subclassing `BaseRoom` in `src/rooms/` and registering them via `RoomManager`.
- Add systems (combat, inventory, dice/cards) under `src/systems/` and compose them into rooms.

This layout keeps modules small and readable while staying flexible for growth.