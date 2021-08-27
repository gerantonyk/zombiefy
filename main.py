from tkinter import *

raiz =Tk()

raiz.title('Zombiefie')

#raiz.resizable(0,0)

raiz.iconbitmap("zombie.ico")

#raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame = Frame()

# miFrame.pack(side="left", anchor="n")

# miFrame.pack(anchor="ne")
# Putting the frame into de the root
miFrame.pack()

# expand when i resize the mail windows
#miFrame.pack(fill="both", expand="1")

# background color
miFrame.config(bg="red")

# width and heigth
miFrame.config(width="650", height="350")
# cursor
miFrame.config(cursor="pirate")
#border size
miFrame.config(bd =35)
# border type
miFrame.config(relief="groove")

raiz.mainloop()
