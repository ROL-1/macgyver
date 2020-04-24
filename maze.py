"""Maze display's file for MacGiver Maze game."""
import pygame
from pygame.locals import *
from config import *
from player import Player
from config import sprite


class Create_maze:
    """Load, generate and display the maze."""

    def __init__(self):
        """Load maze file."""
        self.MAZE_FILE = level_config_file
        self.badguy_sleeping = False
        self.obj1_looted = False
        self.obj2_looted = False
        self.obj3_looted = False

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
        obj1 = pygame.image.load(obj1_file).convert_alpha()
        obj2 = pygame.image.load(obj2_file).convert_alpha()
        obj3 = pygame.image.load(obj3_file).convert_alpha()

        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                if self.maze[y][x] == 'O':
                    self.coord_outdoor = (x, y)
                    window.blit(outdoor, (sprite*x, sprite*y))
                if self.maze[y][x] == 'G':
                    self.coord_badguy = (x, y)
                    if self.badguy_sleeping is not True:
                        window.blit(badguy, (sprite*x, sprite*y))
                if self.maze[y][x] == 'T':
                    self.coord_obj1 = (x, y)
                    if self.obj1_looted is not True:
                        window.blit(obj1, (sprite*x, sprite*y))
                if self.maze[y][x] == 'N':
                    self.coord_obj2 = (x, y)
                    if self.obj2_looted is not True:
                        window.blit(obj2, (sprite*x, sprite*y))
                if self.maze[y][x] == 'P':
                    self.coord_obj3 = (x, y)
                    if self.obj3_looted is not True:
                        window.blit(obj3, (sprite*x, sprite*y))

    def perso_start_coord(self, window):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord
