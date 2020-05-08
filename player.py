"""Player's file for MacGiver maze game."""


class Player:
    """Player rules for movements."""

    def __init__(self, level):
        """Player start parameters."""
        self.level = level
        self.x = level.perso_start_coord[0]
        self.y = level.perso_start_coord[1]
        # Generate inventory
        self.inventory_list = []
        self.loot(level)

    def movement(self, move):
        """Rules for player movements."""
        perso_coord = (self.x, self.y)
        if move == 'UP':
            self.y -= 1
        elif move == 'DOWN':
            self.y += 1
        elif move == 'LEFT':
            self.x -= 1
        elif move == 'RIGHT':
            self.x += 1
        if (self.x, self.y) not in self.level.moves_spaces_list:
            (self.x, self.y) = perso_coord

    def loot(self, level):
        """Increment objects in inventory when player is on."""
        for obj_numb, coord in level.dict_obj.items():
            if (self.x, self.y) == coord \
             and obj_numb not in self.inventory_list:
                self.inventory_list.append(obj_numb)
                self.inventory_list.sort()
