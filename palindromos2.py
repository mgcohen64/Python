cant_palabras=0
son_palindromos=0
noson_palindromos=0
testigo=False

# Funcion que compara la palabra y su inversa palabra[::-1] (devuelve True o False)
def sonpalindromos(palabra):
   return palabra == palabra[::-1] 

print("Programa Verificador de palabras palíndromas.\nIngrese \"adios\" para salir\n")
palabra=str(input("Ingrese palabra : "))

# Solicita palabras hasta que se ingresa "adios"
while palabra != "adios":
    cant_palabras += 1
    longitud=len(palabra)
    if sonpalindromos(palabra):
        son_palindromos += 1
    else:
        noson_palindromos += 1
    palabra=str(input("Ingrese palabra : "))
    
print(f"\nCantidad de palabras ingresadas: {cant_palabras}")
print(f"Cantidad de palabras palíndromas: {son_palindromos}")
print(f"Cantidad de palabras no palíndromas: {noson_palindromos}")