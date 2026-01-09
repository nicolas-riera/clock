# Librairies

import os

# Functions

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")