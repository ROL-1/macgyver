"""Main file for MacGiver maze game."""
from maze import Create_maze
from player import Player
import pygame
from pygame.locals import *
from config import *
from config import sprite


def main():
    """Launch functions."""
    pygame.init()
    # Load window
    window = pygame.display.set_mode(window_size)
    # Load & generate the maze from the file
    level = Create_maze()
    level.load_maze()
    level.empty_spaces()
    # Display the maze
    level.display_maze(window)
    level.perso_start_coord(window)
    # Player movements
    player = Player(level)
    inventory = []

################################## GAME LOOP ################################
    pygame.key.set_repeat(key_set_repeat_delay, key_set_repeat_interval)
    pygame.time.Clock().tick(time_clock_tick)
    loop = 1
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                loop = 0
            # Keyboard reactions
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    coord_perso = player.movement('up')
                if event.key == K_DOWN:
                    coord_perso = player.movement('down')
                if event.key == K_LEFT:
                    coord_perso = player.movement('left')
                if event.key == K_RIGHT:
                    coord_perso = player.movement('right')
   
        # Check Inventory
        player.inventory(level, inventory)

        # Meeting BadGuy
        if (player.x, player.y) == level.coord_badguy:
            if len(inventory) != nb_obj:
                print('YOU LOOSE.')
                loop = 0
            else:
                level.badguy_sleeping = True

        # Check Exit
        if (player.x, player.y) == level.coord_outdoor:
            if level.badguy_sleeping is True:
                print('YOU WIN!')
                loop = 0  
            else:
                print('YOU LOOSE.')    
                loop = 0                       

        # Re-paste images
        background = pygame.image.load(background_file).convert()
        perso = pygame.image.load(perso_file).convert_alpha()
        window.blit(background, (0, 0))
        level.display_maze(window)
        level.display_objects(window)
        window.blit(perso, (player.x*sprite, player.y*sprite))
        # Refresh
        pygame.display.flip()
################################# END GAME LOOP ##############################

if __name__ == "__main__":
    
    main()