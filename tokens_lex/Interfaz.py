import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry

root=Tk()
root.geometry("800x600")
def retrieve_input_lexico():
    inputValue1=text1.get("1.0","end-1c")
    inputValue2=text2.get("1.0","end-1c")
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
    
    print('Codigo programa 1: ',lista1)
    print('Codigo programa 2: ',lista2)   

btnSint=Button(root, height=2, width=14, text="Analisis sintactico", bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnSint.pack(side=TOP, pady=2 )

btnLex=Button(root, height=2, width=14, text="Analisis lexico",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnLex.pack(side=TOP, pady=2 )

btnPlagio=Button(root, height=2, width=14, text="Plagio",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnPlagio.pack(side=TOP, pady=2)


text1=Text(root, height=30, width=40)
text1.pack(padx=10, side=LEFT )

text2=Text(root, height=30, width=40)
text2.pack(padx=0, side=LEFT)

resul=Text(root, height=20, width=20)
resul.pack(padx=10, side=LEFT )


mainloop()


