"""References and parameters for files."""
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

# maze construction file
level_config_file = [
 "level_config_1.json",
 "level_config_2.json"
]
# LEGEND FOR LEVEL CONFIG ####
# W : is a Wall
# E : is Empty
# M : is MacGyver start position
# B : is BadGuy start position
# O : is the Outdoor (need to be next to BadGuy)


# Images ###################################
# Maze
background_file = "images/background.jpg"
outdoor_file = "images/outdoor.png"
wall_file = "images/wall.png"
badguy_file = "images/badguy.png"
# Player
perso_file = "images/macgyver.png"
# Objects
objects_files = [
    "images/ether.png",
    "images/needle.png",
    "images/pipe.png",
    # "images/syringe.png"
]
############################################

# Sprites sizes (pixels)
sprite = 30

# Number of objetcs
nb_obj = len(objects_files)


# Window size (x pixels, y pixels)
window_size = (450, 450)

# Pygame parameters
key_set_repeat_delay = 400    # (milliseconds)
key_set_repeat_interval = 30  # (milliseconds)
time_clock_tick = (30)        # (milliseconds)

# Keyboard events
keys_events = [
 K_UP,
 K_DOWN,
 K_LEFT,
 K_RIGHT
]
