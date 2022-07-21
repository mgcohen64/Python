import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
from turtle import color, left


def genera_clave():
    
    # Definicion de variables para generar las listas de caracteres que se consideraran para armar la clave
    listaminusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listamayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    listanumeros = ["0","1","2","3","4","5","6","7","8","9"]
    listaespeciales = ["+","-","%","$","&","#"]
    password=""
    lista=[]
    largo=longitud.get()
    
    # Verifica si los checkbox estan activos y agrega los caracteres que corresponden segun esto    
    if minusculas.get() == 1:
        lista = lista+ listaminusculas
    if mayusculas.get() == 1:
        lista = lista + listamayusculas
    if numeros.get() == 1:
        lista = lista + listanumeros
    if especiales.get() == 1:
        lista = lista + listaespeciales
    
    # De acuerdo al valor de longitud, se genera un caracter aleatoriamente y se lo guarda en password
    for i in range (0,largo,1):
        password +=(random.choice(lista))
    
    # Borra el contenido de la ventana 
    ventana.delete(0, tk.END)
    # Escrive la nueva clave en la ventana
    ventana.insert(0, password)       

# Crea una ventana de 300 x 300 con titulo Password Generator    
root = Tk()
root.title("Password Generator")
root.geometry("300x250")

# Crea una ventana para mostrar la clave generada
ventana=ttk.Entry()
ventana=ttk.Entry(justify=tk.CENTER)
ventana.configure(font=("Arial", 11),foreground="red")
ventana.place(x=60, y=130, width=180, height=20)

minusculas=1
mayusculas=1
numeros=1
especiales=1

# Crea los checkbox de cada tipo de caracter y lo activa por defecto ( con c1.select() )
minusculas = IntVar()
c1 = tk.Checkbutton(root, text='Minusculas',variable=minusculas, onvalue=1, offvalue=0)
c1.pack()
c1.select()

mayusculas = IntVar()
c2 = tk.Checkbutton(root, text='Mayusculas',variable=mayusculas, onvalue=1,offvalue=0)
c2.pack()
c2.select()

especiales = IntVar()
c3 = tk.Checkbutton(root, text='Carateres especiales',variable=especiales, onvalue=1,offvalue=0)
c3.pack()
c3.select()

numeros = IntVar()
c4 = tk.Checkbutton(root, text='Numeros',variable=numeros, onvalue=1, offvalue=0)
c4.pack()
c4.select()

# Crea una etiqueta con texto "Longitud" para ingresar el largo de la clave. Le asigna una variable longitud
Label(root, text = "Longitud").place(x = 20,y = 100)
# Crea una variable para el ingreso inicilizada en 10
longitud=IntVar(value = 10)
# Crea el campo para ingresar la variable longitud
Entry(root,textvariable=longitud, bd =3, width=5).place(x = 80, y = 100)

# Crea un boton para generar la clave
boton_generar=Button(root, text='Generar', command=lambda:genera_clave())
boton_generar.place(x=120, y=170)

# Crea un boton para salir de la aplicacion
button_exit = tk.Button(root, text='Exit', command=root.destroy)
button_exit.place(x=130, y=200)

root.mainloop()
