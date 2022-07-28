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

minusculas=(input("Incluir minusculas (s/n): "))
mayusculas=(input("Incluir mayusculas (s/n): "))
especiales=(input("Incluir especiales (s/n): "))
numeros=(input("Incluir numeros (s/n): "))

if minusculas == "s" or minusculas == "S":
    lista = lista + listaminusculas
if mayusculas == "s" or mayusculas == "S":
    lista = lista + listamayusculas
if numeros == "s" or numeros == "S":
    lista = lista + listanumeros
if especiales == "s" or especiales == "S":
    lista = lista + listaespeciales
if (minusculas != "s" or minusculas !="S") and (mayusculas != "s" or mayusculas !="S") and (especiales != "s" or especiales !="S") and (numeros != "s" or numeros !="S"):
    lista = listaminusculas + listamayusculas + listanumeros
    
for i in range (1,longitud,1):
    password +=(random.choice(lista))
print(f"Contraseña: {password}")
