"""Main file for MacGiver maze game."""
from maze import *
from player import *
import pygame
from pygame.locals import *
from config import *
import os


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
    level.perso_start_position(window)
    # Player movements
    player = Player(level)   



################################## GAME LOOP ################################
    pygame.key.set_repeat(key_set_repeat_delay,key_set_repeat_interval)
    pygame.time.Clock().tick(time_clock_tick)
    loop = 1
    sprite = sprites_size
    position_perso = level.perso_start_position
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT:
                loop = 0
            # Keyboard reactions    
            if event.type == KEYDOWN:
                # print(position_perso) # To Clean
                if event.key == K_UP:
                    # position_perso = (position_perso[0], position_perso[1]-1)                    
                    position_perso = player.movement('up')
                if event.key == K_DOWN:
                    # position_perso = (position_perso[0], position_perso[1]+1)
                    position_perso = player.movement('down')
                if event.key == K_LEFT:
                    # position_perso = (position_perso[0]-1, position_perso[1])
                    position_perso = player.movement('left')
                if event.key == K_RIGHT:
                    # position_perso = (position_perso[0]+1, position_perso[1])
                    position_perso = player.movement('right')
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
