"""References and parameters for MacGiver maze game."""
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

# LEGEND FOR LEVEL CONFIG ####
# W : is a Wall
# E : is Empty
# M : is MacGyver start position
# B : is BadGuy start position
# O : is the Outdoor (need to be next to BadGuy)

# Levels repertory
levels_rep = 'levels'
# Images repertory
img_rep = 'images\\*'
obj_rep = 'images\\*\\*'

# Sprites sizes (pixels)
sprite = 30

# Number of objetcs
nb_obj = 4


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
