from tkinter import *

root=Tk()

miframe= Frame(root, width=1200, height= 600)
miframe.pack()

minombre=StringVar()


cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=0,column=1,padx=10, pady=10)

cuadropass=Entry(miframe)
cuadropass.grid(row=1,column=1,padx=10, pady=10)
cuadropass.config(show="0")

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2,column=1,padx=10, pady=10)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=3,column=1,padx=10, pady=10)

textocomentario=Text(miframe,width=15, height= 10)
textocomentario.grid(row=4,column=1,padx=10, pady=10)


scrollvert=Scrollbar(miframe, command=textocomentario.yview)
scrollvert.grid(row=4,column=2, sticky= "nsew")
textocomentario.config(yscrollcommand =scrollvert.set)
#----------------------------------------------

nombrelabel=Label(miframe,text="Nombre")
nombrelabel.grid(row=0,column=0,sticky='e',padx=10, pady=10)

passlabel=Label(miframe,text="password")
passlabel.grid(row=1,column=0,sticky='e',padx=10, pady=10)

apellidlabel=Label(miframe,text="Apellido")
apellidlabel.grid(row=2,column=0,sticky='e',padx=10, pady=10)

direccionlabel=Label(miframe,text="Direccion")
direccionlabel.grid(row=3,column=0,sticky='e',padx=10, pady=10)

comentarioslabel=Label(miframe,text="Direccion")
comentarioslabel.grid(row=4,column=0,sticky='e',padx=10, pady=10)

def codigoboton1():
    minombre.set('german')

boton1 =Button(root, text = 'enviar', command=codigoboton1)
boton1.pack()
root.mainloop()
