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
        self.moves_spaces_list = []
        self.empty_spaces()
        self.objects_positions(nb_obj)
        self.perso_start_coord()
        self.moves_spaces()
        # Game count
        type(self).game_count += 1

    def empty_spaces(self):
        """Create list of empty spaces."""
        # Empty spaces coordinates list:
        for x in range(len(self.frame)):
            for y in range(len(self.frame)):
                if self.frame[y][x] == 'E':
                    self.empty_spaces_list.append((x, y))
        print(len(self.empty_spaces_list))

    def objects_positions(self, nb_obj):
        """Create a dictionnary of objects coord."""
        # Objects coordinates list:
        list_coord_obj = sample(self.empty_spaces_list, nb_obj)
        # Create dictionary of objects positions : 'obj'i+1:(x,y)
        self.dict_obj = {}
        for i in range(nb_obj):
            self.dict_obj['obj' + str(i + 1)] = list_coord_obj[i]

    def perso_start_coord(self):
        """Generate coordinates for perso start position."""
        for x in range(len(self.frame)):
            for y in range(len(self.frame)):
                if self.frame[y][x] == 'M':
                    perso_start_coord = (x, y)
        self.perso_start_coord = perso_start_coord

    def moves_spaces(self):
        """Create list of moves spaces."""
        self.moves_spaces_list = self.empty_spaces_list
        self.moves_spaces_list.append(self.perso_start_coord)
        for x in range(len(self.frame)):
            for y in range(len(self.frame)):
                if self.frame[y][x] == 'G':
                    self.moves_spaces_list.append((x, y))
                elif self.frame[y][x] == 'O':
                    self.moves_spaces_list.append((x, y))

    @classmethod
    def print_count(cls):
        if cls.game_count == 1:
            print(f"You played {cls.game_count} game.")
        else:
            print(f"You played {cls.game_count} games.")
