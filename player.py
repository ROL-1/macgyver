"""Player functions file for MacGiver Maze game."""


class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start position."""
        self.level = level
        self.x = self.level.perso_start_coord[0]
        self.y = self.level.perso_start_coord[1]
        self.obj1_erase = False
        self.obj2_erase = False
        self.obj3_erase = False

    def movement(self, move):
        """Rules for player movements."""
        if move == 'up':
            if self.level.maze[self.y-1][self.x] != 'W':
                self.y -= 1
        if move == 'down':
            if self.level.maze[self.y+1][self.x] != 'W':
                self.y += 1
        if move == 'left':
            if self.level.maze[self.y][self.x-1] != 'W':
                self.x -= 1
        if move == 'right':
            if self.level.maze[self.y][self.x+1] != 'W':
                self.x += 1

    def inventory(self, level, inventory):
        """Rules for loot."""
        if (self.x, self.y) == level.coord_obj1 and self.obj1_erase is False:
            self.obj1_erase = True
            level.obj1_looted = True
            inventory.append('T')
        if (self.x, self.y) == level.coord_obj2 and self.obj2_erase is False:
            self.obj2_erase = True
            level.obj2_looted = True
            inventory.append('N')
        if (self.x, self.y) == level.coord_obj3 and self.obj3_erase is False:
            self.obj3_erase = True
            level.obj3_looted = True
            inventory.append('P')
