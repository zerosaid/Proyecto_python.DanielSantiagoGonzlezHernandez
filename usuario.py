
import os
import json 

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
            data = json.load(archivo)
            #print(f"Contenido de archivo json {nombre_archivo} : {data}")
            return data
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado")
    except json.JSONDecodeError:
        print(f"Los datos escritos en el archivo {nombre_archivo} no tienen formato JSON")
    except IOError as e:
        print(f"Hubo un error al leer el archivo {nombre_archivo}:{e}")

def agregar_nuevos_elementos_json(nombre_archivo,new_dicc):
    datos = leer_json(nombre_archivo)
    datos.append(new_dicc)
    escribir_json(nombre_archivo,datos)

def gestion_datos():
    datos_usuario = {}
    datos_usuario['año'] = input("Ingrese el año del cual desea investigar: ")
    datos_usuario['nombre'] = input("Ingrese el nombre del pais que desea revisar:  ").capitalize()
    datos_usuario['codigo ISO3'] = (datos_usuario['nombre'].upper()[:3])
    datos_usuario['codigo ISO'] = (datos_usuario['nombre'].upper()[:2])

def interaccion_paises():
    print("Colombia supremasi")
def generar_informe():
    print("Pere que el sistema esta lento")
def modulo_reportes():
    print("""Obtener todos los datos de población para India desde 2000 hasta 2023.
Listar los países con su información de código ISO y código ISO3.
Datos de población para el indicador 'SP.POP.TOTL'.
Obtener los datos de población de los últimos 10 años para todos los países.
Total de población para India en el año 2022.
Población total registrada antes del año 2000.
Población total registrada después del año 2010.
Porcentaje de crecimiento de la población de India entre 2010 y 2020.
Población de India en el año 2023 (si está disponible).
Obtener el año con la población más baja para India.
Número de registros de población por año.
Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.
Listar los años en los que la población de India superó los 1,000 millones.
Obtener la población total registrada para todos los países en el año 2000.
Obtener la población menos registrada para India en los últimos 20 años.
Promedio de población registrada por año para India desde 1980 hasta 2020.
Cantidad de años con datos de población disponibles para India.
Listar los países con datos de población disponibles para cada año entre 2000 y 2023.
Población total de India en 2019.
Años en los que la población de India creció más de 1 millón en comparación con el año anterior.
Población registrada de India en cada década desde 1960.
Población total registrada para todos los países en 2023.
Años en los que no hay datos de población disponibles para India.
Año con la población más alta registrada para India.
Años con datos de población disponibles para más de 50 países.""")

opciones = {"1": gestion_datos, "2": interaccion_paises, "3": generar_informe, "4": modulo_reportes}

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
    elif opc == "5":
        print("Saliendo...")
        break
    else:
        print("Lea bien...")
        

