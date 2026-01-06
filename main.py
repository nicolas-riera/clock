# Libairies

import time

from clock import *
from menu import menu

# Variables

running = True
display_format_24 = True

# Main program

if __name__ == "__main__":

    clock = set_clock()

    interval = time.monotonic()

    while running:
        running, clock, interval = menu(clock, interval)