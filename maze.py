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
        # Select one file randomly
        select_level = choice(functions.load_files('levels'))        
        # Read .json and return a list
        self.maze = functions.string_json(f'levels/{select_level}')['level_frame']
        # Generate
        self.objects_positions()
        self.perso_start_coord()
 
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

    def perso_start_coord(self):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord
    
