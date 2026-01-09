# Libairies

import time
import sys

from assets.clock import *
from assets.menu import menu

# Variables

running = True

# Main program

if __name__ == "__main__":

    # Verification to check if the user has a new enough version of Python
    if sys.version_info < (3, 10):
        print("Your version of Python is too old, please update to Python 3.10+")
        exit()

    clock, pause_offset = set_clock()

    interval = time.monotonic()

    while running:
        running, clock, interval, pause_offset = menu(clock, interval, pause_offset)