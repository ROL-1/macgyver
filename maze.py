"""Maze display's file for MacGiver Maze game."""
import pygame
from config import sprite, level_config_file, nb_obj, outdoor_file, \
 wall_file, badguy_file, objects_files
from random import sample, choice


class Maze:
    """Load, generate and display the maze."""

    def __init__(self):
        """Load maze file."""
        self.MAZE_FILE = choice(level_config_file)
        self.badguy_sleeping = False

    def load_maze(self):
        """Read maze file and return the maze frame (list type)."""
        with open(self.MAZE_FILE, 'r') as maze_file:
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
        """Check for empty spaces in maze to load objects."""
        empty_spaces_coord = []
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'E':
                    empty_spaces_coord.append((x, y))
        # Objects coordinates list:
        list_coord_obj = sample(empty_spaces_coord, nb_obj)
        # Create dictionary of objects positions : 'objx':(x,y)
        dict_ = {}
        var = "obj"

        def fct_dict_(n, value):
            """Increment name for dictionary."""
            dict_[var+str(n)] = value
        for i in range(nb_obj):
            fct_dict_(i+1, list_coord_obj[i])
        self.dict_obj = dict_

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
