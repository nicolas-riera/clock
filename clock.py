# Librairies

from clear import clear
from error import error_messages
from alarm import *

import time
import datetime

try:
    from playsound3 import playsound
except:
    print("playsound3 is required, please install it : pip install playsound3")
    exit()

# Variables

hour_list = [str(i) for i in range(24)] + [str(i).zfill(2) for i in range(10)]
minute_second_list = [str(i) for i in range(60)] + [str(i).zfill(2) for i in range(10)]
alarm_ring = 0

# Functions

def set_clock()->tuple:

    clear()
    
    usr_time_hour = input("Enter hours (0-23) : ")
    usr_time_minutes = input("Enter minutes (0-59) : ")
    usr_time_seconds = input("Enter seconds (0-59) : ")

    if usr_time_hour in hour_list and usr_time_minutes in minute_second_list and usr_time_seconds in minute_second_list:
        return (int(usr_time_hour), int(usr_time_minutes), int(usr_time_seconds)), 0.0
    else:
        error_messages()
        return set_clock()

def increment_clock(clock, increment):

    clock_incremented = datetime.timedelta(hours=clock[0], 
                        minutes=clock[1], seconds=clock[2]) + datetime.timedelta(seconds=increment)
    
    total_seconds = clock_incremented.total_seconds() % 86400

    return (total_seconds // 3600, (total_seconds  % 3600) // 60, total_seconds % 60)

def display_clock(clock:tuple, interval, display_format_24, alarm, pause_offset):

    try :

        global alarm_ring
        start_monotonic = interval 
        base_clock = clock

        print("\033[?25l", end="", flush=True)

        while True:
            
            now = time.monotonic()
            elapsed = now - start_monotonic - pause_offset
            current_clock = increment_clock(base_clock, elapsed)

            if display_format_24:
                print(f"\033[1;1H{int(current_clock[0]):02}:{int(current_clock[1]):02}:{int(current_clock[2]):02}", end="", flush=True)
            else:
                if current_clock[0] >= 13:
                    print(f"\033[1;1H{int(current_clock[0])-12:02}:{int(current_clock[1]):02}:{int(current_clock[2]):02} PM", end="", flush=True)
                else:
                    print(f"\033[1;1H{int(current_clock[0]):02}:{int(current_clock[1]):02}:{int(current_clock[2]):02} AM", end="", flush=True)

            print("\n\n(Press Ctrl + C to open the menu)")

            if check_alarm((int(f"{int(current_clock[0]):02}"),int(f"{int(current_clock[1]):02}"), int(f"{int(current_clock[2]):02}")), alarm):
                alarm = -1, -1, -1
                alarm_ring = 15
                playsound("alarm.mp3", block=False)
            
            if alarm_ring > 1:
                alarm_ring -= 1
                print("\n Alarm is ringing!!!")
            
            now = time.monotonic()
            sleep_time = 1 - (now % 1)
            time.sleep(sleep_time)

            if alarm_ring == 1:
                alarm_ring = 0
                clear()
    
    except KeyboardInterrupt:
        
        print("\033[?25h", end="", flush=True)

        elapsed = now - start_monotonic - pause_offset
        final_clock = increment_clock(base_clock, elapsed)

        return final_clock, now, alarm