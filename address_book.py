import random
from datetime import datetime

def escribe_archivo(registro):
    f = open ('addresses.csv','a')
    f.write(registro+"\n")
    f.close
    
id=random.randint(0,100000)
fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")

nombre=str(input("Ingrese nombre : "))
direccion=str(input("Ingrese direccion : "))
telefono=str(input("Ingrese numero de telefono: "))

escribe_archivo(str(id)+","+nombre+","+direccion+","+telefono+","+fecha)
