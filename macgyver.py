"""Main file for MacGiver maze game."""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE,\
                          K_UP, K_DOWN, K_LEFT, K_RIGHT,\
                          K_F1, K_F2
from config import conf_
from maze import Maze
from player import Player
from display import Display_mess, Display


def main():
    """Launch functions."""
    # Load constants
    globals().update(conf_)
    # Launch pygame
    pygame.init()

    # Pygame parameters
    pygame.key.set_repeat(KEY_SET_REPEAT_DELAY,
                          KEY_SET_REPEAT_INTERVAL)
    pygame.time.Clock().tick(TIME_CLOCK_TICK)

    big_loop = 1
    while big_loop:
        game_loop = 1
        menu_loop = 1
        nb_obj = 0
        # MENU LOOP ###############################################
        while menu_loop:
            message = Display_mess()
            message.display_message('3 objects : F1 - 4 objects : F2')
            for event in pygame.event.get():
                # Close window
                if event.type == QUIT \
                 or event.type == KEYDOWN \
                 and event.key == K_ESCAPE:
                    menu_loop = 0
                    game_loop = 0
                    big_loop = 0
                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        nb_obj = 3
                        menu_loop = 0
                    if event.key == K_F2:
                        nb_obj = 4
                        menu_loop = 0
        # END MENU LOOP ###########################################
        if nb_obj != 0:
            # Load & generate the maze from the file
            level = Maze(nb_obj)
            # Manage player movements and generate inventory
            player = Player(level)
            # Display the maze
            display = Display(level, player)

        # GAME LOOP ###############################################
        while game_loop:
            for event in pygame.event.get():
                # Close window
                if event.type == QUIT \
                 or event.type == KEYDOWN \
                 and event.key == K_ESCAPE:
                    game_loop = 0
                    menu_loop = 0
                    big_loop = 0
                # Keyboard reactions
                keys_events = {
                 'UP': K_UP,
                 'DOWN': K_DOWN,
                 'LEFT': K_LEFT,
                 'RIGHT': K_RIGHT,
                }
                if event.type == KEYDOWN:
                    for move, value in keys_events.items():
                        if event.key == value:
                            player.movement(move)
            # Re-paste images
            display.repaste_display(level, player)
            # Check Inventory
            player.loot(level)

            # Meeting BadGuy
            if (player.x, player.y) == level.coord_badguy:
                # Check inventory
                if len(player.inventory_list) != nb_obj:
                    message.display_message("Game Over - Try again ? (F1: Yes, F2: No)")
                    for event in pygame.event.get():
                        # Close window
                        if event.type == QUIT \
                         or event.type == KEYDOWN \
                         and event.key == K_ESCAPE:
                            game_loop = 0
                            menu_loop = 0
                            big_loop = 0
                        elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                game_loop = 0
                            if event.key == K_F2:
                                game_loop = 0
                                menu_loop = 0
                                big_loop = 0
                else:
                    display.badguy_sleeping = True

            # Check Exit
            if (player.x, player.y) == level.coord_outdoor:
                # Check if badguy is sleeping
                if display.badguy_sleeping is True:
                    message.display_message("You WIN ! - Try again ? (F1: Yes, F2: No)")
                    for event in pygame.event.get():
                        # Close window
                        if event.type == QUIT \
                         or event.type == KEYDOWN \
                         and event.key == K_ESCAPE:
                            game_loop = 0
                            menu_loop = 0
                            big_loop = 0
                        elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                game_loop = 0
                            if event.key == K_F2:
                                game_loop = 0
                                menu_loop = 0
                                big_loop = 0
                else:
                    message.display_message("Bad guy is still awake. Try again ? (F1: Yes, F2: No)")
                    for event in pygame.event.get():
                        # Close window
                        if event.type == QUIT \
                         or event.type == KEYDOWN \
                         and event.key == K_ESCAPE:
                            game_loop = 0
                            menu_loop = 0
                            big_loop = 0
                        elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                game_loop = 0
                            if event.key == K_F2:
                                game_loop = 0
                                menu_loop = 0
                                big_loop = 0
        # END GAME LOOP ##########################################


if __name__ == "__main__":

    main()
