import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry
from sintactico import *
from funciones_extra import *
from lexico import *
from sintactico import errors_list as e_l
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

def retrieve_input_plagio():
    inputValue1=text1.get("1.0","end-1c")
    inputValue2=text2.get("1.0","end-1c")
    cadena1 = inputValue1.strip()
    cadena2 = inputValue2.strip()
    tupla1=ejecutar_yacc(cadena1)
    tupla2=ejecutar_yacc(cadena2)
    resultado=promedio(tupla1,tupla2)
    resul.config(state="normal")
    resul.insert('end', '\n' + '*' * 40 + '\n'+resultado.center(40, " ") +'\n' + '*' * 40 + '\n')
    resul.configure(state='disabled')

def retrieve_input_lexico():
    resul.delete(1.0,END)
    inputValue1=text1.get("1.0","end-1c")
    inputValue2=text2.get("1.0","end-1c")
    cadena1 = inputValue1.strip()
    cadena2 = inputValue2.strip()
    lista1=mostrar_tokens(cadena1)
    lista2=mostrar_tokens(cadena2)
    resul.config(state="normal")
    resul.insert('end', '\n' + '*' * 40 + '\n'+"ANALISIS LEXICO".center(40, " ") +'\n' + '*' * 40 + '\n')
    resul.insert('end', "programa 1:\n")
    for i in lista1:
        resul.insert('end', i+"\n")
    resul.insert('end', "programa 2:\n")
    for i in lista2:
        resul.insert('end', i+"\n")
    resul.configure(state='disabled')

def retrieve_input_sintactico():
    inputValue1 = text1.get("1.0", "end-1c")
    inputValue2 = text2.get("1.0", "end-1c")
    cadena1 = inputValue1.strip()
    cadena2 = inputValue2.strip()
    tupla1 = ejecutar_yacc(cadena1)
    len1=len(e_l)
    tupla2 = ejecutar_yacc(cadena2)
    len2=len(e_l)
    resul.config(state="normal")
    resul.insert('end', '\n' + '*' * 40 + '\n'+"ANALISIS SINTACTICO".center(40, " ") +'\n' + '*' * 40 + '\n')
    resul.insert('end', "programa 1:\n")
    resul.insert('end', str(tupla1) + "\n")
    if len1>0:
        resul.insert('end', "Errores en el programa 1:\n")
        for i in range(len1):
            resul.insert('end', e_l[i] + "\n")
    resul.insert('end', "programa 2:\n")
    resul.insert('end', str(tupla2) + "\n")
    if (len2-len1)>0:
        resul.insert('end', "Errores en el programa 2:\n")
        for i in range(len2-len1):
            resul.insert('end', e_l[i+len1] + "\n")
    resul.configure(state='disabled')
btnSint=Button(root, height=2, width=14, text="Analisis sintactico", bg="green",
                    command=lambda: retrieve_input_sintactico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnSint.pack(side=TOP, pady=100 )


btnLex=Button(root, height=2, width=14, text="Analisis lexico",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnLex.pack(side=TOP, pady=50 )

btnPlagio=Button(root, height=2, width=14, text="Plagio",bg="green",
                    command=lambda: retrieve_input_plagio())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnPlagio.pack(side=TOP, pady=100)


mainloop()