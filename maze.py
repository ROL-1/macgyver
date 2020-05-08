"""Maze generate's file for MacGiver maze game."""
from random import sample, choice
import config
from lib import funct


class Maze:
    """Generate the maze frame."""

    game_count = 0

    def __init__(self, nb_obj):
        """Create BadGuy status. Load maze file and create 'frame' list."""
        # Select one file randomly
        selected_level = choice(funct.list_files(config.LEVELS_REP))
        # Read .json and return a list
        self.frame = funct.string_json(selected_level)['level_']
        # Generate
        self.empty_spaces_list = []
        self.walls_spaces_list = []
        self.moves_spaces_list = []
        self.coord_lists()
        self.objects_positions(nb_obj)
        self.moves_spaces()
        # Game count
        type(self).game_count += 1

    def coord_lists(self):
        """Create lists for each sprite type."""
        # Empty spaces coordinates list:
        for x in range(len(self.frame)):
            for y in range(len(self.frame)):
                if self.frame[y][x] == 'E':
                    self.empty_spaces_list.append((x, y))
                elif self.frame[y][x] == 'M':
                    self.perso_start_coord = (x, y)
                elif self.frame[y][x] == 'G':
                    bad_guy_coord = ((x, y))
                    self.bad_guy_coord = bad_guy_coord
                elif self.frame[y][x] == 'O':
                    outdoor_coord = ((x, y))
                    self.outdoor_coord = outdoor_coord

    def objects_positions(self, nb_obj):
        """Create a dictionnary of objects coord."""
        # Objects coordinates list:
        list_coord_obj = sample(self.empty_spaces_list, nb_obj)
        # Create dictionary of objects positions : 'obj'i+1:(x,y)
        self.dict_obj = {}
        for i in range(nb_obj):
            self.dict_obj['obj' + str(i + 1)] = list_coord_obj[i]

    def moves_spaces(self):
        """Create list of moves spaces."""
        self.moves_spaces_list = self.empty_spaces_list
        self.moves_spaces_list.append(self.perso_start_coord)
        self.moves_spaces_list.append(self.bad_guy_coord)
        self.moves_spaces_list.append(self.outdoor_coord)

    @classmethod
    def print_count(cls):
        if cls.game_count == 1:
            print(f"You played {cls.game_count} game.")
        else:
            print(f"You played {cls.game_count} games.")
