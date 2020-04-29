"""Main file for MacGiver maze game."""
from display import Display
from maze import Maze
from player import Player
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from config import \
    sprite, key_set_repeat_delay, key_set_repeat_interval, \
    time_clock_tick, window_size, background_file, perso_file, \
    nb_obj, keys_events


def main():
    """Launch functions."""
    pygame.init()
    # Load window
    window = pygame.display.set_mode(window_size)
    # Load & generate the maze from the file
    level = Maze()    
    player = Player(level)
    # Display the maze
    display = Display(level,player)

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
        player.inventory(level)
        # player.inventory_list = inventory
        print(player.inventory_list) #To Clean
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
        display.repaste_display(level,player)
        # background = pygame.image.load(background_file).convert()
        # perso = pygame.image.load(perso_file).convert_alpha()
        # window.blit(background, (0, 0))
        # level.display_maze(window)
        # level.display_objects(window, inventory)
        # window.blit(perso, (player.x*sprite, player.y*sprite))
        # # Refresh
        # pygame.display.flip()

# END GAME LOOP ###############################################################


if __name__ == "__main__":

    main()
