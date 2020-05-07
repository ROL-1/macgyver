"""Player's file for MacGiver maze game."""


class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start parameters."""
        self.level = level
        self.x = self.level.perso_start_coord[0]
        self.y = self.level.perso_start_coord[1]
        # Generate inventory
        self.inventory_list = []
        self.loot(level)

    def movement(self, move):
        """Rules for player movements."""
        if move == 'UP':
            if self.y - 1 >= 0 \
             and self.level.frame[self.y - 1][self.x] != 'W':
                self.y -= 1
        elif move == 'DOWN':
            if self.y + 1 < len(self.level.frame) \
             and self.level.frame[self.y + 1][self.x] != 'W':
                self.y += 1
        elif move == 'LEFT':
            if self.x - 1 >= 0 \
             and self.level.frame[self.y][self.x - 1] != 'W':
                self.x -= 1
        elif move == 'RIGHT':
            if self.x + 1 < len(self.level.frame) \
             and self.level.frame[self.y][self.x + 1] != 'W':
                self.x += 1

    def loot(self, level):
        """Increment objects in inventory when player is on."""
        for obj_numb, coord in level.dict_obj.items():
            if (self.x, self.y) == coord \
             and obj_numb not in self.inventory_list:
                self.inventory_list.append(obj_numb)
                self.inventory_list.sort()
