"""References and parameters for MacGiver maze game."""

# Pygame parameters
KEY_SET_REPEAT_DELAY = 400    # (milliseconds)
KEY_SET_REPEAT_INTERVAL = 30  # (milliseconds)
TIME_CLOCK_TICK = 30          # (milliseconds)

# Levels repertory
LEVELS_REP = 'levels'

# Sprites sizes (pixels)
SPRITE = 30

# Window size (x pixels, y pixels)
WINDOW_SIZE = (450, 450)

# Images repertory
# type = 'path/to/repertory
IMG_REP = 'images'
OBJ_REP = 'images/objects'

# Messages
MENU_MESS = """Help MacGyver to escape!

Please, choose if you want :
- 3 objects : press F1
- 4 objects : press F2

And good luck."""

LOOSE_MESS = """Game Over


Try again ?

- F1: Yes
- F2: No"""

WIN_MESS = """You WIN !

Try again ?

- F1: Yes
- F2: No"""

CHEAT_MESS = """Hum... Bad guy is still awake.
Are you a cheater ?

Try again ?

- F1: Yes
- F2: No"""
