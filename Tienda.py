import sqlite3
import time
import datetime

conn = sqlite3.connect('historial.db')
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE history (id INTEGER PRIMARY KEY, message TEXT)''')
    print("Tabla Creada")
except sqlite3.Error as e:
    pass
    

historial = []
carrito = []
saldo = 0
Ciclo = True
debt2 = 0
Productos = {1:"Barbacoa",2:"Hocho",3:"Horchata",4:"Taco de Chorizo",5:"Agua de Coco"}
Costos = {"Barbacoa":500,"Hocho":15,"Horchata":25,"Taco de Chorizo":35,"Agua de Coco":800}


def showHistory():
    print("--------------------------------------------------")
    index = 1
    print("Historial de Compra: ")
    print(" ")
    cursor.execute("SELECT * FROM history")
    filas = cursor.fetchall()
    conn.commit()
    for things in filas:
        print(str(index) + ".- " + str(things))  
        index += 1
    if index == 1:
        print(" Vacio ")
    print(" ")
    print("--------------------------------------------------")

def showbuy():
    print("--------------------------------------------------")
    index = 1
    print("Tu Carrito: ")
    print(" ")
    for things in carrito:
        print(str(index) + ".- " + things)  
        index += 1
    if index == 1:
        print(" Vacio ")
    print(" ")
    print("--------------------------------------------------")    
    
def pay():
    debt = 0
    amoundeb = 0
    payaccount = True
    trypay = 0
    print("--------------------------------------------------")
    print("Pago")
    print(" ")
    for price in carrito:
        debt = debt + Costos[price]
        amoundeb = amoundeb + Costos[price]
        
    if debt > 0:
        while payaccount:
            trypay += 1
            print("Monto a pagar " + str(debt))
            print(" ")
            print("Ingresa Cantidad a Pagar:")
            amount = input()
            try: 
                amount = int(amount)
                if amount < debt:
                    debt = debt - amount
                    print("Aun debes " + str(debt) + " No te vayas Qlo ")
                    print("  ")
                    if trypay > 3 and trypay <= 7:
                         print("Si andas de Perro mejor dime")
                         
                    elif trypay > 8:
                         print("Cancelo este pedo?")
                         print(" ")
                         print("1.- Si")
                         print("2.- No")
                         print(" ")
                         debt2 = debt
                         choice = input()
                         try:
                            choice = int(choice)
                            if choice == 1:
                                payaccount = False
                                print("Cancelado Por Andar de perro miserable")
                            elif choice == 2:
                                print("Entonces Paga qlero")
                            else:
                                print("Opcion no valida")
                         except ValueError:
                             print("Opcion no valida")
                             
                    print("--------------------------------------------------")
                else:
                    print("Pagado")
                    fecha = datetime.datetime.now().strftime("%A, %d de %B de %Y a las %H:%M")
                    message = "Se Registro una venta de $" + str(amoundeb) + " el dia " + str(fecha) 
                    cursor.execute("INSERT INTO history (message) VALUES (?)", (message,))
                    conn.commit()
                    #historial.append(message)
                    carrito.clear()
                    chancla = amount - debt
                    if chancla > 0:
                        print("Gracias Por su compra Retire su Cambio de " + str(chancla))
                    else:
                        print("Gracias por su Compra nunca regrese Qlero")
                    break
                    payaccount = False
                    debt2 = 0
                    
            except ValueError:
                print("Opcion no valida")
    else:
        print("No debes nada Qlero")
        print(" ")
        
    print("--------------------------------------------------")
 
 

     
while Ciclo:
    print("--------------------------------------------------")
    print("Por Favor Escoge el numero de un producto: ")
    print("1.- Barbacoa")
    print("2.- Hochos Prrns")
    print("3.- Un Horchaton")
    print("4.- Tacos de Chorizo")
    print("5.- Awita de Coco")
    print("6.- Mostrar Carrito")
    print("7.- Pagar")
    print("8.- Historial de Compra")
    print("9.- Salir")
    print("--------------------------------------------------")
    user = input()
    try:
        user = int(user)
        if user in Productos:
            product = Productos[user]
            cost = Costos[product]
            print("Escogiste la Opcion " + product + " con costo de " + "$" +str(cost) + " MXN")
            print("1.- Si")
            print("2.- No")
            choice = input("¿Es Correcto? ")
            try:
                choice = int(choice)
                if choice == 1:
                    carrito.append(product)
            except ValueError:
                print("Opcion no valida")
        elif user == 6:
            showbuy()      
        elif user == 7:
            pay()
        elif user == 8:
            showHistory()
        elif user == 9:
            print("Vuelve Pronto Qlero")
            conn.close()
            break
        else:
            print("Producto No Encontrado o Opcion no valida")
    except ValueError:
        print("Opcion no valida")
    