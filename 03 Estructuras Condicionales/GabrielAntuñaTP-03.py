from statistics import mode, median, mean
import random
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = input("Ingrese su edad porfavor: ")
if edad >= 18:
    print("Es mayor de edad.")
    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = input("Ingrese su nota porfavor: ")
if nota >= 6:
    print("Aprobado.")
elif nota < 6 and nota >= 0:
    print("Desaprobado.")
else:
    print("Nota no valida.")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"
continuar = 1
while continuar == 1:
    numero = input("Ingrese un numero: ")
    if numero%2 == 0:
        print("Ha ingresado un numero par.")
    elif numero%2 != 0:
        print("Porfavor ingrese un numero par.")
    continuar=input("Ingrese 1 si desea continuar, 0 si desea finalizar.")
    
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
edad = input("Ingrese su edad porfavor: ")
if edad < 0:
    print("Ingrese una edad real.")
elif edad > 0 and edad < 12:
    print("Usted es un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un/a adulto/a joven")
else:
    print("Usted es un/a adulto/a")    

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres...
contra =input("Ingrese una contraseña de entre 8 y 14 caracteres. ")
if len(contra)>=8 and len(contra)<=14:
    print("Ha ingresado una contraseña correcta")
elif len(contra)<8 or len(contra)>14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media>mediana and mediana<moda:
    print("Sesgo positivo")
elif media<mediana and mediana<moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")    

#7) Escribir un programa que solicite una frase o palabra al usuario
frase = input("Ingrese una frase: ")
vocal = False
for i in range(len(frase),-1,-1):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        vocal==True
        frase= f"{frase}!"
print(frase)

#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
Nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
numero = input("Ingrese la opcion que desee: ")
if numero==1:
    print(Nombre.upper())
elif numero==2:
    print(Nombre.lower())
elif numero==1:
    print(Nombre.capitalize())
else:
    print("Opcion no valida.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto
Magnitud=input("Ingrese la magnitud de un terremoto: ")
resultado=""
if Magnitud<3:
    print("Muy leve")
elif Magnitud>=3 and Magnitud<4:
    print("Ligeramente perceptible")
elif Magnitud>=4 and Magnitud<5:
    print("Moderado")
elif Magnitud>=5 and Magnitud<6:
    print("Fuerte")
elif Magnitud>=6 and Magnitud<7:
    print("Muy fuerte")
elif Magnitud>=7:
    print("Extremo")

#10)Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
hemisferio = input("Ingrese en que hemisferio se encuentra: ")
hemisferio.lower()
mes = input("Ingrese el mes en el que se encuentra: ")
dia = input("Ingrese el dia en el que se encuentra: ")

if mes<=3:
    if mes==3 and dia<=20:
        if hemisferio=="sur":
            print("Verano")
        elif hemisferio=="norte":
            print("Invierno")
    if mes==2 or mes==1:
        if hemisferio=="sur":
            print("Verano")
        elif hemisferio=="norte":
            print("Invierno")
elif (mes==12 and dia>=21):
    if hemisferio=="sur":
        print("Verano")
    elif hemisferio=="norte":
        print("Invierno")
        
if mes>=3 or mes<=6:
    if mes==6 and dia<=20:
        if hemisferio=="sur":
            print("Otoño")
        elif hemisferio=="norte":
            print("Primavera")
    if mes==4 or mes==5:
        if hemisferio=="sur":
            print("Otoño")
        elif hemisferio=="norte":
            print("Primavera")
elif (mes==3 and dia>=20):
    if hemisferio=="sur":
        print("Otoño")
    elif hemisferio=="norte":
        print("Primavera")
        
if mes>=6 or mes<=9:
    if mes==9 and dia<=20:
        if hemisferio=="sur":
            print("Invierno")
        elif hemisferio=="norte":
            print("Verano")
    if mes==7 or mes==8:
        if hemisferio=="sur":
            print("Invierno")
        elif hemisferio=="norte":
            print("Verano")
elif (mes==6 and dia<=20):
    if hemisferio=="sur":
        print("Invierno")
    elif hemisferio=="norte":
        print("Verano")

if mes>=9 or mes<=12:
     if mes==12 and dia<=20:
         if hemisferio=="sur":
             print("Primavera")
         elif hemisferio=="norte":
             print("Otoño")
     if mes==10 or mes==11:
         if hemisferio=="sur":
             print("Primavera")
         elif hemisferio=="norte":
             print("Otoño")
elif (mes==9 and dia<=20):
    if hemisferio=="sur":
        print("Primavera")
    elif hemisferio=="norte":
        print("Otoño")       




























