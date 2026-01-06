# Libairies

import os
import time

from clock import *

# Variables

running = True
display_format_24 = True

# Functions

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def menu(clock, interval):

    global display_format_24

    clear()

    print("1. Display time")
    print("2. Update time")
    print("3. Set alarm")
    print("4. Set 24h/12h mode")
    
    print("0. Quit")

    usr_input = input("Choose an option : ")
    
    if usr_input == "1":
        clear()
        new_interval = display_clock(clock, interval, display_format_24)
        clock = increment_clock(clock, int(new_interval - interval))
        interval = new_interval

    elif usr_input == "2":
        clock = set_clock()
        interval = time.monotonic()

    elif usr_input == "3":
        pass # à faire

    elif usr_input == "4":

        usr_input_mode = "-1"

        while usr_input_mode != "1" and usr_input_mode != "2":
            clear()

            print("1. 24h")
            print("2. 12h")

            usr_input_mode = input("Choose an option : ")

        if usr_input_mode == "1":
            display_format_24 = True
        elif usr_input_mode == "2":
            display_format_24 = False
    
    elif usr_input == "0":
        clear()
        return False, clock, interval
    
    return True, clock, interval

# Main program

if __name__ == "__main__":

    clock = set_clock()

    interval = time.monotonic()

    while running:
        running, clock, interval = menu(clock, interval)