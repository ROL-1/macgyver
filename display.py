"""Display's file for MacGiver maze game."""
import pygame
from config import *
from maze import Maze
from player import Player
from lib import functions

class Display:
    """Display the maze."""

    def __init__(self,level,player):
        self.window = pygame.display.set_mode(window_size)
        # Boolean for Badguy status
        self.badguy_sleeping = False  

        # Generate
        self.display_maze(level)
        self.display_objects(level, player)

    def display_maze(self, level):
        """Display maze using load_maze."""
        # Maze files
        outdoor = pygame.image.load(outdoor_file).convert_alpha()
        wall = pygame.image.load(wall_file).convert_alpha()
        badguy = pygame.image.load(badguy_file).convert_alpha()

        for x in range(len(level.maze)):
            for y in range(len(level.maze)):
                if level.maze[y][x] == 'W':
                    self.window.blit(wall, (sprite*x, sprite*y))
                elif level.maze[y][x] == 'O':
                    level.coord_outdoor = (x, y)
                    self.window.blit(outdoor, (sprite*x, sprite*y))
                elif level.maze[y][x] == 'G':
                    level.coord_badguy = (x, y)
                    # Check if badguy is sleeping
                    if self.badguy_sleeping is not True:
                        self.window.blit(badguy, (sprite*x, sprite*y))

    def display_objects(self, level, player):
        """Display objects in the maze if not looted."""
        # Load objects images
        i = 0
        while i < len(level.dict_obj):
            for obj_name, coord in level.dict_obj.items():
                py_image = pygame.image.load(objects_files[i]).convert_alpha()
                if obj_name not in player.inventory_list:
                    self.window.blit(py_image, (sprite*coord[0], sprite*coord[1]))
                i += 1

    def repaste_display(self,level,player):
        """Repaste display."""
        background = pygame.image.load(background_file).convert()
        perso = pygame.image.load(perso_file).convert_alpha()
        self.window.blit(background, (0, 0))
        self.display_maze(level)
        self.display_objects(level, player)
        # level.display_maze(window)
        # level.display_objects(window, inventory)
        self.window.blit(perso, (player.x*sprite, player.y*sprite))
        # Refresh
        pygame.display.flip()


