def change(tupla,lista):
    a=list(tupla)
    for i in a:
        if type(i)==type(tupla):
            change(i,lista)
        else:
            lista.append(i)

def promedio(tupla1,tupla2):
    try:
        lista1=[]
        lista2=[]
        coincidencias=0
        change(tupla1,lista1)
        change(tupla2,lista2)
        if len(lista1)<len(lista2):
            max=len(lista1)
        elif len(lista1)>len(lista2):
            max=len(lista2)
        else:
            max=len(lista1)
        for i in range(max):
            if lista1[i]==lista2[i]:
                coincidencias+=1
        return "porcentaje de posible plagio:"+str(round((coincidencias/len(lista1))*100,2))+"%"
    except Exception as e:
        print('----------',e)
        return 'se ha generado un error :v '+ e