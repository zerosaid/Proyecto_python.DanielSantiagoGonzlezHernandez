
import os
import json 

archivo = "Paises.json"


def escribir_json(nombre_archivo, diccionario):
    try:
        with open(nombre_archivo,"w", encoding='utf-8') as archivo:
            json.dump(diccionario, archivo, indent=4)
            input("""
                "nombre": "Indonesia",
                "codigo_iso": "ID",
                "codigo_iso3": "IDN"
                """)
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
        print(f"⚠️ El archivo '{nombre_archivo}' no fue encontrado. Creándolo vacío...")
        escribir_json(nombre_archivo, [])  # Crear archivo vacío
        return []
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no tiene formato JSON válido.")
        return []
    except IOError as e:
        print(f"❌ Error al leer el archivo '{nombre_archivo}': {e}")
        return []

def agregar_nuevos_elementos_json(json,new_dicc):
        datos = leer_json(json)
        datos.append(new_dicc)
        escribir_json(json,datos)

def gestion_datos(nombre_archivo,new_dicc):
    datos = leer_json(nombre_archivo)
    datos.append(new_dicc)
    new_dicc = {
            "nombre": input("Ingrese el nombre del país '(por defecto: Indonesia)': "),
            "codigo_iso": input("Ingrese el código ISO '(por defecto: ID)': "),
            "codigo_iso3": input("Ingrese el código ISO3 '(por defecto: IDN)': ") 
        }
    if any(pais["nombre"] == new_dicc["nombre"] for pais in datos):
        print("Ya está registrado")
    else:
        agregar_nuevos_elementos_json("paises.json",new_dicc)
new_dic={}
def obtener_paises():
    paises = gestion_datos('paises.json')
    return [(p["nombre"], p["codigo_iso"], p["codigo_iso3"]) for p in paises]

def interaccion_paises():
    print("Colombia supremasi")
def generar_informe():
    print("Pere que el sistema esta lento")
def modulo_reportes():
    pais = input("Por favor diga el pais del cual desea ver el modulo de reporte: ").capitalize()
    opc = input(""" Seleccione:
1. Obtener todos los datos de población para un pais desde 2000 hasta 2023.
2. Listar los países con su información de código ISO y código ISO3.
3. Datos de población para el indicador 'SP.POP.TOTL'.
4. Obtener los datos de población de los últimos 10 años para todos los países.
5. Total de población para el pais de su eleccion en el año 2022.
6. Población total registrada antes del año 2000.
7. Población total registrada después del año 2010.
8. Porcentaje de crecimiento de la población de cualquier pais entre 2010 y 2020.
9. Población del pais que desee en el año 2023 (si está disponible).
10. Obtener el año con la población más baja para el pais selecionado.
11. Número de registros de población por año.
12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.
13. Listar los años en los que la población del pais escogido superó los 1,000 millones.
14. Obtener la población total registrada para todos los países en el año 2000.
15. Obtener la población menos registrada para el pais elegido en los últimos 20 años.
16. Promedio de población registrada por año para el pais escogido desde 1980 hasta 2020.
17. Cantidad de años con datos de población disponibles para el pais escogido.
18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.
19. Población total de el pais escogido en 2019.
20. Años en los que la población de el pais escogido creció más de 1 millón en comparación con el año anterior.
21. Población registrada de el pais escogido en cada década desde 1960.
22. Población total registrada para todos los países en 2023.
23. Años en los que no hay datos de población disponibles para el pais escogido.
24. Año con la población más alta registrada para el pais escogido.
25. Años con datos de población disponibles para más de 50 países.
""")
    while True:
        for i in leer_json("paises.json"):
            if i["nombre"] in pais:
                while True:
                    if opc == "1":
                        print("Puto")
                        break
                    elif opc =="2":
                        print("Puto") 
                        break
                    elif opc =="3":
                        print("Puto")
                        break 
                    elif opc =="4":
                        print("Puto")
                        break
                    elif opc =="5":
                        print("Puto") 
                        break
                    elif opc =="6":
                        print("Puto") 
                        break
                    elif opc =="7":
                        print("Puto") 
                        break
                    elif opc =="8":
                        print("Puto") 
                        break
                    elif opc =="9":
                        print("Puto") 
                        break
                    elif opc =="10":
                        print("Puto") 
                        break
                    elif opc =="11":
                        print("Puto") 
                        break
                    elif opc =="12":
                        print("Puto") 
                        break
                    elif opc =="13":
                        print("Puto") 
                        break
                    elif opc =="14":
                        print("Puto") 
                        break
                    elif opc =="15":
                        print("Puto") 
                        break
                    elif opc =="16":
                        print("Puto") 
                        break
                    elif opc =="17":
                        print("Puto") 
                        break
                    elif opc =="18":
                        print("Puto") 
                        break
                    elif opc =="19":
                        print("Puto") 
                        break
                    elif opc =="20":
                        print("Puto") 
                        break
                    elif opc =="21":
                        print("Puto") 
                        break
                    elif opc =="22":
                        print("Puto") 
                        break
                    elif opc =="23":
                        print("Puto") 
                        break
                    elif opc =="24":
                        print("Puto") 
                        break
                    elif opc =="25":
                        print("Puto")
                        break 
                    else:
                        print("Escoja una opcion presentada")
                        return modulo_reportes()
        else:
            print("por favor identifique un pais existente en el sistema de lo contrario registrelo por favor.")
            break

opciones = { "2": interaccion_paises, "3": generar_informe, "4": modulo_reportes}

while True:
    os.system("cls" if os.name =="nt" else"clear")
    print("""
        🂠  🂡  🂫  🂬  🂭  🂮  🃟 🃟  🂱  🂻  🂼  🂽  🂾  🂠
                Gestion de datos del IEG
        🂠  🃁  🃋  🃌  🃍  🃎  🃟 🃟  🃑  🃛  🃜  🃝  🃞  🂠
        """)
    print("Ingrese \n1. Ver Gestión de Datos de Población \n2. Ver Interacción con Países y Indicadores \n3. Generar un informe \n4. Ver Módulo de Reportes \n5. Salir")
    opc = input("Ingrese la opción requerida: \n")
    if opc in opciones:
        os.system("cls" if os.name =="nt" else"clear")
        opciones[opc]()
        input("\n Presione enter para continuar")
    elif opc == "1":
        os.system("cls" if os.name =="nt" else"clear")
        gestion_datos("paises.json",new_dic)
        input("\n Presione enter para continuar")
    elif opc == "5":
        print("Saliendo...")
        break
    else:
        print("Lea bien...")
