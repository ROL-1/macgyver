"""References and parameters for files."""

# maze construction file
level_config_file = "level_config_1.json"


# Images ###################################
# Maze
background_file = "images/background.jpg"
# Player
perso_file = "images/macgyver.png"

outdoor_file = "images/outdoor.png"
wall_file = "images/wall.png"
# BadGuy and Objects
badguy_file = "images/badguy.png"

objects_files = [
    "images/ether.png",
    "images/needle.png",
    "images/pipe.png"
]
############################################

# Sprites sizes (pixels)
sprite = 30

# Number of objetcs
nb_obj = 3


# Window size (x pixels, y pixels)
window_size = (450, 450)

# Pygame parameters
key_set_repeat_delay = 400    # (milliseconds)
key_set_repeat_interval = 30  # (milliseconds)
time_clock_tick = (30)        # (milliseconds)
