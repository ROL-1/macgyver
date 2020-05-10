import pygame
from pygame import image
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE,
                           K_UP, K_DOWN, K_LEFT, K_RIGHT,
                           K_F1, K_F2)


def py_keyboard():
    """Control keyboard reactions."""
    for event in pygame.event.get():
        # Leave pygame
        keys_events = {
            'UP': K_UP,
            'DOWN': K_DOWN,
            'LEFT': K_LEFT,
            'RIGHT': K_RIGHT,
            'F1': K_F1,
            'F2': K_F2,
            'ESCAPE': K_ESCAPE
        }
        if event.type == KEYDOWN:
            for k, v in keys_events.items():
                if event.key == v:
                    return k
        elif event.type == QUIT:
            return 'QUIT'


def py_img(path):
    """Convert images for pygame."""
    return image.load(path).convert_alpha()