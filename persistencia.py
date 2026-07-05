import os

SEPARADOR = ";"

def asegurar_directorio(ruta):
    """Crea la carpeta si no existe."""
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def cargar_datos(archivo, campos):
    """Lee el archivo .txt y carga los datos en una lista de diccionarios."""
    lista_datos = []
    if not os.path.exists(archivo):
        return lista_datos
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    valores = linea.split(SEPARADOR)
                    if len(valores) == len(campos):
                        dicc = {}
                        for i in range(len(campos)):
                            dicc[campos[i]] = valores[i]
                        lista_datos.append(dicc)
                    else:
                        print(f"⚠️ Línea ignorada por formato incorrecto en {archivo}.")
    except IOError as e:
        print(f"❌ Error al leer {archivo}: {e}")
    return lista_datos

def guardar_datos(archivo, lista_datos, campos):
    """Escribe la lista de diccionarios en el archivo .txt separando por ';'."""
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for registro in lista_datos:
                valores = []
                for campo in campos:
                    valores.append(str(registro[campo]))
                f.write(SEPARADOR.join(valores) + "\n")
    except IOError as e:
        print(f"❌ Error al guardar {archivo}: {e}")