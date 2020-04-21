"""Classes file for MacGiver Labyrinth game."""
import numpy as np
import pygame
from pygame.locals import *


class Create_labyrinth:
    """Load, generate and display the labyrinth."""

    def __init__(self):
        """Load labyrinth file."""
        self.LABY_FILE = "labyrinth.py"

    def load_labyrinth(self):
        """Read labyrinth file and return a ndarray."""
        with open(self.LABY_FILE, 'r') as labyrinth_file:
            # Read 17 to 32 lines only
            labyrinth_file_line = labyrinth_file.readlines()[16:31]
            laby = []
            for line in labyrinth_file_line:
                laby_line = []
                for caracter in line:
                    if caracter != '\n':
                        laby_line.append(caracter)
                laby.append(laby_line)
                labyrinth = np.array(laby)
            self.labyrinth = labyrinth
            print(labyrinth)  # To Clean
            print(type(labyrinth))  # To Clean

    def display_labyrinth(self, window):
        """Display labyrinth using load_labyrinth."""
        background = pygame.image.load("images/background.jpg").convert()
        outdoor = pygame.image.load("images/outdoor.png").convert_alpha()
        wall = pygame.image.load("images/wall.png").convert_alpha()
        window.blit(background, (0, 0))
        sprite = 30  # px
        for x in range(15):
            for y in range(15):
                if self.labyrinth[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                if self.labyrinth[y][x] == 'O':
                    window.blit(outdoor, (sprite*x, sprite*y))


class Perso:
    """Display player's perso."""

    def __init__(self, window):
        """Load and display image for player's perso."""
        perso = pygame.image.load("images/perso.png").convert_alpha()
        position_perso = perso.get_rect()
        position_perso.center = (225, 225)
        self.position_perso = position_perso
