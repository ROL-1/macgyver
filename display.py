"""Display's file for MacGiver maze game."""
from glob import glob
from pygame import display
from config import conf_display
from lib import funct
import pygame


class Display_mess:
    """Display messages."""

    def display_message(self, message):
        """Create police and message screen to display messages."""
        menu_window = display.set_mode((850, 250))
        police = pygame.font.Font(None, 44)
        texte = police.render(message, True, pygame.Color("WHITE"))
        rectTexte = texte.get_rect()
        rectwindow = menu_window.get_rect()
        rectTexte.center = rectwindow.center
        menu_window.fill(pygame.Color("BLACK"))
        menu_window.blit(texte, rectTexte)
        pygame.display.update()


class Display:
    """Display the maze."""

    def __init__(self, level, player):
        """Initialize window add badguy status and launch display."""
        # Load constants
        globals().update(conf_display)
        self.window = display.set_mode(WINDOW_SIZE)
        # Boolean for Badguy status
        self.badguy_sleeping = False
        # Generate
        self.load_img()
        self.display_maze(level)
        self.display_objects(level, player)

    def load_img(self):
        """Load images, return paths as globals variables."""
        # Return list of images paths
        img_list = glob(IMG_REP+'\\*')+glob(OBJ_REP+'\\*')
        # Create dictionnary of images paths
        img_dict = {funct.file_name(img_list[i]): img_list[i]
                    for i in range(len(img_list))}
        # Return each name/path as globals variables
        globals().update(img_dict)

    def display_maze(self, level):
        """Display maze using load_maze."""
        for x in range(len(level.maze)):
            for y in range(len(level.maze)):
                if level.maze[y][x] == 'W':
                    self.window.blit(funct.py_img(wall),
                                     (SPRITE*x, SPRITE*y))
                elif level.maze[y][x] == 'O':
                    level.coord_outdoor = (x, y)
                    self.window.blit(funct.py_img(outdoor),
                                     (SPRITE*x, SPRITE*y))
                elif level.maze[y][x] == 'G':
                    level.coord_badguy = (x, y)
                    # Check if badguy is sleeping
                    if self.badguy_sleeping is not True:
                        self.window.blit(funct.py_img(badguy),
                                         (SPRITE*x, SPRITE*y))

    def display_objects(self, level, player):
        """Display objects in the maze if not looted."""
        i = 0
        while i < len(level.dict_obj):
            for obj_numb, coord in level.dict_obj.items():
                py_img = funct.py_img(glob(OBJ_REP+'\\*')[i])
                if obj_numb not in player.inventory_list:
                    self.window.blit(py_img,
                                     (SPRITE*coord[0], SPRITE*coord[1]))
                i += 1

    def repaste_display(self, level, player):
        """Repaste display."""
        self.window.blit(funct.py_img(background), (0, 0))
        self.display_maze(level)
        self.display_objects(level, player)
        self.window.blit(funct.py_img(macgyver),
                         (player.x*SPRITE, player.y*SPRITE))
        # Refresh
        display.flip()
