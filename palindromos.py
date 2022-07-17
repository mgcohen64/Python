cant_palabras=0
son_palindromos=0
noson_palindromos=0
testigo=False

def soniguales(letra1,letra2):
   return letra1 == letra2 

print("Programa Verificador de palabras palíndromas.\nIngrese \"adios\" para salir\n")
palabra=str(input("Ingrese palabra : "))

while palabra != "adios":
    cant_palabras += 1
    longitud=len(palabra)
    for i in range (0,longitud//2,1):
      if soniguales(palabra[i],palabra[longitud-i-1]) == False:
        noson_palindromos += 1
        testigo=True
        break
    if testigo == False:
        son_palindromos += 1
    else:
        testigo=False  
    palabra=str(input("Ingrese palabra : "))
    
print(f"\nCantidad de palabras ingresadas: {cant_palabras}")
print(f"Cantidad de palabras palíndromas: {son_palindromos}")
print(f"Cantidad de palabras no palíndromas: {noson_palindromos}")