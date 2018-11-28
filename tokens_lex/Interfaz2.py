import tkinter.messagebox
from tkinter import *

from tkinter.filedialog import askopenfilename
from tkinter.ttk import Frame, Label, Entry

root=Tk()
root.geometry("1200x800")


text1=Text(root)
text1.pack(padx=10, side=LEFT )
text1.place(x=60,y=40, height=300, width=400)
text2=Text(root)
text2.pack(padx=0, side=LEFT)
text2.place(x=60,y=350, height=300, width=400)
resul=Text(root,state='disabled')
resul.pack(padx=10, side=LEFT)
resul.place(x=700,y=40, height=610, width=400)

def retrieve_input_lexico():
    inputValue1 = text1.get("1.0", "end-1c")
    inputValue2 = text2.get("1.0", "end-1c")
    print(inputValue1)
    print(inputValue2)
    lista1 = inputValue1.split('\n')
    for i in range(len(lista1)):
        if '\t' in lista1[i]:
            lista1[i] = lista1[i][1:]

    lista2 = inputValue2.split('\n')
    for i in range(len(lista2)):
        if '\t' in lista2[i]:
            lista2[i] = lista2[i][1:]

    resul.config(state="normal")
    resul.insert('end', '\n'+'*'*50+'\n')
    resul.insert('end', 'Codigo programa 1: \n')
    resul.insert('end', lista1)
    resul.insert('end', '\nCodigo programa 2: \n')
    resul.insert('end', lista2)
    resul.configure(state='disabled')

btnSint=Button(root, height=2, width=14, text="Analisis sintactico", bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnSint.pack(side=TOP, pady=100 )


btnLex=Button(root, height=2, width=14, text="Analisis lexico",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnLex.pack(side=TOP, pady=50 )

btnPlagio=Button(root, height=2, width=14, text="Plagio",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnPlagio.pack(side=TOP, pady=100)



mainloop()


