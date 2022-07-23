import random

listaminusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listamayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
listanumeros = ["0","1","2","3","4","5","6","7","8","9"]
listaespeciales = ["+","-","%","$","&","#"]
password=""
lista=[]

print("Programa generador de contraseñas\n")
try:
    longitud=int(input("Ingrese longitud de la contraseña: "))
except ValueError:
    longitud=16

# No es necesario usar la funcion 'str' dado que por defecto el tipo de dato devuelto por 'input()' es un string
minusculas=str(input("Incluir minusculas (s/n): "))
mayusculas=str(input("Incluir mayusculas (s/n): "))
especiales=str(input("Incluir especiales (s/n): "))
numeros=str(input("Incluir numeros (s/n): "))

if minusculas == "s" or minusculas == "S":
    lista = lista + listaminusculas
if mayusculas == "s" or mayusculas == "S":
    lista = lista + listamayusculas
if numeros == "s" or numeros == "S":
    lista = lista + listanumeros
if especiales == "s" or especiales == "S":
    lista = lista + listaespeciales

# Falta tener una lista por defecto en caso de que el usuario no elija nungun criterio
for i in range (1,longitud,1):
    password +=(random.choice(lista))
print(f"Contraseña: {password}")
