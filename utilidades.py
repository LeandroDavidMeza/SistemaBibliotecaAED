# ---------------------------------------------------------------------------
# Módulo de utilidades comunes a todo el sistema.
# Centraliza el manejo de errores (try/except) al leer datos por teclado
# y la generación automática e incremental de los ID.
# ---------------------------------------------------------------------------
from datetime import datetime


def leer_texto(mensaje):
    """
    Pide un texto por teclado. Elimina espacios sobrantes y cualquier ';'
    (el ';' es el separador de los .txt y rompería el archivo).
    No acepta vacío: si tras la limpieza no queda nada, vuelve a pedir.
    """
    while True:
        valor = input(mensaje).replace(";", "").strip()
        if valor != "":
            return valor
        print("❌ El dato no puede quedar vacío ni contener solo ';'. Intente nuevamente.")


def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Pide un número entero por teclado usando try/except.
    Si el usuario escribe letras u otro símbolo, avisa y vuelve a preguntar.
    Se pueden fijar un mínimo y un máximo opcionales.
    """
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("❌ Error: debe ingresar un número entero.")
            continue

        if minimo is not None and valor < minimo:
            print(f"❌ El valor no puede ser menor que {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"❌ El valor no puede ser mayor que {maximo}.")
        else:
            return valor


def leer_fecha(mensaje):
    """
    Pide una fecha con día, mes y año en formato DD/MM/AAAA.
    Usa try/except con datetime para validar que la fecha realmente exista
    (por ejemplo, rechaza 31/02/2026).
    """
    while True:
        texto = input(mensaje).strip()
        try:
            # strptime lanza ValueError si el formato o la fecha no son válidos
            datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print("❌ Fecha inválida. Use el formato DD/MM/AAAA (ej: 09/07/2026).")


def generar_nuevo_id(lista, clave_id):
    """
    Genera un ID incremental automático (1, 2, 3...).
    Recorre la lista elemento a elemento buscando el ID más alto usado
    y le suma 1. Si la lista está vacía, arranca en 1.
    """
    maximo = 0
    for elemento in lista:
        id_actual = int(elemento[clave_id])
        if id_actual > maximo:
            maximo = id_actual
    return maximo + 1

def dias_entre(fecha_inicio, fecha_fin):
    """
    Días entre dos fechas en formato DD/MM/AAAA (ya validadas por leer_fecha).
    Positivo si fecha_fin es posterior; negativo si es anterior.
    """
    d1 = datetime.strptime(fecha_inicio, "%d/%m/%Y")
    d2 = datetime.strptime(fecha_fin, "%d/%m/%Y")
    return (d2 - d1).days