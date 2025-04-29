import random

# 1)
for i in range(0, 101, 1):
    print(i)

# 2)
digitos = 0
numero = input("Ingrese un numero entero. ")
for i in range(len(numero)):
    digitos+=1
print(f"Tu numero tiene {digitos} digitos.")

# 3)
continuar = "si"
total = 0
while continuar == "si":
    numero=int(input("ingrese un numero. "))
    total += numero
    continuar=input("Desea agregar otro numero?")
    continuar=continuar.lower()
    
print("Los numeros sumados da: ", total)
    
# 4)
total = 0
while True:
    print("Si desea detener, ingrese 0.")
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    total += numero
    print(total)
    
# 5)
numero = random.randint(0,9)
intento = 0
acerto = False
while acerto == False:
    intento+=1
    numUsuario = int(input("Adivina el numero del 0 al 9 "))
    if numUsuario == numero:
        print("Felicidades acertaste!")
        print(f"Te costo {intento} intentos.")
        acerto = True
    else:
        print("Incorrecto, intenta denuveo!")

# 6)
for i in range(100, -1, -2):
    print(i)

# 7)
numUser = int(input("Ingresa un numero entero positivo. "))
resultado = 0
for i in range(0, numUser, 1):
    resultado += i
print(f"La suma de todos los numeros enteros comprendidos desde el cero hasta {numUser} es: {resultado}.")

# 8)
CANTIDAD = 100  
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i+1}: ")) 
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1 
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("Resultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#9)
cantidad=100
suma=0
for i in range(cantidad):
    numero= int(input(f"Ingrese el numero {i+1}:"))
    suma += numero
media = suma/cantidad
print(f"La media de los {cantidad} numeros es: media.")

    
#10)
numero = input("Ingrese un número entero: ")
if numero[0] == "-":
    invertido = "-" + numero[:0:-1]
else:
    invertido = numero[::-1]
print("Número invertido:", invertido)


