# Librairies

from clear import clear
from error import error_messages

# Variables

hour_list = [str(i) for i in range(24)] + [str(i).zfill(2) for i in range(10)]
minute_second_list = [str(i) for i in range(60)] + [str(i).zfill(2) for i in range(10)]

# Functions

def set_alarm():
    clear()
    
    usr_alarm_hour = input("Enter hours (0-23) : ")
    usr_alarm_minutes = input("Enter minutes (0-59) : ")
    usr_alarm_seconds = input("Enter seconds (0-59) : ")

    if usr_alarm_hour in hour_list and usr_alarm_minutes in minute_second_list and usr_alarm_seconds in minute_second_list:

        return int(usr_alarm_hour), int(usr_alarm_minutes), int(usr_alarm_seconds)
    
    else:
        error_messages()
        return set_alarm()

def check_alarm(clock, alarm):
    return clock == alarm