"""Display's file for MacGiver maze game."""
from glob import glob
from pygame import display, font, Color
import config
from lib import funct


class Display_mess:
    """Display messages."""

    window_mess = display.set_mode(config.WINDOW_SIZE)

    def display_message(self, message):
        """Create font and message screen to display messages."""
        font_ = font.Font(None, 44)
        x, y = 20, 20
        type(self).window_mess.fill(Color("BLACK"))
        lines = message.splitlines()
        for i, line in enumerate(lines):
            line_py = font_.render(line, True, Color("WHITE"))
            type(self).window_mess.blit(line_py, (x, y + 44 * i))
        display.update()


class Display_maze:
    """Display the maze."""

    window = display.set_mode(config.WINDOW_SIZE)

    def __init__(self, level, player):
        """Initialize window add badguy status and launch display."""
        type(self).window = display.set_mode(config.WINDOW_SIZE)
        # Boolean for Badguy status
        self.badguy_sleeping = False
        # Generate
        self.load_img()
        self.display_sprites(level)
        self.display_objects(level, player)

    def load_img(self):
        """Load images, return paths."""
        # Return list of images paths
        img_list = glob(config.IMG_REP + '/*') + glob(config.OBJ_REP + '/*')
        # Create dictionnary of images paths
        self.img_dict = {funct.file_name(img_list[i]): img_list[i]
                         for i in range(len(img_list))}

    def display_sprites(self, level):
        """Display maze using load_maze."""
        for x in range(len(level.frame)):
            for y in range(len(level.frame)):
                if level.frame[y][x] == 'W':
                    type(self).window.blit(
                        funct.py_img(self.img_dict['wall']),
                        (config.SPRITE * x, config.SPRITE * y))
                elif level.frame[y][x] == 'O':
                    level.coord_outdoor = (x, y)
                    type(self).window.blit(
                        funct.py_img(self.img_dict['outdoor']),
                        (config.SPRITE * x, config.SPRITE * y))
                elif level.frame[y][x] == 'G':
                    level.coord_badguy = (x, y)
                    # Check if badguy is sleeping
                    if self.badguy_sleeping is not True:
                        type(self).window.blit(
                            funct.py_img(self.img_dict['badguy']),
                            (config.SPRITE * x, config.SPRITE * y))

    def display_objects(self, level, player):
        """Display objects in the maze if not looted."""
        i = 0
        while i < len(level.dict_obj):
            for obj_numb, coord in level.dict_obj.items():
                py_img = funct.py_img(glob(config.OBJ_REP + '/*')[i])
                if obj_numb not in player.inventory_list:
                    type(self).window.blit(
                        py_img,
                        (config.SPRITE * coord[0], config.SPRITE * coord[1]))
                i += 1

    def repaste_display(self, level, player):
        """Repaste display."""
        type(self).window.blit(funct.py_img(self.img_dict['background']),
                               (0, 0))
        self.display_sprites(level)
        self.display_objects(level, player)
        type(self).window.blit(
            funct.py_img(self.img_dict['macgyver']),
            (player.x * config.SPRITE, player.y * config.SPRITE))
        # Refresh
        display.flip()
