# Libairies

import os
import time

from clock import *

# Functions

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def menu(clock, interval):

    clear()

    print("1. Display time")
    print("2. Update time")
    print("3. Set alarm")
    
    print("0. Quit")

    usr_input = input("Choose an option : ")
    
    if usr_input == "1":
        clear()
        new_interval = display_clock(clock, interval)
        clock = increment_clock(clock, int(new_interval - interval))
        interval = new_interval

    elif usr_input == "2":
        clock = set_clock()
        interval = time.monotonic()

    elif usr_input == "3":
        pass # à faire
    
    elif usr_input == "0":
        clear()
        return False, clock, interval
    
    return True, clock, interval

# Main program

if __name__ == "__main__":

    clock = set_clock()

    interval = time.monotonic()
    running = True
    while running:
        running, clock, interval = menu(clock, interval)