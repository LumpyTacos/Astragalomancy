from __future__ import annotations
import pygame as pg
from typing import List, Dict


class Animation:
    """Handles sprite animations."""
    
    def __init__(self, frames: List[pg.Surface], frame_duration: float = 0.1, loop: bool = True):
        self.frames = frames
        self.frame_duration = frame_duration
        self.loop = loop
        self.current_frame = 0
        self.time_elapsed = 0
        self.finished = False
        
    def update(self, dt: float) -> pg.Surface:
        """Update animation and return current frame."""
        if self.finished:
            return self.frames[-1]
            
        self.time_elapsed += dt
        
        if self.time_elapsed >= self.frame_duration:
            self.time_elapsed = 0
            self.current_frame += 1
            
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True
                    
        return self.frames[self.current_frame]
        
    def reset(self) -> None:
        """Reset animation to first frame."""
        self.current_frame = 0
        self.time_elapsed = 0
        self.finished = False


class AnimationManager:
    """Manages multiple animations for an entity."""
    
    def __init__(self):
        self.animations: Dict[str, Animation] = {}
        self.current_animation: str | None = None
        
    def add_animation(self, name: str, frames: List[pg.Surface], frame_duration: float = 0.1, loop: bool = True) -> None:
        """Add a new animation."""
        self.animations[name] = Animation(frames, frame_duration, loop)
        
    def play(self, name: str, force: bool = False) -> None:
        """Play an animation. If force is True, restart even if already playing."""
        if name not in self.animations:
            return
            
        if self.current_animation != name or force:
            self.current_animation = name
            self.animations[name].reset()
            
    def update(self, dt: float) -> pg.Surface | None:
        """Update current animation and return current frame."""
        if self.current_animation and self.current_animation in self.animations:
            return self.animations[self.current_animation].update(dt)
        return None
        
    def is_finished(self) -> bool:
        """Check if current animation is finished."""
        if self.current_animation and self.current_animation in self.animations:
            return self.animations[self.current_animation].finished
        return True


# Placeholder animations until we have assets
def create_placeholder_animation(color: tuple[int, int, int], size: tuple[int, int], 
                              frames: int = 4) -> List[pg.Surface]:
    """Create placeholder animation frames."""
    surfaces = []
    for i in range(frames):
        surf = pg.Surface(size)
        surf.fill(color)
        # Add simple visual change to show animation
        pg.draw.rect(surf, (255, 255, 255), 
                    (i * size[0]/frames, i * size[1]/frames, 
                     size[0]/frames, size[1]/frames))
        surfaces.append(surf)
    return surfaces
