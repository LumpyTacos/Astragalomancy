from __future__ import annotations

import sys
import pygame as pg

from core import config
from rooms.start_room import StartRoom
from systems.room_manager import RoomManager

def init_pygame() -> pg.Surface:
    pg.init()
    pg.display.set_caption(config.WINDOW_TITLE)
    pg.display.set_icon(pg.image.load("assets/icon.png"))
    screen = pg.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    return screen


def main() -> None:
    screen = init_pygame()
    clock = pg.time.Clock()
  
    room_manager.add_room(StartRoom())

    running = True
    while running:
        dt = clock.tick(config.TARGET_FPS) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        screen.fill(config.BACKGROUND_COLOR)
        room_manager.update(dt)
        room_manager.draw(screen)
        pg.display.flip()

    pg.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()