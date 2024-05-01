import os
import datetime
import time

# Variables globales: Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
bright_pink_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"
rose_color = "\033[95m"
pink_color = "\033[38;2;255;192;203m"
bright_pink_color = "\033[38;2;255;105;180m"

# funciones de usuario

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass


def gotxy_frame(x, y, width, height):
    # Mover el cursor a la posición (x, y)
    gotoxy(x, y)
    
    # Imprimir la parte superior del marco
    print(bright_pink_color+"*" * width)
    
    # Imprimir los lados del marco
    for _ in range(height - 2):
        gotoxy(x, y + 1)
        print(bright_pink_color+"*", end="")
        gotoxy(x + width - 1, y + 1)
        print(bright_pink_color+"*", end="")
        y += 1
    
    # Imprimir la parte inferior del marco
    gotoxy(x, y + 1)
    print(bright_pink_color+"*" * width)

def gotxy_profile(x,y):
    gotoxy(x,y)
    print("   *****  ")
    print("  *******  ")
    print("   *****  ")
    print("          ")
    print("  ********  ")
    print(" ********** ")
    print(" ********** ")
