# Libairies

import os
import time

# Variables

clock = (0, 0, 0)

hour_list = [str(i) for i in range(24)]
minute_second_list = [str(i) for i in range(60)]

# Functions

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def menu():

    clear()

    print("1. Display time")
    print("2. Update time")
    print("3. Set alarm")

    usr_input = input("Choose an option : ")

    if usr_input == "1":
        pass
    elif usr_input == "2":
        set_clock()
    elif usr_input == "3":
        pass
    else:
        menu()

def set_clock():

    clear()
    
    usr_time_hour = input("Enter hours (0-23) : ")
    usr_time_minutes = input("Enter minutes (0-59) : ")
    usr_time_seconds = input("Enter seconds (0-59) : ")

    if usr_time_hour in hour_list and usr_time_minutes in minute_second_list and usr_time_seconds in minute_second_list:
        return int(usr_time_hour), int(usr_time_minutes), int(usr_time_seconds)
    else:
        set_clock()

def display_clock():

    clear()

    print(f"{clock[0]}:{clock[1]}:{clock[2]}")

# Main program

clock = set_clock()

while 1:
    display_clock()
    time.sleep(1)