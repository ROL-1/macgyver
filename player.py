"""Player functions file for MacGiver Maze game."""
from config import keys_events


class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start position."""
        self.level = level
        self.x = self.level.perso_start_coord[0]
        self.y = self.level.perso_start_coord[1]
        self.inventory_list = []

    def movement(self, move):
        """Rules for player movements."""
        if move == keys_events[0]:
            if self.y-1 >= 0 \
             and self.level.maze[self.y-1][self.x] != 'W':
                self.y -= 1
        elif move == keys_events[1]:
            if self.y+1 < len(self.level.maze) \
             and self.level.maze[self.y+1][self.x] != 'W':
                self.y += 1
        elif move == keys_events[2]:
            if self.x-1 >= 0 \
             and self.level.maze[self.y][self.x-1] != 'W':
                self.x -= 1
        elif move == keys_events[3]:
            if self.x+1 < len(self.level.maze) \
             and self.level.maze[self.y][self.x+1] != 'W':
                self.x += 1

    def inventory(self, level):
        """Rules for loot."""
        for obj_name, coord in level.dict_obj.items():
            if (self.x, self.y) == coord \
             and obj_name not in self.inventory_list:
                self.inventory_list.append(obj_name)
                self.inventory_list.sort()
