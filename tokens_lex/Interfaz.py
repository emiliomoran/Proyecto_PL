import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry

root=Tk()
root.geometry("800x600")
def retrieve_input():
    inputValue=text1.get("1.0","end-1c")
    print(inputValue)


btnSint=Button(root, height=2, width=14, text="Analisis sintactico", bg="green",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnSint.pack(side=TOP, pady=2 )

btnLex=Button(root, height=2, width=14, text="Analisis lexico",bg="green",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnLex.pack(side=TOP, pady=2 )

btnPlagio=Button(root, height=2, width=14, text="Plagio",bg="green",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
btnPlagio.pack(side=TOP, pady=2)


text1=Text(root, height=30, width=40)
text1.pack(padx=10, side=LEFT )

text2=Text(root, height=30, width=40)
text2.pack(padx=0, side=LEFT)

resul=Text(root, height=20, width=20)
resul.pack(padx=10, side=LEFT )


mainloop()


