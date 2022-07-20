
from os import path

# Funcion que escribe una frase dada como parametro en el archivo dado como parametro
def escribe_archivo(frase_nueva,archivo_frases):
    if path.exists(archivo_frases):
        f = open (archivo_frases,'a')
    else:
        f = open (archivo_frases,'w')
    f.write(frase_nueva +"\n")
    f.close

# Lee el archivo para contar cantidad de frases y palabras que contiene
def lee_archivo(archivo_frases):
    cant_palabras=0
    cant_frases=0
           
    f=open (archivo_frases,'r')
    
    for x in f.readlines():
      cant_palabras += len(x.split())
      cant_frases += 1
    
    print(f"El archivo {archivo_frases} posee {cant_frases} frases")
    print(f"Cantidad de palabras: {cant_palabras}")
      
      
print("Programa contador de frases y palabras")
print("Ingrese \"the end\" para salir\n")
frase=str(input("Ingrese frase: "))

# Se ingresan frases mientras no se ingrese "the end"
while frase != "the end":
    escribe_archivo(frase,"phrases.txt")
    frase=str(input("Ingrese frase: "))

lee_archivo("phrases.txt")
