"""Player functions file for MacGiver Maze game."""


class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start position."""
        self.level = level
        self.x = self.level.perso_start_position[0]
        self.y = self.level.perso_start_position[1]
        self.ether_erase = False
        self.needle_erase = False
        self.pipe_erase = False

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
        if (self.x, self.y) == level.position_ether and self.ether_erase == False:
            self.ether_erase = True
            level.ether_looted = True
            inventory.append('T')
        if (self.x, self.y) == level.position_needle and self.needle_erase == False:
            self.needle_erase = True
            level.needle_looted = True
            inventory.append('N')
        if (self.x, self.y) == level.position_pipe and self.pipe_erase == False:
            self.pipe_erase = True
            level.pipe_looted = True
            inventory.append('P')
