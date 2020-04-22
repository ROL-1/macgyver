"""Classes file for MacGiver Maze game."""
import numpy as np
import pygame
from pygame.locals import *


class Create_maze:
    """Load, generate and display the maze."""

    def __init__(self):
        """Load maze file."""
        self.LABY_FILE = "level_config_1.json"

    def load_maze(self):
        """Read maze file and return a ndarray."""
        with open(self.LABY_FILE, 'r') as maze_file:
            # Read 17 to 32 lines only
            maze_file_line = maze_file.readlines()[16:31]
            laby = []
            for line in maze_file_line:
                laby_line = []
                for caracter in line:
                    if caracter != '\n':
                        laby_line.append(caracter)
                laby.append(laby_line)
                maze = np.array(laby)
            self.maze = maze
            print(maze)  # To Clean
            print(type(maze))  # To Clean

    def display_maze(self, window):
        """Display maze using load_maze."""
        background = pygame.image.load("images/background.jpg").convert()
        outdoor = pygame.image.load("images/outdoor.png").convert_alpha()
        wall = pygame.image.load("images/wall.png").convert_alpha()
        window.blit(background, (0, 0))
        sprite = 30  # px
        for x in range(15):
            for y in range(15):
                if self.maze[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                if self.maze[y][x] == 'O':
                    window.blit(outdoor, (sprite*x, sprite*y))


class Perso:
    """Display player's perso."""

    def __init__(self, window):
        """Load and display image for player's perso."""
        perso = pygame.image.load("images/perso.png").convert_alpha()
        position_perso = perso.get_rect()
        position_perso.center = (225, 225)
        self.position_perso = position_perso
