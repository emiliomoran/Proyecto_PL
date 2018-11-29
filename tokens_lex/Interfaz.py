import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry
from sintactico import *
from funciones_extra import *
from lexico import *
from sintactico import errors_list as e_l
import time
root=Tk()
root.geometry("1200x750")
var = StringVar()
label1=Label(root,textvariable=var, relief=RAISED )
var.set("PROGRAMA 1")
label1.place(x=60,y=40,height=30,width=400)
text1=Text(root)
text1.pack(padx=10, side=LEFT )
text1.place(x=60,y=80, height=300, width=400)
var2 = StringVar()
label2=Label(root,textvariable=var2, relief=RAISED )
var2.set("PROGRAMA 2")
label2.place(x=60,y=400,height=30,width=400)
text2=Text(root)
text2.pack(padx=0, side=LEFT)
text2.place(x=60,y=440, height=300, width=400)
var3 = StringVar()
label3=Label(root,textvariable=var3, relief=RAISED )
var3.set("ANALISIS")
label3.place(x=700,y=40,height=30,width=400)
resul=Text(root,state='disabled')
resul.pack(padx=10, side=LEFT)
resul.place(x=700,y=80, height=660, width=400)

def retrieve_input_plagio():
    inputValue1=text1.get("1.0","end-1c")
    inputValue2=text2.get("1.0","end-1c")
    cadena1 = inputValue1.strip()
    cadena2 = inputValue2.strip()
    tupla1=ejecutar_yacc(cadena1)
    tupla2=ejecutar_yacc(cadena2)
    resultado=promedio(tupla1,tupla2)
    resul.config(state="normal")
    contenido='\n' + '*' * 40 + '\n'+resultado.center(40, " ") +'\n' + '*' * 40 + '\n'
    archivo = open("reportes/AnalisisDePlagio_"+time.strftime("%d_%m_%y")+"-"+time.strftime("%H_%M_%S")+".txt", "w")
    archivo.write(contenido)
    archivo.close()
    resul.insert('end', contenido)
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
    inicio='\n' + '*' * 40 + '\n'+"ANALISIS LEXICO".center(40, " ") +'\n' + '*' * 40 + '\n'
    archivo = open("reportes/AnalisisLexico_" + time.strftime("%d_%m_%y") + "-" + time.strftime("%H_%M_%S") + ".txt","w")
    resul.insert('end', inicio)
    archivo.write(inicio)
    resul.insert('end', "programa 1:\n")
    archivo.write("programa 1:\n")
    for i in lista1:
        resul.insert('end', i+"\n")
        archivo.write(i+"\n")
    resul.insert('end', "programa 2:\n")
    archivo.write("programa 2:\n")
    for i in lista2:
        resul.insert('end', i+"\n")
        archivo.write(i+"\n")
    archivo.close()
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
    inicio='\n' + '*' * 40 + '\n'+"ANALISIS SINTACTICO".center(40, " ") +'\n' + '*' * 40 + '\n'
    archivo = open("reportes/AnalisisSintactico_" + time.strftime("%d_%m_%y") + "-" + time.strftime("%H_%M_%S") + ".txt","w")
    resul.insert('end', inicio)
    archivo.write(inicio)
    resul.insert('end', "programa 1:\n")
    archivo.write("programa 1:\n")
    resul.insert('end', str(tupla1) + "\n")
    archivo.write(str(tupla1) + "\n")
    if len1>0:
        resul.insert('end', "Errores en el programa 1:\n")
        archivo.write("Errores en el programa 1:\n")
        for i in range(len1):
            resul.insert('end', e_l[i] + "\n")
            archivo.write(e_l[i] + "\n")
    resul.insert('end', "programa 2:\n")
    archivo.write("programa 2:\n")
    resul.insert('end', str(tupla2) + "\n")
    archivo.write(str(tupla2) + "\n")
    if (len2-len1)>0:
        resul.insert('end', "Errores en el programa 2:\n")
        archivo.write("Errores en el programa 2:\n")
        for i in range(len2-len1):
            resul.insert('end', e_l[i+len1] + "\n")
            archivo.write(e_l[i+len1] + "\n")
    resul.configure(state='disabled')
    archivo.close()
    e_l.clear()
btnSint=Button(root, text="Analisis sintactico", bg="green",
                    command=lambda: retrieve_input_sintactico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnSint.pack(side=TOP, pady=100 )
btnSint.place(x=525,y=100, height=50, width=100)


btnLex=Button(root, text="Analisis lexico",bg="green",
                    command=lambda: retrieve_input_lexico())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnLex.pack(side=TOP, pady=50 )
btnLex.place(x=525,y=300, height=50, width=100)

btnPlagio=Button(root, text="Plagio",bg="green",
                    command=lambda: retrieve_input_plagio())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnPlagio.pack(side=TOP, pady=100)
btnPlagio.place(x=525,y=500, height=50, width=100)


mainloop()