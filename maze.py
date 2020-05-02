"""Maze generate's file for MacGiver maze game."""
from random import sample, choice
from config import conf_
from lib import funct


class Maze:
    """Generate the maze frame."""

    def __init__(self, nb_obj):
        """Create BadGuy status. Load maze file and create 'maze' list."""
        # Load constants
        globals().update(conf_)
        # Select one file randomly
        selected_level = choice(funct.list_files(LEVELS_REP))
        # Read .json and return a list
        self.maze = funct.string_json(selected_level)['level_']
        # Generate
        self.objects_positions(nb_obj)
        self.perso_start_coord()

    def objects_positions(self, nb_obj):
        """Check for empty spaces and create a list of objects coord."""
        # Empty spaces coordinates list:
        empty_spaces_coord = []
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'E':
                    empty_spaces_coord.append((x, y))
        # Objects coordinates list:
        list_coord_obj = sample(empty_spaces_coord, nb_obj)
        # Create dictionary of objects positions : 'obj'i+1:(x,y)
        self.dict_obj = {}
        for i in range(nb_obj):
            self.dict_obj['obj'+str(i+1)] = list_coord_obj[i]

    def perso_start_coord(self):
        """Generate coordinates for perso start position."""
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if self.maze[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord
