import math
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado
nombre = input("Ingrese su nombre. ")
print("Hola ",nombre,"!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
Nombre = input("Ingrese su nombre. ")
Apellido = input("Ingrese su apellido. ")
Edad = int(input("Ingrese su edad. "))
Residencia = input("Ingrese su pais de residencia. ")

print("Soy ", Nombre, " ", Apellido, ", tengo ", Edad, " años y vivo en ", Residencia)

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
Radio = int(input("Ingrese el radio del circulo. "))
Area = math.pi*Radio**2
Perimetro = 2*math.pi*Radio

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
CantSegundos = int(input("Ingrese una cantidad de segundos. "))
Horas = (CantSegundos/60)/60
print(CantSegundos, " equivale a ", Horas, " Horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
Num = int(input("Ingrese un numero. "))
Tabla = 0
vuelta = 1
for i in range(0,10,1):
    Tabla = Num*vuelta
    vuelta+=1
    print(Tabla)
    
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1, num2 = int(input("Ingrese un numero entero distinto a 0. ")), int(input("Ingrese un segundo numero entero distinto a 0. "))

if num1==0 or num2==0:
    print("Ingrese un numero distinto a 0.")
else:
    Suma = num1 + num2
    Resta = num1 - num2
    Multiplicacion = num1 * num2
    Division = num1 / num2

print("Su suma es: ", Suma)
print("Su resta es: ", Resta)
print("Su multiplicacion es: ", Multiplicacion)
print("Su division es: ", Division)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
Altura, Peso = float(input("Ingrese su altura en metros porfavor. ")), float(input("Ingrese su peso corporal en kilos porfavor."))
IMC = Peso/(Altura**2)
print("Su indice de masa corporal es de: " , IMC)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit
GradosC = float(input("Ingrese la temperatura en grados celsius. "))
TempF = ((9/5) * GradosC) + 32
print("La temperatura ingresada equivale a ", TempF, " grados Farenheit.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1, num2, num3 = float(input("Ingrese el primer numero")), float(input("Ingrese el segundo numero")), float(input("Ingrese el tercer numero"))
Resultado = (num1 + num2 + num3)/3
print("El promedio de los numeros ingresados es: ", Resultado)













