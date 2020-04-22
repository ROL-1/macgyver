"""Player functions file for MacGiver Maze game."""
import numpy as np
import pygame
from pygame.locals import *
from config import *
from maze import *

class Player:
    """Player start position and rules for movements."""
    
    def __init__(self,level):
        """Player start position."""
        self.level = level
        self.x = self.level.perso_start_position[0]
        self.y = self.level.perso_start_position[1]

    def movement(self,move):
        """Rules for player movements."""
        if move == 'up':
            if self.level.maze[self.y-1][self.x] != 'W':
                self.y -= 1
        if move == 'down':
            if self.level.maze[self.y+1][self.x] != 'W':
                self.y += 1 
        if move == 'left':
            if self.level.maze[self.y][self.x-1] != 'W':
                self.x -= 1
        if move == 'right':
            if self.level.maze[self.y][self.x+1] != 'W':
                self.x += 1
