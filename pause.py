# Librairies

from clear import clear
import time

# Functions

def pause_clock(clock, display_format_24, pause_offset):

    clear()

    if display_format_24:
        print(f"\033[1;1H{int(clock[0]):02}:{int(clock[1]):02}:{int(clock[2]):02}", end="", flush=True)
    else:
        if clock[0] >= 13:
            print(f"\033[1;1H{int(clock[0])-12:02}:{int(clock[1]):02}:{int(clock[2]):02} PM", end="", flush=True)
        else:
            print(f"\033[1;1H{int(clock[0]):02}:{int(clock[1]):02}:{int(clock[2]):02} AM", end="", flush=True)

    start_monotonic = time.monotonic()

    print("\n\nClock is paused")
    input("Press Enter to unpause clock.")

    return pause_offset + (time.monotonic() - start_monotonic)