import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Entry



class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Validator Project")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global expr
        expr = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="BIENVENIDO", width=18)
        lbl1.pack(side=TOP, padx=5, pady=5)



        frame3 = Frame(self)
        frame3.pack(fill=Y)

        btnSint = Button(frame3, text="Analisis Sintatico", width=15, command=self.validar, bg = "green")
        btnSint.pack(side=TOP, anchor=N, padx=8, pady=5)
        btnLex = Button(frame3, text="Analisis Lexico", width=15, command=self.validar, bg="green")
        btnLex.pack(side=TOP, anchor=N, padx=8, pady=5)
        btnPlagio = Button(frame3, text="Calcular plagio", width=15, command=self.validar, bg="green")
        btnPlagio.pack(side=TOP, anchor=N, padx=8, pady=5)

        programa1 = Text(frame3, width=40, height=30)
        programa1.pack(side=LEFT, anchor=N, padx=8, pady=5)
        programa2 = Text(frame3, width=40, height=30)
        programa2.pack(side=LEFT, anchor=N, padx=8, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=Y)

        lbl2 = Label(frame2, text="Porcentaje de plagio es: ", width=18)
        lbl2.pack(side=LEFT, anchor=N, padx=8, pady=5)
        plagio = Label(frame2, text="----", width=18)
        plagio.pack(side=LEFT, anchor=N, padx=8, pady=5)



    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error','Ingrese expresion')

    def validar(self):
        if expr.get() == '':
            self.errorMsg('error')

def main():
    root = Tk()
    root.geometry("700x700")
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()