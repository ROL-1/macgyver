"""References and parameters for MacGiver maze game."""

# Check number of objects in repertory
NB_OBJ = 3

# Sprites sizes (pixels)
SPRITE = 30

# Window size (x pixels, y pixels)
WINDOW_SIZE = (450, 450)

# Pygame parameters
KEY_SET_REPEAT_DELAY = 400    # (milliseconds)
KEY_SET_REPEAT_INTERVAL = 30  # (milliseconds)
TIME_CLOCK_TICK = (30)        # (milliseconds)

# Images repertory
# type : 'path\\to\\my\\repertory
IMG_REP = 'images'
OBJ_REP = 'images\\objects'

# Levels repertory
LEVELS_REP = 'levels'

# LEGEND FOR LEVEL CONFIG ####
# W : is a Wall
# E : is Empty
# M : is MacGyver start position
# B : is BadGuy start position
# O : is the Outdoor (need to be next to BadGuy)
