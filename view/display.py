"""Display's file for MacGiver maze game."""
import pygame
from types import SimpleNamespace

from pygame import display, font, Color

import config
from libs.py_lib import py_img
from libs.paths_lib import file_name, glob_path


class Display_mess:
    """Display messages."""
    # Launch pygame
    pygame.init()

    # Pygame parameters
    pygame.key.set_repeat(config.KEY_SET_REPEAT_DELAY,
                          config.KEY_SET_REPEAT_INTERVAL)
    pygame.time.Clock().tick(config.TIME_CLOCK_TICK)

    window_mess = display.set_mode(config.WINDOW_SIZE)

    def display_message(self, message):
        """Create font and message screen to display messages."""
        font_ = font.Font(None, 44)
        # Margins and background
        x, y = 20, 20
        type(self).window_mess.fill(Color("BLACK"))
        # Read message
        lines = message.splitlines()
        # Display message
        for i, line in enumerate(lines):
            line_py = font_.render(line, True, Color("WHITE"))
            type(self).window_mess.blit(line_py, (x, y + 44 * i))
        display.update()


class Display_maze:
    """Display the maze."""

    window = display.set_mode(config.WINDOW_SIZE)

    def __init__(self, maze, player):
        """Initialize window add badguy status and launch display."""
        # Boolean for Badguy status
        self.badguy_sleeping = False
        # Generate
        self.load_img()
        self._display_sprites(maze)
        self._display_objects(maze, player)

    def load_img(self):
        """Load images, return paths."""
        # Return list of images paths
        img_paths = []
        for ext in ('/*.png', '/*.jpg'):
            img_paths.extend(glob_path(config.IMG_REP+ext))
        # Create dictionnary of images paths
        self.img_paths = {file_name(img_paths[i]): img_paths[i]
                          for i in range(len(img_paths))}

    def _display_sprites(self, maze):
        """Display maze using load_maze."""
        n = SimpleNamespace(**self.img_paths)
        for coord in maze.walls_spaces_list:
            type(self).window.blit(py_img(n.wall),
                                   (config.SPRITE * coord[0],
                                    config.SPRITE * coord[1]))
        type(self).window.blit(py_img(n.outdoor),
                               (config.SPRITE * maze.outdoor_coord[0],
                                config.SPRITE * maze.outdoor_coord[1]))
        if self.badguy_sleeping is False:
            type(self).window.blit(py_img(n.badguy),
                                   (config.SPRITE * maze.bad_guy_coord[0],
                                    config.SPRITE * maze.bad_guy_coord[1]))

    def _display_objects(self, maze, player):
        """Display objects in the maze if not looted."""
        i = 0
        while i < len(maze.list_coord_obj):
            for coord in maze.list_coord_obj:
                img = py_img(glob_path(config.OBJ_REP + '/*')[i])
                if coord not in player.inventory_list:
                    type(self).window.blit(img,
                                           (config.SPRITE * coord[0],
                                            config.SPRITE * coord[1]))
                i += 1

    def repaste_display(self, maze, player):
        """Repaste display."""
        n = SimpleNamespace(**self.img_paths)
        type(self).window.blit(py_img(n.background), (0, 0))
        self._display_sprites(maze)
        self._display_objects(maze, player)
        type(self).window.blit(py_img(n.macgyver),
                               (player.perso_coord[0] * config.SPRITE,
                                player.perso_coord[1] * config.SPRITE))
        # Refresh
        display.flip()
