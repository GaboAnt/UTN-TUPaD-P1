#1)
mult4=[]
for i in range(1,101,1):
    if i % 4 == 0:
        mult4.append(i)
print(mult4)

#2)
meGustan= ["Basket","Gimnasio","Milanesas","Amigos","Series"]
print(meGustan[(len(meGustan)-2)])

#3)
listaVacia=[]
for i in range(1,4,1):
    listaVacia.append(input("Ingresa una palabra"))
print(listaVacia)    

#4)
animales = ["perro", "gato", "conejo", "pez"] 
for i in range(1,(len(animales)+1),1):
    if i==2:
        animales[i-1]="loro"
    elif i==len(animales):
        animales[i-1]="oso"
print(animales)

#5) analizar el siguiente programa
numeros = [8,15,3,22,7] #se crea una lista de 5 elementos
numeros.remove(max(numeros)) #se remueve el elemento de mayor valor dentro de la lista
print(numeros) #se imprime la lista final quedando 4 elementos

#6)
diezAlTreinta = []
for i in range(10,31,5):
    diezAlTreinta.append(i)
print(diezAlTreinta[0:2])

#7)
autos = ["sedan", "polo", "suran", "gol"] 
for i in range(1,(len(autos)+1),1):
    if i == 1 or i == 2:
        autos[i]=input("Nuevo valor ")
print(autos)

#8)
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]] 
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].pop(0)
print(compras)


#10)
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)

