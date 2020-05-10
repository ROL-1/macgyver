"""Player's file for MacGiver maze game."""


class Player:
    """Player rules for movements and loot."""

    def __init__(self, level):
        """Player start parameters."""
        self.perso_coord = level.perso_start_coord
        # Generate inventory
        self.inventory_list = []

    def movement(self, action, level):
        """Rules for player movements."""
        x = self.perso_coord[0]
        y = self.perso_coord[1]
        if action == 'UP':
            y -= 1
        elif action == 'DOWN':
            y += 1
        elif action == 'LEFT':
            x -= 1
        elif action == 'RIGHT':
            x += 1
        if (x, y) in level.moves_spaces_list:
            self.perso_coord = (x, y)

    def loot(self, level):
        """Increment objects in inventory when player is on."""
        for coord in level.list_coord_obj:
            if self.perso_coord == coord and coord not in self.inventory_list:
                self.inventory_list.append(coord)
