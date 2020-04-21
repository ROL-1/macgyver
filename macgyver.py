"""Main file for MacGiver Labyrinth game."""
from classes import *
import pygame
from pygame.locals import *


def main():
    """Launch functions."""
    pygame.init()
    # Load window
    window = pygame.display.set_mode((450, 450))
    # Load & generate the labyrinth from the file
    level = Create_labyrinth()
    level.load_labyrinth()
    # Display the labyrinth
    level.display_labyrinth(window)
    # Generate player's perso
    player = Perso(window)

################################## GAME LOOP ################################
    pygame.key.set_repeat(400, 30)
    pygame.time.Clock().tick(30)
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.position_perso = player.position_perso.move(0, -30)
                if event.key == K_DOWN:
                    player.position_perso = player.position_perso.move(0, 30)
                if event.key == K_LEFT:
                    player.position_perso = player.position_perso.move(-30, 0)
                if event.key == K_RIGHT:
                    player.position_perso = player.position_perso.move(30, 0)
        # Re-paste
        background = pygame.image.load("images/background.jpg").convert()
        perso = pygame.image.load("images/perso.png").convert_alpha()
        window.blit(background, (0, 0))
        level.display_labyrinth(window)
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
