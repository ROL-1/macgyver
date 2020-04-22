"""Maze display's file for MacGiver Maze game."""
import numpy as np
import pygame
from pygame.locals import *
from config import *


class Create_maze:
    """Load, generate and display the maze."""

    def __init__(self):
        """Load maze file."""
        self.MAZE_FILE = level_config1_file

    def load_maze(self):
        """Read maze file and return a ndarray."""
        with open(self.MAZE_FILE, 'r') as maze_file:
            # Read 17 to 32 lines only
            maze_file_line = maze_file.readlines()
            maze_frame = []
            for line in maze_file_line:
                maze_frame_line = []
                for caracter in line:
                    if caracter != '\n':
                        maze_frame_line.append(caracter)
                maze_frame.append(maze_frame_line)
                maze = np.array(maze_frame)
            self.maze = maze
            print(maze)  # To Clean
            print(type(maze))  # To Clean

    def display_maze(self, window):
        """Display maze using load_maze."""
        # Maze
        background = pygame.image.load(background_file).convert()
        outdoor = pygame.image.load(outdoor_file).convert_alpha()
        wall = pygame.image.load(wall_file).convert_alpha()
        # BadGuy and Objects
        badguy = pygame.image.load(badguy_file).convert_alpha()
        ether = pygame.image.load(ether_file).convert_alpha()
        needle = pygame.image.load(needle_file).convert_alpha()
        pipe = pygame.image.load(pipe_file).convert_alpha()
        
        window.blit(background, (0, 0))
        sprite = sprites_size
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                if self.maze[y][x] == 'O':
                    window.blit(outdoor, (sprite*x, sprite*y))
                if self.maze[y][x] == 'G':
                    window.blit(badguy, (sprite*x, sprite*y))   
                if self.maze[y][x] == 'T':
                    window.blit(ether, (sprite*x, sprite*y))
                if self.maze[y][x] == 'N':
                    window.blit(needle, (sprite*x, sprite*y))
                if self.maze[y][x] == 'P':
                    window.blit(pipe, (sprite*x, sprite*y))
