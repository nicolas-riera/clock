# Librairies

from main import clear
import time
import datetime

# Variables

hour_list = [str(i) for i in range(24)]
minute_second_list = [str(i) for i in range(60)]

# Functions

def set_clock()->tuple:

    clear()
    
    usr_time_hour = input("Enter hours (0-23) : ")
    usr_time_minutes = input("Enter minutes (0-59) : ")
    usr_time_seconds = input("Enter seconds (0-59) : ")

    if usr_time_hour in hour_list and usr_time_minutes in minute_second_list and usr_time_seconds in minute_second_list:
        return int(usr_time_hour), int(usr_time_minutes), int(usr_time_seconds)
    else:
        set_clock()

def increment_clock(clock, increment):

    clock_incremented = datetime.timedelta(hours=clock[0], 
                        minutes=clock[1], seconds=clock[2]) + datetime.timedelta(seconds=increment)
    return (clock_incremented.seconds // 3600, (clock_incremented.seconds % 3600) // 60, clock_incremented.seconds % 60)

def display_clock(clock:tuple, interval):

    try :
        while 1:
            clear()
            clock = increment_clock(clock, time.monotonic() - interval)
            interval = time.monotonic()
            print(f"{clock[0]}:{clock[1]}:{clock[2]}")
            print("\n(Press Ctrl + C to exit)")
            time.sleep(1)

        return interval
    except KeyboardInterrupt:

        return interval