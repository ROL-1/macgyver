"""Main file for MacGiver maze game."""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE,\
                          K_UP, K_DOWN, K_LEFT, K_RIGHT,\
                          K_F1, K_F2
import config
from maze import Maze
from player import Player
from display import Display_mess, Display_maze


def main():
    """Launch functions."""
    # Launch pygame
    pygame.init()

    # Pygame parameters
    pygame.key.set_repeat(config.KEY_SET_REPEAT_DELAY,
                          config.KEY_SET_REPEAT_INTERVAL)
    pygame.time.Clock().tick(config.TIME_CLOCK_TICK)

    big_loop = 1
    while big_loop:
        game_loop = 1
        menu_loop = 1
        # Print game count after first game
        if Display_maze.game_count != 0:
            Display_maze.print_count()

        # MENU LOOP ##########################################
        while menu_loop:
            nb_obj = 0
            message = Display_mess()
            message.display_message(config.MENU_MESS)
            for event in pygame.event.get():
                # Close window
                if event.type == QUIT \
                 or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    menu_loop = 0
                    big_loop = 0
                # Choose number of objects
                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        nb_obj = 3
                        menu_loop = 0
                    elif event.key == K_F2:
                        nb_obj = 4
                        menu_loop = 0
        # END MENU LOOP ######################################

        # Loads
        if nb_obj != 0:
            # Load & generate the maze from the file
            level = Maze(nb_obj)
            # Manage player movements and generate inventory
            player = Player(level)
            # Display the maze
            display_maze = Display_maze(level, player)

            # GAME LOOP ##########################################
            while game_loop:
                for event in pygame.event.get():
                    # Back to menu
                    if event.type == QUIT \
                     or (event.type == KEYDOWN
                       and event.key == K_ESCAPE):
                        game_loop = 0
                    # Movements reactions
                    keys_events = {
                     'UP': K_UP,
                     'DOWN': K_DOWN,
                     'LEFT': K_LEFT,
                     'RIGHT': K_RIGHT,
                    }
                    if event.type == KEYDOWN:
                        for move, value in keys_events.items():
                            if event.key == value:
                                player.movement(move, level)

                # Add loot in Inventory
                player.loot(level)
                # Re-paste images
                display_maze.repaste_display(level, player)

                # Meeting BadGuy
                if (player.x, player.y) == level.bad_guy_coord:
                    # Check inventory
                    if len(player.inventory_list) != nb_obj:
                        message.display_message(config.LOOSE_MESS)
                        for event in pygame.event.get():
                            # Close window
                            if event.type == QUIT \
                             or (event.type == KEYDOWN
                               and event.key == K_ESCAPE):
                                game_loop = 0
                                big_loop = 0
                            # Choose replay or quit
                            elif event.type == KEYDOWN:
                                if event.key == K_F1:
                                    game_loop = 0
                                elif event.key == K_F2:
                                    game_loop = 0
                                    big_loop = 0
                    else:
                        display_maze.badguy_sleeping = True

                # Check Exit
                if (player.x, player.y) == level.outdoor_coord:
                    # Check if badguy is sleeping
                    for event in pygame.event.get():
                        # Close window
                        if event.type == QUIT \
                         or (event.type == KEYDOWN
                           and event.key == K_ESCAPE):
                            game_loop = 0
                            big_loop = 0
                        # Choose replay or quit
                        elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                game_loop = 0
                            if event.key == K_F2:
                                game_loop = 0
                                big_loop = 0
                    if display_maze.badguy_sleeping is True:
                        message.display_message(config.WIN_MESS)
                    else:
                        message.display_message(config.CHEAT_MESS)
            # END GAME LOOP ######################################


if __name__ == "__main__":

    main()
