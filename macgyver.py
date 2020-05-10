"""Main file for MacGiver maze game."""
import config
from models.maze import Maze
from models.player import Player
from view.display import Display_mess, Display_maze
from lib.py_lib import py_keyboard


def main():
    """Launch functions."""
    big_loop = True
    while big_loop:
        game_loop = True
        menu_loop = True
        # MENU LOOP ##########################################
        while menu_loop:
            nb_obj = 0
            message = Display_mess()
            message.display_message(config.MENU_MESS)
            action = py_keyboard()
            if action == 'QUIT' or action == 'ESCAPE':
                menu_loop = False
                game_loop = False
                big_loop = False
            elif action == 'F1':
                menu_loop = False
                nb_obj = 3
            elif action == 'F2':
                menu_loop = False
                nb_obj = 4
        # END MENU LOOP ######################################

        # Load & generate the maze from the file
        level = Maze(nb_obj)
        # Manage player movements and generate inventory
        player = Player(level)
        # Display the maze
        display_maze = Display_maze(level, player)

        # GAME LOOP ##########################################
        end_message = False
        while game_loop:
            action = py_keyboard()
            if action == 'ESCAPE':
                game_loop = False
            elif action == 'QUIT':
                menu_loop = False
                game_loop = False
                big_loop = False
            else:
                if end_message is False:
                    player.movement(action, level)

            # Add loot in Inventory
            player.loot(level)
            # Re-paste images
            display_maze.repaste_display(level, player)

            # Meeting BadGuy
            if player.perso_coord == level.bad_guy_coord:
                # Check inventory
                if len(player.inventory_list) != nb_obj:
                    message.display_message(config.LOOSE_MESS)
                    end_message = True
                else:
                    display_maze.badguy_sleeping = True
            # Check Exit
            elif player.perso_coord == level.outdoor_coord:
                if display_maze.badguy_sleeping:
                    message.display_message(config.WIN_MESS)
                    end_message = True
                else:
                    message.display_message(config.CHEAT_MESS)
                    end_message = True
            if end_message:
                if action == 'F1':
                    game_loop = False
                elif action == 'F2':
                    game_loop = False
                    big_loop = False
        # END GAME LOOP ######################################


if __name__ == "__main__":

    main()
