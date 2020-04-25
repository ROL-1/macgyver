"""Player functions file for MacGiver Maze game."""
import os

class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start position."""
        self.level = level
        self.x = self.level.perso_start_coord[0]
        self.y = self.level.perso_start_coord[1]

    def movement(self, move):
        """Rules for player movements."""
        if move == 'up':
            if self.y-1 >= 0 \
             and self.level.maze[self.y-1][self.x] != 'W':
                self.y -= 1
        elif move == 'down':
            if self.y+1 < len(self.level.maze) \
             and self.level.maze[self.y+1][self.x] != 'W':
                self.y += 1
        elif move == 'left':
            if self.x-1 >= 0 \
             and self.level.maze[self.y][self.x-1] != 'W':
                self.x -= 1
        elif move == 'right':
            if self.x+1 < len(self.level.maze) \
             and self.level.maze[self.y][self.x+1] != 'W':
                self.x += 1

    def inventory(self, level, inventory):
        """Rules for loot."""      
        for key, value in level.dict_obj.items():
            if (self.x, self.y) == value \
             and key not in inventory:                
                inventory.append(key)
        print(inventory)
