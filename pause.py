# Librairies

from clear import clear

import time

try :
    import pyfiglet
except:
    print("pyfiglet is required, please install it : pip install pyfiglet")
    exit()

# Functions

def pause_clock(clock, display_format_24, pause_offset):

    clear()

    
    if display_format_24:
        clock_font = pyfiglet.figlet_format(f"{int(clock[0]):02}:{int(clock[1]):02}:{int(clock[2]):02}", font = "lcd")
    else:
        if clock[0] >= 13:
            clock_font = pyfiglet.figlet_format(f"{int(clock[0])-12:02}:{int(clock[1]):02}:{int(clock[2]):02} PM", font = "lcd")
        else:
            clock_font = pyfiglet.figlet_format(f"{int(clock[0]):02}:{int(clock[1]):02}:{int(clock[2]):02} AM", font = "lcd")
      
    print(f"\033[1;1H{clock_font}", end="", flush=True)

    start_monotonic = time.monotonic()

    print("Clock is paused")
    input("Press Enter to unpause clock.")

    return pause_offset + (time.monotonic() - start_monotonic)