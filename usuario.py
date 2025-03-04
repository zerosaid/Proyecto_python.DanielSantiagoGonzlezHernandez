
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

def gestion_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        datos_usuario = {}
    datos_usuario['año'] = input("Ingrese el año del cual desea investigar: ")
    datos_usuario['nombre'] = input("Ingrese el nombre del pais que desea revisar:  ").capitalize()
    datos_usuario['codigo ISO3'] = (datos_usuario['nombre'].upper()[:3])
    datos_usuario['codigo ISO'] = (datos_usuario['nombre'].upper()[:2])
    return json.load(f)

def obtener_paises():
    paises = gestion_datos('paises.json')
    return [(p["nombre"], p["codigo_iso"], p["codigo_iso3"]) for p in paises]

def obtener_indicadores():
    indicadores = gestion_datos('indicadores.json')
    return {i["id_indicador"]: i["descripcion"] for i in indicadores}

def obtener_poblacion_por_pais(pais, indicador="SP.POP.TOTL"):
    poblacion = gestion_datos('poblacion.json')
    return [p for p in poblacion if p["pais"] == pais and p["indicador_id"] == indicador]

def obtener_poblacion_por_rango(pais, inicio, fin):
    datos = obtener_poblacion_por_pais(pais)
    return [p for p in datos if inicio <= p["ano"] <= fin]

def obtener_poblacion_total_anio(anio):
    poblacion = gestion_datos('poblacion.json')
    return sum(p["valor"] for p in poblacion if p["ano"] == anio)

def obtener_anio_poblacion_extrema(pais, tipo="min"):
    datos = obtener_poblacion_por_pais(pais)
    if tipo == "min":
        return min(datos, key=lambda x: x["valor"])["ano"]
    return max(datos, key=lambda x: x["valor"])["ano"]

def calcular_crecimiento_poblacional(pais, anio_inicio, anio_fin):
    datos = obtener_poblacion_por_pais(pais)
    inicio = next((p["valor"] for p in datos if p["ano"] == anio_inicio), None)
    fin = next((p["valor"] for p in datos if p["ano"] == anio_fin), None)
    if inicio and fin:
        return ((fin - inicio) / inicio) * 100
    return None

if __name__ == "__main__":
    pais = input("Ingrese el nombre del país: ")
    print(f"Población de {pais} entre 2000 y 2023:", obtener_poblacion_por_rango(pais, 2000, 2023))


def interaccion_paises():
    print("Colombia supremasi")
def generar_informe():
    print("Pere que el sistema esta lento")
def modulo_reportes():
    opc = input(""" Seleccione:
1. Obtener todos los datos de población para India desde 2000 hasta 2023.
2. Listar los países con su información de código ISO y código ISO3.
3. Datos de población para el indicador 'SP.POP.TOTL'.
4. Obtener los datos de población de los últimos 10 años para todos los países.
5. Total de población para India en el año 2022.
6. Población total registrada antes del año 2000.
7. Población total registrada después del año 2010.
8. Porcentaje de crecimiento de la población de India entre 2010 y 2020.
9. Población de India en el año 2023 (si está disponible).
10. Obtener el año con la población más baja para India.
11. Número de registros de población por año.
12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.
13. Listar los años en los que la población de India superó los 1,000 millones.
14. Obtener la población total registrada para todos los países en el año 2000.
15. Obtener la población menos registrada para India en los últimos 20 años.
16. Promedio de población registrada por año para India desde 1980 hasta 2020.
17. Cantidad de años con datos de población disponibles para India.
18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.
19. Población total de India en 2019.
20. Años en los que la población de India creció más de 1 millón en comparación con el año anterior.
21. Población registrada de India en cada década desde 1960.
22. Población total registrada para todos los países en 2023.
23. Años en los que no hay datos de población disponibles para India.
24. Año con la población más alta registrada para India.
25. Años con datos de población disponibles para más de 50 países.
""")
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
