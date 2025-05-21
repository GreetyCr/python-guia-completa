#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PYTHON BASICS - REPASO COMPLETO
===============================
Este archivo contiene un repaso de los conceptos fundamentales de Python.
"""

# ======================================================================
# 1. VARIABLES Y TIPOS DE DATOS
# ======================================================================

# Enteros (int)
entero = 42
print(f"Entero: {entero}, tipo: {type(entero)}")

# Flotantes (float)
flotante = 3.14159
print(f"Flotante: {flotante}, tipo: {type(flotante)}")

# Cadenas de texto (str)
texto = "Hola Mundo"
print(f"Texto: {texto}, tipo: {type(texto)}")

# Booleanos (bool)
verdadero = True
falso = False
print(f"Boolean: {verdadero}, tipo: {type(verdadero)}")

# Listas (list) - Colección ordenada y mutable
lista = [1, 2, 3, "cuatro", 5.0]
print(f"Lista: {lista}, tipo: {type(lista)}")

# Tuplas (tuple) - Colección ordenada e inmutable
tupla = (1, 2, "tres", 4.0)
print(f"Tupla: {tupla}, tipo: {type(tupla)}")

# Diccionarios (dict) - Colección no ordenada de pares clave-valor
diccionario = {"nombre": "Python", "año": 1991, "creador": "Guido van Rossum"}
print(f"Diccionario: {diccionario}, tipo: {type(diccionario)}")

# Conjuntos (set) - Colección no ordenada de elementos únicos
conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto: {conjunto}, tipo: {type(conjunto)}")

# None - Valor nulo
nulo = None
print(f"None: {nulo}, tipo: {type(nulo)}")

# ======================================================================
# 2. OPERADORES
# ======================================================================

# Operadores aritméticos
a, b = 10, 3
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo (resto): {a % b}")
print(f"Potencia: {a ** b}")

# Operadores de comparación
print(f"Igual a (==): {a == b}")
print(f"No igual a (!=): {a != b}")
print(f"Mayor que: {a > b}")
print(f"Menor que: {a < b}")
print(f"Mayor o igual que: {a >= b}")
print(f"Menor o igual que: {a <= b}")

# Operadores lógicos
x, y = True, False
print(f"AND lógico: {x and y}")
print(f"OR lógico: {x or y}")
print(f"NOT lógico (x): {not x}")

# Operadores de asignación
c = 5
c += 2  # Equivalente a c = c + 2
print(f"+=: {c}")
c -= 1  # Equivalente a c = c - 1
print(f"-=: {c}")
c *= 2  # Equivalente a c = c * 2
print(f"*=: {c}")
c /= 2  # Equivalente a c = c / 2
print(f"/=: {c}")

# Operadores de identidad
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")  # False, diferentes objetos
print(f"list1 is list3: {list1 is list3}")  # True, mismo objeto
print(f"list1 is not list2: {list1 is not list2}")  # True

# ======================================================================
# 3. ESTRUCTURAS DE CONTROL
# ======================================================================

# Condicionales (if-elif-else)
edad = 18
if edad < 18:
    print("Menor de edad")
elif edad == 18:
    print("Justo 18 años")
else:
    print("Mayor de edad")

# Bucle for (iteración)
print("Iterando lista con for:")
for elemento in [1, 2, 3, 4, 5]:
    print(f"  Elemento: {elemento}")

# Bucle for con range
print("For con range:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"  i: {i}")

# Bucle while
print("Bucle while:")
contador = 0
while contador < 5:
    print(f"  Contador: {contador}")
    contador += 1

# Break y continue
print("Break y continue:")
for i in range(10):
    if i == 3:
        continue  # Salta a la siguiente iteración
    if i == 7:
        break  # Sale del bucle
    print(f"  Valor de i: {i}")

# Comprensión de listas
cuadrados = [x**2 for x in range(1, 6)]
print(f"Comprensión de listas (cuadrados): {cuadrados}")

pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares con comprensión: {pares}")

# ======================================================================
# 4. FUNCIONES
# ======================================================================

# Definición básica de función
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"¡Hola, {nombre}!"

print(saludar("Python"))

# Parámetros por defecto
def saludar_con_default(nombre="Mundo"):
    return f"¡Hola, {nombre}!"

print(saludar_con_default())
print(saludar_con_default("Usuario"))

# Argumentos posicionales y con nombre
def describir_persona(nombre, edad, ciudad):
    return f"{nombre} tiene {edad} años y vive en {ciudad}."

print(describir_persona("Ana", 25, "Madrid"))
print(describir_persona(edad=30, ciudad="Barcelona", nombre="Carlos"))

# Número variable de argumentos (*args, **kwargs)
def suma_varios(*numeros):
    """Suma varios números."""
    return sum(numeros)

print(f"Suma de varios números: {suma_varios(1, 2, 3, 4, 5)}")

def info_persona(nombre, **datos):
    """Muestra información de una persona."""
    info = f"Información de {nombre}:"
    for clave, valor in datos.items():
        info += f"\n- {clave}: {valor}"
    return info

print(info_persona("Laura", edad=28, profesion="Ingeniera", ciudad="Valencia"))

# Funciones lambda (anónimas)
cubo = lambda x: x**3
print(f"Cubo de 3 (lambda): {cubo(3)}")

# ======================================================================
# 5. MANEJO DE EXCEPCIONES
# ======================================================================

# Try-except básico
try:
    resultado = 10 / 0
except ZeroDivisionError:
    resultado = "Error: División por cero"
print(f"Resultado tras try-except: {resultado}")

# Try-except-else-finally
try:
    numero = int("10")
except ValueError:
    print("No se pudo convertir a entero")
else:
    print(f"Conversión exitosa: {numero}")
finally:
    print("Este bloque siempre se ejecuta")

# Lanzar excepciones con raise
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    verificar_edad(-5)
except ValueError as e:
    print(f"Error capturado: {e}")

# ======================================================================
# 6. MÓDULOS Y PAQUETES
# ======================================================================

# Importar un módulo completo
import math
print(f"Valor de PI: {math.pi}")
print(f"Seno de 0: {math.sin(0)}")

# Importar elementos específicos
from datetime import datetime, timedelta
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Mañana a esta hora: {ahora + timedelta(days=1)}")

# Importar con alias
import random as rnd
print(f"Número aleatorio: {rnd.randint(1, 100)}")

# ======================================================================
# 7. ENTRADA/SALIDA Y ARCHIVOS
# ======================================================================

# Entrada por consola (comentado para no interrumpir la ejecución)
# nombre = input("Introduce tu nombre: ")
# print(f"Hola, {nombre}")

# Trabajar con archivos (modo básico)
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.\n")
    archivo.write("Segunda línea del archivo.")

# Leer de un archivo
try:
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo:\n{contenido}")
except FileNotFoundError:
    print("El archivo no se encontró")

# ======================================================================
# 8. PROGRAMACIÓN ORIENTADA A OBJETOS
# ======================================================================

# Definición de clase
class Persona:
    """Clase que representa a una persona."""
    
    # Atributo de clase
    especie = "Homo sapiens"
    
    # Constructor
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    # Método de instancia
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    # Método de clase
    @classmethod
    def crear_desde_nacimiento(cls, nombre, año_nacimiento):
        edad = datetime.now().year - año_nacimiento
        return cls(nombre, edad)
    
    # Método estático
    @staticmethod
    def es_adulto(edad):
        return edad >= 18

# Crear instancias
persona1 = Persona("Juan", 30)
print(persona1.saludar())
print(f"¿Es adulto? {Persona.es_adulto(persona1.edad)}")

# Usar método de clase
persona2 = Persona.crear_desde_nacimiento("María", 1995)
print(persona2.saludar())

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    # Sobrescribir método
    def saludar(self):
        return f"{super().saludar()} Estudio {self.carrera}."

estudiante = Estudiante("Pedro", 22, "Informática")
print(estudiante.saludar())

# ======================================================================
# 9. EXTRAS Y CARACTERÍSTICAS AVANZADAS
# ======================================================================

# Generadores
def fibonacci(n):
    """Generador de la secuencia de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Secuencia de Fibonacci:")
