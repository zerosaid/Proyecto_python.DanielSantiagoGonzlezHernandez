import json
import os

def escribir_json(nombre_archivo, diccionario):
    try:
        with open(nombre_archivo,"w", encoding='utf-8') as archivo:
            json.dump(diccionario, archivo, indent=4)
        print(f"Los datos fueron escritos correctamente en el archivo {nombre_archivo}")
    except (KeyError, ValueError) as e:
        print(f"Error al escribir en el archivo {nombre_archivo} : {e}")
    except IOError as e:
        print(f"Ocurrio un error al escribir en el archivo {nombre_archivo} : {e}")

def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f" El archivo '{nombre_archivo}' no fue encontrado. Creándolo vacío...")

        return []
    except json.JSONDecodeError:
        print(f" Error: El archivo '{nombre_archivo}' no tiene formato JSON válido.")
        return []
    except IOError as e:
        print(f" Error al leer el archivo '{nombre_archivo}': {e}")
        return []

def agregar_nuevos_elementos_json(json,new_dicc):
        datos = leer_json(json)
        datos.append(new_dicc)
        escribir_json(json,datos)   

def registrar_pedido():
    
    nombre =  input("Ingrese su nombre: ").capitalize()
    agregar_nuevos_elementos_json("pedidos.json",orden)
    if nombre == (""):
        return registrar_pedido

    pedido =  input("Ingrese el nombre de su pedido: ").capitalize()
    agregar_nuevos_elementos_json("pedidos.json",orden)
    if pedido == (""):
        return registrar_pedido

    if  nombre in pedidos:
        print("Pedido ya registrado")
    elif nombre != "" and pedido != "":
        new_dicc = {
                "nombre":"",
                "pedido":"",
            }
        if nombre in pedidos:
            print("Pedido ya registrado")
        agregar_nuevos_elementos_json("pedidos.json",new_dicc)
        return
    else:
        print("No se ingresaron datos")
    registrar_pedido()

def obtener_pedidos():
    pedidos = registrar_pedido('pedidos.json')
    return [(p["nombre"], p["pedido"], p["precio"]) for p in pedidos]

def revisar_pedido ():
    opc= input("Desea ver un pedido especifico s/n").lower()
    if opc == "s":
        datos = leer_json("pedidos.json")
        agregar_nuevos_elementos_json("pedidos.json",new_dic)

        pedidos_especifico = {
            "nombre": input("Ingrese el nombre del cliente ").capitalize(),
            "pedido": input("Ingrese el pedido que hizo").capitalize(),
        }
        if any(ind["nombre"] == pedidos_especifico["nombre"] for ind in datos):
            print("Pedido si existe aun no ha sido cancelado")
        else:
            print("Pedido no existe o ya ha sido canselado")
            leer_json("pedidos.json", datos)
    elif opc == "n":
        print("Mostrando todos los pedidos realizados")
        datos = leer_json("pedidos.json")
        if not datos:
            print("No hay pedidos realizados.")
        else:
            for ind in datos:
                print(f"Pedido: {ind['pedido']}, costo: {ind['precio']}")

def realizar_pago():
    def leer_json(nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                try:
                    datos = json.load(archivo)
                    return datos if isinstance(datos, list) else []
                except json.JSONDecodeError:
                    return []
        else:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
            return []
    def guardar_json(nombre_archivo, datos):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def pagar():
        datos = leer_json(NOMBRE_ARCHIVO2)
        try:
            nuevo_dato = {
                "precio": int(input("ingrese el monto a pagar: ")),
                "nombre": input("Ingrese el nombre del cliente: ").strip().capitalize(),
                "pedido": input("Ingrese el pedido realizado: ").strip().capitalize(),
            }
            datos.append(nuevo_dato)
            guardar_json(NOMBRE_ARCHIVO2, datos)

            print("\n El pago ha sido realizado y almacenado.")

        except ValueError:

            print("Error: Ingrese valores numéricos en el año y la población.")

    if __name__ == "__main__":
        while True:
            print("Seleccione:\n1. Pagar.\n2.Volver.")
            opc = input("Seleccione una opción: ")
            if opc == "1":
                pagar()
            elif opc == "2":
                print("Volviendo...")
                return menu()
            else:
                print("Opción inválida. Intente de nuevo.")

def ver_menu():
    while True:
        opc = input(""" 
                    Seleccione lo que desee

        ENTRADAS:       
        "Entrada":"Papas frtitas"               "Precio":5000
        "Entrada":"Sopa"                        "Precio":8000
        "Entrada":"Empanadas mini"              "Precio":9000
        "Entrada":"Ensalada"                    "Precio":7500

        PLATO FUERTE:   2
        "Plato fuerte":"Pollo Apanado"        "Precio":"12000
        "Plato fuerte":"Carne molida"         "Precio":"12000
        "Plato fuerte":"Cerdo frito"          "Precio":"12000
        "Plato fuerte":"Carne Asada"          "Precio":"15000
        "Plato fuerte":"Lomo Doreado"         "Precio":"16000
        "Plato fuerte":"Pechuga Asada"        "Precio":"15000
        "Plato fuerte":"Carne Bbq"            "Precio":"17000

        BEBIDAS:        3
        "Bebida":"Limonada"                     "Precio":6000
        "Bebida":"Limonada cerezada"            "Precio":7500
        "Bebida":"Gaseosa persona, 350ml"       "Precio":7000
        "Bebida":"Gaseosa 1.5l"                 "Precio":9000
        "Bebida":"Cerveza en lata"              "Precio":6500

        SALIR:          4
                    """)
        if opc == "1":
            for i in pedidos:
                registrar_pedido()
                print (i)
        elif opc == "2":
            for i in pedidos2:
                registrar_pedido()
                print (i)
        elif opc == "3":
            for i in pedidos3:
                registrar_pedido()
                print (i)
        elif opc == "4":
            return menu()
        else:
            print("Opción no válida, intente de nuevo.")  
   
new_dic={}
orden = {
    "nombre":"",
    "pedido":""
}
archivo = "pedidos.json"
pedidos = {i["nombre"]:[i["Entrada"], i["precio"]] for i in leer_json("Entradas.json")}
pedidos2 = {i["nombre"]:[i["Plato fuerte"], i["precio"]] for i in leer_json("Plato_fuerte.json")}
pedidos3 = {i["nombre"]:[i["Bebida"], i["precio"]] for i in leer_json("Bebidas.json")}
NOMBRE_ARCHIVO2 = "pagos.json"
opciones = {"1": ver_menu, "2": revisar_pedido, "3": realizar_pago}

def menu ():
    while True:
        os.system("cls" if os.name =="nt" else"clear")
        print("Bienvenido a Molipollitapp")
        print("Seleccione:\n1.Si desea ver el menu\n2.Revisar los pedidos ya realizados\n3.Realizar el pago de los pedidos\n0.Salir")
        opc = input("Ingrese la opción requerida: \n")
        if opc in opciones:
            os.system("cls" if os.name =="nt" else"clear")
            opciones[opc]()
            input("\n Presione enter para continuar")
        elif opc == "0":
            print("Gracias por visitarnos vuelva pronto")
            break
        else:
            print("Lea bien...")
menu()