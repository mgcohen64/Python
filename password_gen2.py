import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from turtle import left


def genera_clave(largo):
    
    listaminusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listamayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    listanumeros = ["0","1","2","3","4","5","6","7","8","9"]
    listaespeciales = ["+","-","%","$","&","#"]
    password=""
    lista=[]
        
    if minusculas.get() == 1:
        lista = lista+ listaminusculas
    if mayusculas.get() == 1:
        lista = lista + listamayusculas
    if numeros.get() == 1:
        lista = lista + listanumeros
    if especiales.get() == 1:
        lista = lista + listaespeciales
    
    for i in range (1,largo,1):
        password +=(random.choice(lista))
#    print(password)

    ventana.delete(0, tk.END)
    ventana.insert(0, password)       
    
root = Tk()
root.title("Password Generator")
root.geometry("300x300")

ventana=ttk.Entry()
ventana=ttk.Entry(justify=tk.CENTER)
ventana.configure(font=("Arial", 12))
ventana.place(x=90, y=130, width=145, height=25)

#l = tk.Label(root, bg='lightgrey', width=20, text='')

minusculas=1
mayusculas=1
numeros=1
especiales=1
longitud=10

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

#Label(root, text = "Longitud").place(x = 20,y = 100)
#longitud=IntVar()
#Entry(root,textvariable=longitud).place(x = 80, y = 100)
#L1=longitud.get()
#print(L1)

boton_generar=Button(root, text='Generar', command=lambda:genera_clave(longitud))
boton_generar.place(x=120, y=170)

button_exit = tk.Button(root, text='Exit', command=root.destroy)
button_exit.place(x=130, y=200)

root.mainloop()


