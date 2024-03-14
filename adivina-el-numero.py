# Numeros aleatorias en python
# Para generar numeros aleatorios en python, usamos la libreria random

from random import *

# Fucion randint
# Genera un numero aleatorio entre 0 y n, siendo en este caso el segundo valor 30

x = randint(0,30)
print("El numero generado es: " , str(x))

# Funcion uniform
# Genera valores aleatorios iniciales 

x = uniform(0,30)
print("El numero generado es: " , str(x))

# Funcion random
# Genera numeros decimales entre 0 y 1

x = random()
print("El numero generado es: " , str(x))

# Funcion choice 
# Permite elegir un elemento aleatorio a una lista 

nombre = choice (["Fulano 1" ,"Fulano 2", "Fulano 3", "Fulano 4"])
print("Elestudiante escogido es " + nombre)