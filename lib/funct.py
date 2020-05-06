"""Generic functions for MacGiver maze game."""
from os import listdir
from os.path import basename, isfile, join, splitext
from json import load
from pygame import image


def list_files(path):
    """Make list of all path files in a directory."""
    return [join(path, f) for f in listdir(path)
            if isfile(join(path, f))]


def string_json(path):
    """Read a .json and return a dictionary."""
    with open(path) as json_data:
        return load(json_data)


def py_img(path):
    """Convert images for pygame."""
    return image.load(path).convert_alpha()


def file_name(path):
    """Return the name of a file, without extension."""
    return basename(splitext(path)[0])
