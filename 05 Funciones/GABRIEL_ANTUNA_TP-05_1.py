import math
#1) 
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#2)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#3) 
def informacion_personal(nombre, apellido, edad, residencia):
    return f"soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}."
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4)
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingrese el radio de un círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

#5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")

# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

# 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} Fahrenheit.")

# 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
n1 = float(input("Ingrese el primer número para el promedio: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")