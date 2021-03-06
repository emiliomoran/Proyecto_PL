from lexico import *

def change(tupla,lista): #funcion recursiva que transforma la tupla ingresada en lista, guardando los datos transformados en la lista que se le envia
    a=list(tupla)
    for i in a:
        if type(i)==type(tupla):
            change(i,lista)
        else:
            lista.append(i)

def promedio(tupla1,tupla2): #funcion que recibe los arboles(tuplas) de los programas, llama a change() y va comparando elemento por elemento
                             #entre las dos listas y el el porcentaje de plagio es de las coincidencias que encuentra dividido con el total de tokens de la lista 1
        lista1=[]
        lista2=[]
        lista1_t=[]
        lista2_t=[]
        coincidencias=0
        change(tupla1,lista1)
        change(tupla2,lista2)
        for e in lista1:
            lista1_t.append(get_tokens(str(e)))
        for e in lista2:
            lista2_t.append(get_tokens(str(e)))
        if len(lista1)<len(lista2):
            max=len(lista1)
        elif len(lista1)>len(lista2):
            max=len(lista2)
        else:
            max=len(lista1)
        for i in range(max):
            if lista1_t[i]==lista2_t[i]:
                coincidencias+=1
        if len(lista1)==0:
            return "El programa 1 posee errores lexicos"
        return "Porcentaje de posible plagio:"+str(round((coincidencias/len(lista1))*100,2))+"%"