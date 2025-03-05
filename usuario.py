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
            return json.load(archivo)
    except FileNotFoundError:
        print(f"⚠️ El archivo '{nombre_archivo}' no fue encontrado. Creándolo vacío...")

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

def gestion_datos():
    
    nombre =  input("Ingrese el nombre del país por ejemplo: Indonesia ").capitalize()
    codigo_iso =  input("Ingrese el código ISO por ejemplo: ID ").upper()
    codigo_iso3 =  input("Ingrese el código ISO3 por ejemplo: IDN ").upper()

    if  nombre in paises:
        print("Pais ya Registrado")
    elif nombre != "" and codigo_iso != "" and codigo_iso3 != "":
        new_dicc = {
                "nombre":nombre,
                "codigo_iso":codigo_iso,
                "codigo_iso3":codigo_iso3 
            }
        agregar_nuevos_elementos_json("paises.json",new_dicc)
        return
    else:
        print("No se ingresaron datos")
    gestion_datos()

def obtener_paises():
    paises = gestion_datos('paises.json')
    return [(p["nombre"], p["codigo_iso"], p["codigo_iso3"]) for p in paises]

def indicadores ():
    opc= input("¿Desea agregar un nuevo indicador? (s/n): ").lower()
    if opc == "s":
        """Solicita datos al usuario y los guarda en el JSON."""
        datos = leer_json("indicadore.json")
        agregar_nuevos_elementos_json("indicadore.json",new_dic)

        nuevo_indicador = {
            "id_indicador": input("Ingrese el ID del indicador: "),
            "descripcion": input("Ingrese la descripción del indicador: ")
        }
        if any(ind["id_indicador"] == nuevo_indicador["id_indicador"] for ind in datos):
            print("El indicador ya está registrado.")
        else:
            datos.append(nuevo_indicador)
            escribir_json("paises.json", datos)
            print("Indicador agregado correctamente.")
    elif opc == "n":
        """Muestra todos los indicadores almacenados en el JSON."""
        datos = leer_json("indicadore.json")
        if not datos:
            print("No hay indicadores registrados.")
        else:
            for ind in datos:
                print(f"ID: {ind['id_indicador']}, Descripción: {ind['descripcion']}")

def interaccion_paises():
    while True:
        opc = input("Digite: \n1. Para ver paises\n2. Para ver o agregar indicadores\n3. Para volver\n")
        if opc == "1":
            for i in paises:
                print (i)
        elif opc == "2":
            indicadores()
        elif opc == "3":
            return menu()
        else:
            print("Opción no válida, intente de nuevo.")        

def generar_informe():
    def leer_json(nombre_archivo):
        #Lee y devuelve el contenido del archivo JSON como una lista. Si no existe, crea uno vacío.
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                try:
                    datos = json.load(archivo)
                    return datos if isinstance(datos, list) else []
                except json.JSONDecodeError:
                    return []  # Si hay error en el JSON, devolver lista vacía
        else:
            # Si el archivo no existe, se crea vacío
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
            return []

    def guardar_json(nombre_archivo, datos):
        """Guarda los datos en un archivo JSON."""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def agregar_dato_poblacion():
        """Permite agregar un nuevo dato de población al JSON."""
        datos = leer_json(NOMBRE_ARCHIVO2)

        try:
            #Registra los paise si no existe creando un archivo json
            nuevo_dato = {
                "ano": int(input("Ingrese el año del dato: ")),
                "pais": input("Ingrese el nombre del país: ").strip().capitalize(),
                "codigo_iso3": input("Ingrese el código ISO3 del país: ").strip().upper(),
                "indicador_id": "SP.POP.TOTL",
                "descripcion": "Total de población",
                "valor": int(input("Ingrese el valor de la población: ")),
                "estado": "disponible",
                "unidad": "personas"
            }
            datos.append(nuevo_dato)
            guardar_json(NOMBRE_ARCHIVO2, datos)
            print("\n Nuevo dato agregado correctamente al archivo JSON.")

        except ValueError:
            print("⚠️ Error: Ingrese valores numéricos en el año y la población.")
    #Entrega una lista de los cambiso entre las fechas por los datos ingresados
    def generar_informe():
        """Genera un informe de población para un país en un período de tiempo específico."""
        datos = leer_json(NOMBRE_ARCHIVO2)

        if not datos:
            print("No hay datos de población registrados.")
            return

        pais = input("Ingrese el nombre del país: ").strip().capitalize()
        try:
            anio_inicio = int(input("Ingrese el año de inicio: "))
            anio_fin = int(input("Ingrese el año de fin: "))

            if anio_inicio > anio_fin:
                print("⚠️ Error: El año de inicio no puede ser mayor que el año de fin.")
                return

            # Filtrar los datos según el país y el período de tiempo
        # (
            datos_filtrados = [
                dato for dato in datos 
                if dato["pais"].capitalize() == pais.capitalize() and anio_inicio <= dato["ano"] <= anio_fin
            ]

            if datos_filtrados:
                print(f"\n Informe de población para {pais} ({anio_inicio} - {anio_fin}):\n")
                for dato in datos_filtrados:
                    print(f"Año: {dato['ano']}, Población: {dato['valor']} {dato['unidad']}")
            else:
                print(f"⚠️ No se encontraron datos para {pais} en el período {anio_inicio}-{anio_fin}.")
        except ValueError:
            print("⚠️ Error: Ingrese años válidos en formato numérico.")#) <- La filtracion se da hasta este punto si no hay mas datos esta no se llevara acabo marcando el error :)

    if __name__ == "__main__":
        while True:
            print("1. Agregar un dato de población")
            print("2. Generar informe de población")
            print("3. Volver a interfaz inicial")

            opc = input("Seleccione una opción: ")
            if opc == "1":
                agregar_dato_poblacion()
            elif opc == "2":
                generar_informe()
            elif opc == "3":
                print("Volviendo...")
                return menu()
            else:
                print("⚠️ Opción inválida. Intente de nuevo.")

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
                        print("Escoja una opc presentada")
                        return modulo_reportes()
        else:
            print("por favor identifique un pais existente en el sistema de lo contrario registrelo por favor.")
            break

new_dic={}
archivo = "Paises.json"
opciones = {"1": gestion_datos, "2": interaccion_paises, "3": generar_informe, "4": modulo_reportes}
paises = {i["nombre"]:[i["codigo_iso"], i["codigo_iso3"]] for i in leer_json("paises.json")}
NOMBRE_ARCHIVO = "indicadores.json"
NOMBRE_ARCHIVO2 = "poblacion.json"

def menu ():
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
menu()
