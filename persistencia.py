import os

def asegurar_directorio(ruta):
    """Crea la carpeta si no existe."""
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def cargar_datos(archivo, campos):
    """Lee el archivo .txt y carga los datos en una lista de diccionarios."""
    lista_datos = []
    if not os.path.exists(archivo):
        return lista_datos
        
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                valores = linea.split(',')
                # Si la línea tiene la cantidad de datos correcta, armamos el diccionario
                if len(valores) == len(campos):
                    dicc = {}
                    for i in range(len(campos)):
                        dicc[campos[i]] = valores[i]
                    lista_datos.append(dicc)
    return lista_datos

def guardar_datos(archivo, lista_datos, campos):
    """Saca los datos de la lista de diccionarios y los escribe en el archivo .txt."""
    with open(archivo, 'w', encoding='utf-8') as f:
        for registro in lista_datos:
            # Armamos una lista con los valores en el orden estricto de los campos
            valores = []
            for campo in campos:
                valores.append(str(registro[campo]))
            # Los juntamos con comas y los escribimos en un renglón
            f.write(",".join(valores) + "\n")
            