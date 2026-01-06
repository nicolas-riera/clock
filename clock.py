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
        return set_clock()

def increment_clock(clock, increment):

    clock_incremented = datetime.timedelta(hours=clock[0], 
                        minutes=clock[1], seconds=clock[2]) + datetime.timedelta(seconds=increment)
    
    total_seconds = int(clock_incremented.total_seconds()) % 86400

    return (total_seconds // 3600, (total_seconds  % 3600) // 60, total_seconds % 60)

def display_clock(clock:tuple, interval):

    try :
        while True:
            
            now = time.monotonic()
            clock = increment_clock(clock, now - interval)
            interval = now

            clear()
            print(f"{clock[0]:02}:{clock[1]:02}:{clock[2]:02}")
            print("\n(Press Ctrl + C to open the menu)")
            time.sleep(1)
    
    except KeyboardInterrupt:
        
        return interval