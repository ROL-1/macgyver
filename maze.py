"""Maze generate's file for MacGiver maze game."""
import pygame
from lib import functions
from config import sprite, nb_obj, outdoor_file, \
 wall_file, badguy_file, objects_files
from random import sample, choice


class Maze:
    """Generate the maze frame."""

    def __init__(self):
        """ Create BadGuy status. Load maze file and create 'maze' list."""
        # Boolean for Badguy status
        self.badguy_sleeping = False         
        # Select one file randomly
        select_level = choice(functions.load_files('levels'))        
        # Read .json and return a list
        self.maze = functions.string_json(f'levels/{select_level}')['level_frame']
        # Generate
        self.objects_positions()
 
    def objects_positions(self):
        """Check for empty spaces in maze and create a list of objects positions"""
        # Empty spaces coordinates list:
        empty_spaces_coord = []
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'E':
                    empty_spaces_coord.append((x, y))
        # Objects coordinates list:
        list_coord_obj = sample(empty_spaces_coord, nb_obj)
        # Create dictionary of objects positions : 'obj'i+1:(x,y)   
        for i in range(nb_obj):            
            self.dict_obj = functions.name_inc('obj',i+1, list_coord_obj[i])

    def display_maze(self, window):
        """Display maze using load_maze."""
        # Maze files
        outdoor = pygame.image.load(outdoor_file).convert_alpha()
        wall = pygame.image.load(wall_file).convert_alpha()
        badguy = pygame.image.load(badguy_file).convert_alpha()

        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'W':
                    window.blit(wall, (sprite*x, sprite*y))
                elif self.maze[y][x] == 'O':
                    self.coord_outdoor = (x, y)
                    window.blit(outdoor, (sprite*x, sprite*y))
                elif self.maze[y][x] == 'G':
                    self.coord_badguy = (x, y)
                    # Check if badguy is sleeping
                    if self.badguy_sleeping is not True:
                        window.blit(badguy, (sprite*x, sprite*y))

    def display_objects(self, window, inventory):
        """Display objects in the maze if not looted."""
        # Load objects images
        i = 0
        while i < len(self.dict_obj):
            for obj_name, coord in self.dict_obj.items():
                py_image = pygame.image.load(objects_files[i]).convert_alpha()
                if obj_name not in inventory:
                    window.blit(py_image, (sprite*coord[0], sprite*coord[1]))
                i += 1

    def perso_start_coord(self, window):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord
