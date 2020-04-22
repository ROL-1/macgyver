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
    window = pygame.display.set_mode(windows_size)
    # Load & generate the maze from the file
    level = Create_maze()
    level.load_maze()
    # Display the maze
    level.display_maze(window)
    # Generate player's perso
    player = Perso(window)

################################## GAME LOOP ################################
    pygame.key.set_repeat(key_set_repeat_delay,key_set_repeat_interval)
    pygame.time.Clock().tick(time_clock_tick)
    loop = 1
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT:
                loop = 0
            # Keyboard reactions    
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.position_perso = player.position_perso.move(0, -sprites_size)
                if event.key == K_DOWN:
                    player.position_perso = player.position_perso.move(0, sprites_size)
                if event.key == K_LEFT:
                    player.position_perso = player.position_perso.move(-sprites_size, 0)
                if event.key == K_RIGHT:
                    player.position_perso = player.position_perso.move(sprites_size, 0)
        # Re-paste images
        background = pygame.image.load(background_file).convert()
        perso = pygame.image.load(perso_file).convert_alpha()
        window.blit(background, (0, 0))
        level.display_maze(window)
        window.blit(perso, (player.position_perso))
        # Refresh
        pygame.display.flip()
################################# END GAME LOOP ##############################

main()


############################### TO DO ######################
#  Inventory:
#     """Return True when all items are looted"""
#     #list of objects on MacGyver

#  Loots:
#     """Rules when MacGyver come on Loots cell"""
#     # Erase the loot on the graph and make a empty cell
#     # Add the loot in the Inventory list

#  Badguy:
#     """Rules when MacGyver come on BadGuy cell"""

#     # Check Inventory list
#     # Kill MacGyver
#     # Is killed by MacGyver

#  Outdoor:
#     """Rules when MacGyver come on Outdoor cell"""

#     # Win condition when MacGyver is on the cell
#     # STOP PROGRAM
############################ END TO DO ######################
