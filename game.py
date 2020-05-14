"""Game file for MacGiver maze game."""
import config
from controler.maze import Maze
from controler.player import Player
from view.display import Display_maze


class Game:
    """Initialize modules and contain logical of the game."""

    def __init__(self, nb_obj):
        """Load modules and initialize end condition."""
        # End game status
        self.end_message = False
        # Load & generate the maze from the file
        self.maze = Maze(nb_obj)
        # Manage player movements and generate inventory
        self.player = Player(self.maze)
        # Display the maze
        self.display_maze = Display_maze(self.maze, self.player)

    def ends(self, message, nb_obj):
        """Check condition for display end menu or erase badguy."""
        # Meeting BadGuy
        if self.player.perso_coord == self.maze.bad_guy_coord:
            # Check inventory
            if len(self.player.inventory_list) != nb_obj:
                message.display_message(config.LOOSE_MESS)
                self.end_message = True
            else:
                self.display_maze.badguy_sleeping = True
        # Check Exit
        elif self.player.perso_coord == self.maze.outdoor_coord:
            self.end_message = True
            if self.display_maze.badguy_sleeping:
                message.display_message(config.WIN_MESS)
            else:
                message.display_message(config.CHEAT_MESS)

    def play(self, action):
        """Call module for movements, loot and repaste display."""
        # Players moves
        self.player.movement(action, self.maze)
        # Add loot in Inventory
        self.player.loot(self.maze)
        # Re-paste images
        self.display_maze.repaste_display(self.maze, self.player)
