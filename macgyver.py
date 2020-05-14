"""Main file for MacGiver maze game."""
import config
from game import Game
from view.display import Display_mess
from libs.py_lib import py_keyboard


def main():
    """Contains loops defining when a menu or game is displayed.
       And Launch the Game module."""
    program_loop = True
    while program_loop:
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
                program_loop = False
            elif action == 'F1':
                menu_loop = False
                nb_obj = 3
            elif action == 'F2':
                menu_loop = False
                nb_obj = 4
        # END MENU LOOP ######################################

        # Initialize game modules
        game = Game(nb_obj)

        # GAME LOOP ##########################################
        while game_loop:
            action = py_keyboard()
            if action == 'ESCAPE':
                game_loop = False
            elif action == 'QUIT':
                menu_loop = False
                game_loop = False
                program_loop = False
            else:
                game.ends(message, nb_obj)
                if game.end_message is True:
                    if action == 'F1':
                        game_loop = False
                    elif action == 'F2':
                        game_loop = False
                        program_loop = False
                else:
                    game.play(action)
        # END GAME LOOP ######################################


if __name__ == "__main__":

    main()
