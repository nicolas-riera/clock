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

    clock = increment_clock(clock, time.monotonic() - interval)
    interval = time.monotonic()
    
    if usr_input == "1":
        interval = display_clock(clock, interval)
    elif usr_input == "2":
        set_clock()
    elif usr_input == "3":
        pass # à faire
    elif usr_input == "0":
        return False
    
    return True

# Main program

if __name__ == "__main__":

    clock = set_clock()

    interval = time.monotonic()
    running = True
    while running:
        running = menu(clock, interval)