"""Main file for MacGiver maze game."""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from maze import Maze
from player import Player
from display import Display
from config import key_set_repeat_delay, key_set_repeat_interval, \
                   time_clock_tick, nb_obj, keys_events


def main():
    """Launch functions."""
    # Launch pygame
    pygame.init()
    # Load & generate the maze from the file
    level = Maze()
    # Generate player firt position, movements and inventory
    player = Player(level)
    # Display the maze
    display = Display(level, player)

# GAME LOOP ###################################################################
    pygame.key.set_repeat(key_set_repeat_delay, key_set_repeat_interval)
    pygame.time.Clock().tick(time_clock_tick)
    loop = 1
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT \
             or event.type == KEYDOWN \
             and event.key == K_ESCAPE:
                loop = 0
            # Keyboard reactions
            if event.type == KEYDOWN:
                for move in keys_events:
                    if event.key == move:
                        player.movement(move)

        # Check Inventory
        player.loot(level)

        # Meeting BadGuy
        if (player.x, player.y) == level.coord_badguy:
            # Check inventory
            if len(player.inventory_list) != nb_obj:
                print('YOU LOOSE.')
                loop = 0
            else:
                display.badguy_sleeping = True

        # Check Exit
        if (player.x, player.y) == level.coord_outdoor:
            # Check if badguy is sleeping
            if display.badguy_sleeping is True:
                print('YOU WIN!')
                loop = 0
            else:
                print('Bad guy is still awake.\nYOU CHEAT')
                loop = 0

        # Re-paste images
        display.repaste_display(level, player)

# END GAME LOOP ###############################################################


if __name__ == "__main__":

    main()