for num in fibonacci(10):
    print(f"  {num}", end=" ")
print()  # Nueva línea

# Decoradores
def decorador_simple(funcion):
    def wrapper(*args, **kwargs):
        print("Inicio de la ejecución")
        resultado = funcion(*args, **kwargs)
        print("Fin de la ejecución")
        return resultado
    return wrapper

@decorador_simple
def función_ejemplo():
    print("  Función siendo ejecutada")

función_ejemplo()

# Type hints (indicaciones de tipo)
def suma_con_tipos(a: int, b: int) -> int:
    return a + b

print(f"Suma con tipos: {suma_con_tipos(5, 7)}")

# Contextos (with)
class MiContexto:
    def __enter__(self):
        print("Entrando al contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
    
    def hacer_algo(self):
        print("  Haciendo algo en el contexto")

with MiContexto() as ctx:
    ctx.hacer_algo()

# ======================================================================
# 10. EJEMPLOS DE LIBRERÍAS POPULARES
# ======================================================================

# Ejemplo básico de NumPy (si está instalado)
try:
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array NumPy: {arr}")
    print(f"Media del array: {np.mean(arr)}")
except ImportError:
    print("NumPy no está instalado. Instálalo con: pip install numpy")

# Ejemplo básico de Pandas (si está instalado)
try:
    import pandas as pd
    datos = {'Nombre': ['Ana', 'Juan', 'María'],
             'Edad': [25, 30, 22],
             'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}
    df = pd.DataFrame(datos)
    print("\nDataFrame de Pandas:")
    print(df)
except ImportError:
    print("Pandas no está instalado. Instálalo con: pip install pandas")

print("\n¡Repaso de Python completado!")