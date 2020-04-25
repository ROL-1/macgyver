"""Maze display's file for MacGiver Maze game."""
import pygame
from config import *
# from config import sprite, level_config_file, nb_obj, outdoor_file, wall_file,\
#     badguy_file, obj1_file, obj2_file, obj3_file
from random import sample
import os


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

    def empty_spaces(self):
        """Looking for empty spaces in maze to load objects."""
        empty_spaces_coord = []
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'E':
                    empty_spaces_coord.append((x, y))
        # Objects coordinates list:
        list_coord_obj = sample(empty_spaces_coord, nb_obj)
        #Create dictionary of objects positions
        dict_ = {}
        var = "obj"
        def fct_dict_(n, value):
            dict_[var+str(n)] = value
        for i in range(nb_obj):
            fct_dict_(i+1, list_coord_obj[i])
        self.dict_obj = dict_
        # # for j, k in self.dict_obj.items()
        # self.coord_obj1 = self.dict_obj['obj1']
        # self.coord_obj2 = self.dict_obj['obj2']
        # self.coord_obj3 = self.dict_obj['obj3']

        # for j, k in dict_obj.items():
        #     print(j,k)
        #     print(type(j),type(k))
        #     j = k
        #     print(f'le terme-clef {j} est associé à la coord-valeur{k}')

        # os.system('pause')        
###########################################################
        # self.coord_obj1 = list_coord_obj[0]
        # self.coord_obj2 = list_coord_obj[1]
        # self.coord_obj3 = list_coord_obj[2]
##################################################################################
##################################################################################        

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

    def display_objects(self, window):
        """Display objects in the maze if not looted"""
        # # Load objects images
        # print(objects_files)        
        # for i in range(len(objects_files)):
        #     for file in objects_files:
        #         for key in self.dict_obj.keys():
        #             key = pygame.image.load(file).convert_alpha()
        #             print(key)         
      
        obj1surface = pygame.image.load(objects_files[0]).convert_alpha()
        # obj2 = pygame.image.load(obj2_file).convert_alpha()
        # obj3 = pygame.image.load(obj3_file).convert_alpha()
# WIP ####################################################################
        # for i in range (nb_obj):
        # print(self.dict_obj['self.obj1'][0])
        for j, k in self.dict_obj.items():                        
                window.blit(obj1surface, (sprite*k[0], sprite*k[1]))
        
 ###########################################################################################      
        # if self.obj1_looted is not True:
        #     window.blit(obj1, (sprite*self.coord_obj1[0], sprite*self.coord_obj1[1]))
        # if self.obj2_looted is not True:
        #     window.blit(obj2, (sprite*self.coord_obj2[0], sprite*self.coord_obj2[1]))
        # if self.obj3_looted is not True:
        #     window.blit(obj3, (sprite*self.coord_obj3[0], sprite*self.coord_obj3[1]))
############################################################################################
############################################################################################
    def perso_start_coord(self, window):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord
