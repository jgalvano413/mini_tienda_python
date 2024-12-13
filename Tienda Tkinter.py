import sqlite3
import time
import datetime
import tkinter as tk

historial = []
carrito = []
saldo = 0
Ciclo = True
debt2 = 0
Productos = {1: "Barbacoa", 2: "Hocho", 3: "Horchata", 4: "Taco de Chorizo", 5: "Agua de Coco"}
Costos = {"Barbacoa": 500, "Hocho": 15, "Horchata": 25, "Taco de Chorizo": 35, "Agua de Coco": 800}

root = tk.Tk()
root.title("Tienda Galvana")


def setData():
    global debt2
    debt2 = debt2 + 1
    label.config(text="Tu deuda es de: " + str(debt2))

button = tk.Button(root, text="Incrementar deuda", command=setData)
button.pack(side=tk.LEFT)


button2 = tk.Button(root, text="Pagar", command=setData)
button2.pack(side=tk.LEFT)

label = tk.Label(root, text="Tu deuda es de: " + str(debt2))
label.pack()

root.mainloop()
