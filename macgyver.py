"""Main file for MacGiver maze game."""
from maze import *
from player import *
import pygame
from pygame.locals import *
from config import *


def main():
    """Launch functions."""
    pygame.init()
    # Load window
    window = pygame.display.set_mode(window_size)
    # Load & generate the maze from the file
    level = Create_maze()
    level.load_maze()
    # Display the maze
    level.display_maze(window)
    level.perso_start_position(window)
    # Player movements
    player = Player(level)
    inventory = []


################################## GAME LOOP ################################
    pygame.key.set_repeat(key_set_repeat_delay, key_set_repeat_interval)
    pygame.time.Clock().tick(time_clock_tick)
    loop = 1
    sprite = sprites_size
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT:
                loop = 0
            # Keyboard reactions
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = player.movement('up')
                if event.key == K_DOWN:
                    position_perso = player.movement('down')
                if event.key == K_LEFT:
                    position_perso = player.movement('left')
                if event.key == K_RIGHT:
                    position_perso = player.movement('right')

        # Check Exit
        if (player.x, player.y) == level.position_outdoor:
            print('YOU WIN!')
            loop = 0

        # Check Inventory
        player.inventory(level, inventory)

        # Meeting BadGuy
        if (player.x, player.y) == level.position_badguy:
            if len(inventory) != 3:
                print('YOU LOOSE')
                loop = 0
            else:
                level.badguy_sleeping = True
                print('BadGuy is Sleeping !\nBadGuy is Sleeping !\n')

        # Re-paste images
        background = pygame.image.load(background_file).convert()
        perso = pygame.image.load(perso_file).convert_alpha()
        window.blit(background, (0, 0))
        level.display_maze(window)
        window.blit(perso, (player.x*sprite, player.y*sprite))
        # Refresh
        pygame.display.flip()
################################# END GAME LOOP ##############################

main()
