"""Maze display's file for MacGiver Maze game."""
import pygame
from pygame.locals import *
from config import *
from player import *


class Create_maze:
    """Load, generate and display the maze."""

    def __init__(self):
        """Load maze file."""
        self.MAZE_FILE = level_config1_file
        self.badguy_sleeping = False
        self.ether_looted = False
        self.needle_looted = False
        self.pipe_looted = False

    def load_maze(self):
        """Read maze file and return the maze frame (list type)."""
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
            self.maze = maze_frame
            print(self.maze)  # To Clean

    def display_maze(self, window):
        """Display maze using load_maze."""
        # Maze files
        outdoor = pygame.image.load(outdoor_file).convert_alpha()
        wall = pygame.image.load(wall_file).convert_alpha()
        # BadGuy and Objects files
        badguy = pygame.image.load(badguy_file).convert_alpha()
        ether = pygame.image.load(ether_file).convert_alpha()
        needle = pygame.image.load(needle_file).convert_alpha()
        pipe = pygame.image.load(pipe_file).convert_alpha()

        sprite = sprites_size
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                if self.maze[y][x] == 'O':
                    self.position_outdoor = (x, y)
                    window.blit(outdoor, (sprite*x, sprite*y))
                if self.maze[y][x] == 'G':
                    self.position_badguy = (x, y)
                    if self.badguy_sleeping != True:
                        window.blit(badguy, (sprite*x, sprite*y))
                if self.maze[y][x] == 'T':
                    self.position_ether = (x, y)
                    if self.ether_looted != True:
                        window.blit(ether, (sprite*x, sprite*y))
                if self.maze[y][x] == 'N':
                    self.position_needle = (x, y)
                    if self.needle_looted != True:
                        window.blit(needle, (sprite*x, sprite*y))
                if self.maze[y][x] == 'P':
                    self.position_pipe = (x, y)
                    if self.pipe_looted != True:
                        window.blit(pipe, (sprite*x, sprite*y))

    def perso_start_position(self, window):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                        perso_start_position = (x, y)
        self.perso_start_position = perso_start_position
