import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry
from sintactico import *

root=Tk()
root.geometry("800x600")
def retrieve_input_lexico():
    inputValue1=text1.get("1.0","end-1c")
    inputValue2=text2.get("1.0","end-1c")
    print(inputValue1)
    print(inputValue2)
    lista1 = inputValue1.split('\n')
    lista2 = inputValue2.split('\n')

    #print(lista1)
    for i in range(len(lista1)):
    	if(lista1[i].startswith('while') or lista1[i].startswith('if') or lista1[i].startswith('for')):
    		index_padre = i
    	if '\t' in lista1[i]:
    		lista1[index_padre] = lista1[index_padre] +" "+lista1[i][1:]

    lista1_final = []
    for element in lista1:
    	if not '\t' in element:
    		lista1_final.append(element)
    
    print('Codigo programa 1: ',lista1_final)
    for element in lista1_final:
    	ejecutar_yacc(element)


    for i in range(len(lista2)):
    	if(lista2[i].startswith('while') or lista2[i].startswith('if') or lista2[i].startswith('for')):
    		index_padre = i
    	if '\t' in lista2[i]:
    		lista2[index_padre] = lista2[index_padre] +" "+lista2[i][1:]

    lista2_final = []
    for element in lista2:
    	if not '\t' in element:
    		lista2_final.append(element)
    
    print('Codigo programa 2: ',lista2_final)
    for element in lista2_final:
    	ejecutar_yacc(element)

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