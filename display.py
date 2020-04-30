"""Display's file for MacGiver maze game."""
import pygame
from config import window_size, img_rep, obj_rep, sprite
from lib import funct
from glob import glob


class Display:
    """Display the maze."""

    def __init__(self, level, player):
        """Initialize window add badguy status and launch display."""
        self.window = pygame.display.set_mode(window_size)
        # Boolean for Badguy status
        self.badguy_sleeping = False
        # Generate
        self.load_img()
        self.display_maze(level)
        self.display_objects(level, player)

    def load_img(self):
        """Load images, return a dictionnary."""
        # Return list of images paths
        img_list = glob(img_rep)+glob(obj_rep)

        # Create dictionnary of images paths
        self.img_dict = {funct.file_name(img_list[i]): img_list[i]
                         for i in range(len(img_list))}

    def display_maze(self, level):
        """Display maze using load_maze."""
        for x in range(len(level.maze)):
            for y in range(len(level.maze)):
                if level.maze[y][x] == 'W':
                    self.window.blit(funct.py_img(self.img_dict['wall']),
                                     (sprite*x, sprite*y))
                elif level.maze[y][x] == 'O':
                    level.coord_outdoor = (x, y)
                    self.window.blit(funct.py_img(self.img_dict['outdoor']),
                                     (sprite*x, sprite*y))
                elif level.maze[y][x] == 'G':
                    level.coord_badguy = (x, y)
                    # Check if badguy is sleeping
                    if self.badguy_sleeping is not True:
                        self.window.blit(funct.py_img(self.img_dict['badguy']),
                                         (sprite*x, sprite*y))

    def display_objects(self, level, player):
        """Display objects in the maze if not looted."""
        i = 0
        while i < len(level.dict_obj):
            for obj_numb, coord in level.dict_obj.items():
                # py_img = funct.py_img(objects_files[i])
                py_img = funct.py_img(glob(obj_rep)[i])
                if obj_numb not in player.inventory_list:
                    self.window.blit(py_img,
                                     (sprite*coord[0], sprite*coord[1]))
                i += 1

    def repaste_display(self, level, player):
        """Repaste display."""
        self.window.blit(funct.py_img(self.img_dict['background']), (0, 0))
        self.display_maze(level)
        self.display_objects(level, player)
        self.window.blit(funct.py_img(self.img_dict['macgyver']),
                         (player.x*sprite, player.y*sprite))
        # Refresh
        pygame.display.flip()
