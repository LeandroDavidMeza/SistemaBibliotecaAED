from utilidades import leer_texto, generar_nuevo_id
# Estructura homogénea requerida por la cátedra para el diccionario de libros
CAMPOS_LIBROS = ["IDLibro", "ISBN", "Titulo", "Autor", "StockTotal", "StockDisponible"]


def crear_libro(id_libro, isbn, titulo, autor, cantidad=1):
    """
    Retorna un diccionario estructurado para representar un libro.
    Al crearlo, el stock total y el disponible arrancan iguales.
    """
    return {
        "IDLibro": str(id_libro),
        "ISBN": isbn,
        "Titulo": titulo,
        "Autor": autor,
        "StockTotal": str(cantidad),
        "StockDisponible": str(cantidad),
    }


def buscar_libro(libros, criterio):
    """
    Recorre la lista de libros elemento a elemento buscando coincidencia.
    Acepta como criterio el IDLibro o el ISBN (lo que resulte más cómodo).
    Retorna el diccionario del libro si lo encuentra, o None si no existe.
    """
    for libro in libros:
        if libro["IDLibro"] == criterio or libro["ISBN"] == criterio:
            return libro
    return None


def agregar_libro(libros):
    """
    Añade un libro al sistema recorriendo la lista elemento a elemento.
    Si el ISBN ya existe, NO crea un registro nuevo: aumenta en 1 el stock
    (total y disponible) del libro que ya estaba cargado.
    Si el ISBN es nuevo, genera un ID automático e incremental.
    """
    print("\n[📚 Alta de Libro]")
    isbn = leer_texto("Ingrese el código ISBN: ")

    # Buscamos si ya existe un libro con ese ISBN (elemento a elemento)
    libro_existente = None
    for libro in libros:
        if libro["ISBN"] == isbn:
            libro_existente = libro
            break  # cortamos el ciclo apenas encontramos la coincidencia

    if libro_existente is not None:
        # Acumulador: sumamos un ejemplar al mismo registro
        nuevo_total = int(libro_existente["StockTotal"]) + 1
        nuevo_disp = int(libro_existente["StockDisponible"]) + 1
        libro_existente["StockTotal"] = str(nuevo_total)
        libro_existente["StockDisponible"] = str(nuevo_disp)
        print(f"✔️ El libro ya existía. Se sumó un ejemplar.")
        print(f"   Stock total: {nuevo_total} | Disponibles: {nuevo_disp}")
    else:
        # ID automático e incremental (no lo escribe el usuario)
        nuevo_id = generar_nuevo_id(libros, "IDLibro")
        titulo = leer_texto("Título del libro: ")
        autor = leer_texto("Autor del libro: ")

        nuevo_l = crear_libro(nuevo_id, isbn, titulo, autor)
        libros.append(nuevo_l)
        print(f"✔️ Nuevo libro registrado. ID automático asignado: {nuevo_id}")


def listar_libros(libros):
    """Muestra el catálogo completo recorriendo la lista elemento a elemento."""
    print("\n--- 📋 CATÁLOGO DE LIBROS ---")
    if not libros:
        print("No hay libros registrados en el catálogo.")
        return

    for libro in libros:
        print(
            f"ID: {libro['IDLibro']} | ISBN: {libro['ISBN']} | "
            f"Título: {libro['Titulo']} | Autor: {libro['Autor']} | "
            f"Stock total: {libro['StockTotal']} | Disponibles: {libro['StockDisponible']}"
        )