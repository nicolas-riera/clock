# Librairies

from src.clear import clear
from src.error import error_messages
from src.alarm import *

try :
    import pyfiglet
except:
    print("pyfiglet is required, please install it : pip install pyfiglet")
    exit()
    
import time
import datetime
import os

try:
    from playsound3 import playsound
except:
    print("playsound3 is required, please install it : pip install playsound3")
    exit()

# Variables

HOUR_LIST = [str(i) for i in range(24)] + [str(i).zfill(2) for i in range(10)]
MINUTE_SECOND_LIST = [str(i) for i in range(60)] + [str(i).zfill(2) for i in range(10)]
alarm_ring = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Functions

def set_clock()->tuple:

    clear()
    
    usr_time_hour = input("Enter hours (0-23) : ")
    usr_time_minutes = input("Enter minutes (0-59) : ")
    usr_time_seconds = input("Enter seconds (0-59) : ")

    if usr_time_hour in HOUR_LIST and usr_time_minutes in MINUTE_SECOND_LIST and usr_time_seconds in MINUTE_SECOND_LIST:
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
                clock_font = pyfiglet.figlet_format(f"{int(current_clock[0]):02}:{int(current_clock[1]):02}:{int(current_clock[2]):02}", font = "lcd")
            else:
                if current_clock[0] >= 13:
                    clock_font = pyfiglet.figlet_format(f"{int(current_clock[0])-12:02}:{int(current_clock[1]):02}:{int(current_clock[2]):02} PM", font = "lcd")
                else:
                    clock_font = pyfiglet.figlet_format(f"{int(current_clock[0]):02}:{int(current_clock[1]):02}:{int(current_clock[2]):02} AM", font = "lcd")
      
            print(f"\033[1;1H{clock_font}", end="", flush=True)

            print("(Press Ctrl + C to open the menu)")

            if check_alarm((int(f"{int(current_clock[0]):02}"),int(f"{int(current_clock[1]):02}"), int(f"{int(current_clock[2]):02}")), alarm):
                alarm = -1, -1, -1
                alarm_ring = 15
                playsound((os.path.join(BASE_DIR, "media", "alarm.mp3")), block=False)
            
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