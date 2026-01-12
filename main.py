# Libairies

import time
import sys

from src.clock import *
from src.menu import menu

# Variables

running = True

# Main program

if __name__ == "__main__":

    clock, pause_offset = set_clock()

    interval = time.monotonic()

    while running:
        running, clock, interval, pause_offset = menu(clock, interval, pause_offset)