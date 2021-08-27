from tkinter import *
from tkinter import ttk
def var_states():
   print(var1.get())
root=Tk()

miframe= Frame(root,width=650, height=400)

miframe.pack()

milabel= Label(miframe,text="culitos locos")

# con esto me resizea el frame
miCombobox = ttk.Combobox()
miCombobox.place(x=50,y=180)
# con esto puedo poerlo donde quiera
milabel.place(x=100,y=180)
# una forma si voy a usar variable es invocar la clase directamente
#Label(miframe,text='culitoss locos', fg="red", font=('Comic Sans MS', 18)).place(x=102,y=203)
#miimagen=PhotoImage(file="zombie.gif")
    var1=IntVar()
desecratecheck = ttk.Checkbutton(miframe, text="Desecrate",variable= var1, onvalue=1, offvalue=0)
desecratecheck.place(x=50,y=120)
Button(miframe, text='Show', command=var_states).place(x=50,y=90)


#Label(miframe,image= miimagen).place(x=50,y=100)

root.mainloop()
