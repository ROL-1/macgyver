"""Maze generate's file for MacGiver maze game."""
from random import sample, choice

import config
from libs.paths_lib import list_files, string_json


class Maze:
    """Generate the maze frame."""

    def __init__(self, nb_obj):
        """Load maze file create frame list and lists for each sprite type."""
        # Select one file randomly
        selected_level = choice(list_files(config.LEVELS_REP))
        # Read .json and return a list
        self.frame = string_json(selected_level)['level_']
        # Generate
        self.empty_spaces_list = []
        self.walls_spaces_list = []
        self.moves_spaces_list = []
        self._coord_lists()
        self._objects_positions(nb_obj)
        self._moves_spaces()

    def _coord_lists(self):
        """Create lists for each sprite type."""
        # Empty spaces coordinates list:
        for x, line in enumerate(self.frame):
            for y, char in enumerate(line):
                if char == 'E':
                    self.empty_spaces_list.append((y, x))
                if char == 'W':
                    self.walls_spaces_list.append((y, x))
                elif char == 'M':
                    self.perso_start_coord = (y, x)
                elif char == 'G':
                    bad_guy_coord = (y, x)
                    self.bad_guy_coord = bad_guy_coord
                elif char == 'O':
                    outdoor_coord = (y, x)
                    self.outdoor_coord = outdoor_coord

    def _objects_positions(self, nb_obj):
        """Create a list of objects coord."""
        self.list_coord_obj = sample(self.empty_spaces_list, nb_obj)

    def _moves_spaces(self):
        """Create list of moves spaces."""
        self.moves_spaces_list = self.empty_spaces_list
        self.moves_spaces_list.append(self.perso_start_coord)
        self.moves_spaces_list.append(self.bad_guy_coord)
        self.moves_spaces_list.append(self.outdoor_coord)
