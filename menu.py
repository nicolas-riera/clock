# Librairies

from clear import clear
from error import error_messages
from clock import *
from alarm import *
import time

# Variables

display_format_24 = True
alarm = -1, -1, -1

# Functions

def menu(clock, interval):

    global display_format_24
    global alarm

    clear()

    print("1. Display time")
    print("2. Update time")
    print("3. Set alarm")
    print("4. Set 24h/12h mode")
    
    print("0. Quit")

    usr_input = input("Choose an option : ")
    
    if usr_input == "1":
        clear()
        new_interval, alarm = display_clock(clock, interval, display_format_24, alarm)
        clock = increment_clock(clock, new_interval - interval)
        interval = new_interval

    elif usr_input == "2":
        clock = set_clock()
        interval = time.monotonic()

    elif usr_input == "3":
        clear()

        if not(check_alarm((-1, -1, -1), alarm)):

            if display_format_24:
                alarm_text = f"{int(alarm[0]):02}:{int(alarm[1]):02}:{int(alarm[2]):02}"
            else:
                if alarm[0] >= 13:
                    alarm_text = f"{int(alarm[0])-12:02}:{int(alarm[1]):02}:{int(alarm[2]):02} PM"
                else:
                    alarm_text = f"{int(alarm[0]):02}:{int(alarm[1]):02}:{int(alarm[2]):02} AM"

            clear()

            print("1. Disable Alarm")
            print("0. Exit")
            
            print(f"An alarm is set : {alarm_text}")

            usr_alarm_input = input("Choose an option : ")

            if usr_alarm_input == "1":
                alarm = -1, -1, -1
                clear()
                print("Successfully disabled the alarm.")
                time.sleep(0.2)
                input("Press Enter to continue.")
                
            elif usr_alarm_input == "0":
                pass
            else:
                error_messages()
        else:
            alarm = set_alarm()

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
            else:
                error_messages()
    
    elif usr_input == "0":
        clear()
        return False, clock, interval
    else:
        error_messages()
    
    return True, clock, interval