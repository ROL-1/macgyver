"""Player's display and functions file for MacGiver Maze game."""
import numpy as np
import pygame
from pygame.locals import *

class Perso:
    """Display player's perso, first position."""

    def __init__(self, window):
        """Load and display image for player's perso."""
        perso = pygame.image.load("images/macgyver.png").convert_alpha()
        position_perso = perso.get_rect()
        position_perso.center = (225, 225)
        self.position_perso = position_perso
