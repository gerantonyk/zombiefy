from tkinter import *

root=Tk()

miframe= Frame(root, width=1200, height= 600)
miframe.pack()



cuadronombre=Entry(miframe)
cuadronombre.grid(row=0,column=1,padx=10, pady=10)

cuadropass=Entry(miframe)
cuadropass.grid(row=1,column=1,padx=10, pady=10)
cuadropass.config(show="0")

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2,column=1,padx=10, pady=10)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=3,column=1,padx=10, pady=10)

nombrelabel=Label(miframe,text="Nombre")
nombrelabel.grid(row=0,column=0,sticky='e',padx=10, pady=10)

passlabel=Label(miframe,text="password")
passlabel.grid(row=1,column=0,sticky='e',padx=10, pady=10)

apellidlabel=Label(miframe,text="Apellido")
apellidlabel.grid(row=2,column=0,sticky='e',padx=10, pady=10)

direccionlabel=Label(miframe,text="Direccion de casa")
direccionlabel.grid(row=3,column=0,sticky='e',padx=10, pady=10)

root.mainloop()
