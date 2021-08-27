# data_files/data.txt
#hello
#world

# myScript.py
from tkinter import *
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def print_file(file_path):
    file_path = resource_path(file_path)
    #with open(file_path) as fp:
    #    for line in fp:
    #        return line

if __name__ == '__main__':
    # resource_path('zombie.ico')
    # resource_path('zombie.gif')
    miframe=Tk()
    miimagen=PhotoImage(file=resource_path('zombie.gif'))

    Label(miframe,image= miimagen).place(x=50,y=100)
    miframe.mainloop()
