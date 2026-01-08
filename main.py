# Libairies

import time

from clock import *
from menu import menu

# Variables

running = True

# Main program

if __name__ == "__main__":

    # Verification to check if the user has a new enough version of Python
    try: 
        match running:
            case _:
                pass
    except:
        print("Your version of Python is too old, please update to Python 3.10+")
        exit()

    clock, pause_offset = set_clock()

    interval = time.monotonic()

    while running:
        running, clock, interval, pause_offset = menu(clock, interval, pause_offset)