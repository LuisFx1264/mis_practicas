import datetime
import random
def saludar():
    print("Hola, Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora ctual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es: {resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Raul",19)

#mis ejemplos
def lanzar_moneda():
    opciones = ["Cara", "Cruz"]
    resultado = random.choice(opciones)
    print(f"La moneda cayó en: {resultado}")
lanzar_moneda()

def sumar_numeros(numero1, numero2):
    suma = numero1 + numero2
    return suma

resultado = sumar_numeros(15, 20)
print(f"La suma total es: {resultado}")

def repetir_texto(palabra, veces):
    mensaje = (palabra + " ") * veces
    print(mensaje)

repetir_texto("Regresa Valeria", 10)

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

resultado = es_par_o_impar(7)
print(f"El número 7 es: {resultado}")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura = celsius_a_fahrenheit(25)
print(f"25°C equivalen a: {temperatura}°F")