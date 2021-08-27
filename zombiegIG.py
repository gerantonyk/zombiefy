# Version final
#para regenerar
#pyinstaller --windowed --onefile --add-data "E:\aprendiendo pyton\nuevo proyecto\graphics\zombie.ic
from tkinter import *
from tkinter import ttk
import sys
import os
import time

# para usar archivos guardados en el exe
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Ventana
class Root(Tk):

    def __init__(self):
        super(Root,self).__init__()
        self.title("Zombify")
        self.minsize(564,260)
        self.iconbitmap(resource_path('zombie.ico'))
        self.resizable(width=False, height=False)

# Entrys numericos
class ParametroNumerico(Entry):

    def __init__(self,parent):
        super().__init__(parent)
        reg =root.register(correctn)
        #selfEntry(root)
        self.config(width = 2, validate='key',validatecommand=(reg,'%P'))
        self.Entryval = StringVar()
        self.config(textvariable = self.Entryval)

# conversion de monstruo
def convert():
    stro   = int(strEntry.Entryval.get())
    dexo   = int(dexEntry.Entryval.get())
    chan   = 10
    hdo    = int(hdEntry.Entryval.get())
    nombre = nombreEntryval.get()
    hdn=1
    indice= size.index(sizeComboval.get())
    #print(indice)
    if undeadComboval.get() =="Skeleton" or undeadComboval.get() =="Bloody Skeleton" :
        #print("esqueleto")
        #hd
        hdn = hdo
        bonifdh =''
        ACn     = sac[indice]
        Attack = sclaw[indice]
        # STR
        strn = stro
        # DEX
        dexn = dexo +2
        # AC
        acn = 10 + (dexn-10)//2 + sac[indice]
        # attack
        attack =  f'Claw {sclaw[indice]}+{(strn-10)//2}'
        # INI
        inin = (dexn-10)//2+4
        # DAMAGE REDUCTION
        damred = '5/bludgeoning'
        if undeadComboval.get() =="Bloody Skeleton":
            chan   = chan + 4
            damred = f'''5/bludgeoning
        Deathless (Su)
        Fasthealing {hdn//2}'''
        hpextra = hdn*((chan-10)//2)+(hdn*desecrate.get())


    elif undeadComboval.get()=="Zombie" or undeadComboval.get()=="Fast Zombie":
        # print("zombie")
        # HD
        hdn = hdo + zhd[indice]
        hpextra = 3 +(hdn*desecrate.get())
        if hdn > 3:
            hpextra = hdn +(hdn*desecrate.get())
        # STR
        strn = stro +2
        # DEX
        dexn = dexo -2
        # DAMAGE REDUCTION
        damred = '''5/slashing
        Staggered (Ex)'''
        if undeadComboval.get()=="Fast Zombie":
                dexn = dexo +2
                damred = 'Quick Strikes (Ex)'
        # AC
        acn = 10 + (dexn-10)//2  + zac[indice]
        # attack
        attack =  f'Slam {zslam[indice]}+{str((strn-10)//2) }'
        # INI
        inin = (dexn-10)//2

    #hpextra
    bonifdh = ''
    if hpextra !=0:
        bonifdh = f'+{hpextra}'
    # BAB
    babn = hdn*3//4
    # CHA
    #chan = 10
    # FORT
    forn = (hdn*1)//3 + (chan-10)//2
    # REFL
    refn = (hdn*1)//3 + (dexn-10)//2
    # WILL
    wiln = (hdn*1)//2+2

    resultado = f'''Nombre: {undeadComboval.get()} {nombre}
Size:   {sizeComboval.get()}
HD:     {hdn}d8 {bonifdh}
BAB     {babn}
STR:    {strn}
DEX:    {dexn}
CHA:    {chan}
AC:     {acn}
FORT:   {forn}
REFL:   {refn}
WILL:   {wiln}
INIT:   {inin}
Attack: {attack}
Sp:     {damred}
'''

    textocomentario=Text(root,width=50, height= 16)
    textocomentario.grid(row=0,column=2,rowspan= 9999)
    # print(resultado)
    textocomentario.insert(INSERT,resultado)
    textocomentario.config(state = 'disabled')

# Para que el botton se hunda cuando presionas enter
def invoke_button(event):
    convertbutton.config(relief = "sunken")
    root.update_idletasks()
    time.sleep(0.1)
    convertbutton.invoke()
    convertbutton.config(relief = "raised")

# def convert1(event):
#     convert()


# Función para validar texto
def correctc(inp):
    if all(x.isalpha() or x.isspace() for x in inp) and len(inp)<30:
        return True
    else:
        return False


# Función para validar numeros
def correctn(inp):
    if inp.isdigit() and  0<int(inp)< 36:
        return True
    elif inp =='':
        return True
    else:
        return False

# if __name__=='__main__':
root = Root()

# inicializacion de variables
nombreEntryval = StringVar()
sizeComboval   = StringVar()
undeadComboval = StringVar()
desecrate = IntVar()
size  = ("Tinny","Small","Medium","Large","Huge","Gargantuan","Colossal")
zhd   = (0,1,1,2,4,6,10)
zac   = (0,1,2,3,4,7,11)
sac   = (0,1,2,2,3,6,10)
zslam = ('1d3','1d4','1d6','1d8','2d6','2d8','2d10')
sclaw = ('1d2','1d3','1d4','1d6','1d8','2d6','2d8')

undead= ("Skeleton","Zombie","Bloody Skeleton", "Fast Zombie")

# fin inicializacion de variables

# Graficos
nombreEntry = Entry(root)
reg =root.register(correctc)
nombreEntry.config(width = 15, validate=('key') ,validatecommand=(reg,'%P'))
nombreEntry.grid(column = 1, row =0, sticky =W, padx=2)
nombreEntry.config(textvariable = nombreEntryval)
nombreEntry.insert(END, 'Criatura')
nombrelabel=Label(root)
nombrelabel.config(text = 'Criatura:')
nombrelabel.grid(column = 0, row =0, sticky =W)


#-----------------------
# sv = StringVar() ya esta arriba

# def callback():
#     print(nombreEntryval.get())
#     return True

#nombreEntry.config(validate="focusout", validatecommand=callback)










#-----------------------
hdEntry=ParametroNumerico(root)
hdEntry.grid(column = 1, row =1, sticky =W, padx=2)
hdEntry.insert(0, '2')
hdlabel=Label(root)
hdlabel.config(text = 'HD:')
hdlabel.grid(column = 0, row =1, sticky =W)

strEntry=ParametroNumerico(root)
strEntry.grid(column = 1, row =2, sticky =W, padx=2)
strEntry.insert(0, '10')
strlabel=Label(root)
strlabel.config(text = 'Str:')
strlabel.grid(column = 0, row =2, sticky =W)

dexEntry=ParametroNumerico(root)
dexEntry.grid(column = 1, row =3, sticky =W, padx=2)
dexEntry.insert(0, '10')
dexlabel=Label(root)
dexlabel.config(text = 'Dex:')
dexlabel.grid(column = 0, row =3, sticky =W)

sizeCombo = ttk.Combobox(root,state="readonly",width = 10)
sizeCombo['values'] = size
sizeCombo.grid(column = 1, row = 4, sticky =W, padx=2)
sizeCombo.config(textvariable = sizeComboval)
sizeCombo.current(2)
sizelabel=Label(root)
sizelabel.config(text = 'Size:')
sizelabel.grid(column = 0, row =4, sticky =W)

undeadCombo = ttk.Combobox(root,state="readonly",width = 10)
undeadCombo['values'] = undead
undeadCombo.grid(column = 1, row = 5, sticky =W, padx=2)
undeadCombo.config(textvariable = undeadComboval)
undeadCombo.current(1)
undeadlabel=Label(root)
undeadlabel.config(text = 'Undead:')
undeadlabel.grid(column = 0, row =5, sticky =W)

desecratecheck = ttk.Checkbutton(root, text="Desecrate", variable=desecrate, onvalue=1, offvalue=0)
desecratecheck.grid(column = 0, row =6, sticky =W)

convertbutton = Button(root, text ="Convert", command = convert)
convertbutton.grid(column = 0, row =7, columnspan= 2,pady=20)
#root.bind("<Return>", convert1)
root.bind("<Return>", invoke_button)
# fin Graficos

# somewhere the button is defined to do something when clicked
#button_save = Button(text="Save", command = self.doSomething)





# somewhere else






root.mainloop()
