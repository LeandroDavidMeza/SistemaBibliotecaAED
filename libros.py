# Estructura homogénea requerida por la cátedra para el diccionario de libros
CAMPOS_LIBROS = ["IDLibro", "ISBN", "Titulo", "Autor", "Cantidad"]

def crear_libro(id_libro, isbn, titulo, autor, cantidad=1):
    """
    Retorna un diccionario estructurado para representar un libro.
    Garantiza que todas las claves sean iguales en cada registro.
    """
    return {
        "IDLibro": str(id_libro),
        "ISBN": isbn,
        "Titulo": titulo,
        "Autor": autor,
        "Cantidad": str(cantidad)
    }

def agregar_libro(libros):
    """
    Añade un libro al sistema. 
    Recorre la lista elemento a elemento buscando coincidencias por ISBN.
    Si el ISBN ya existe, aumenta la cantidad (Stock).
    Si no existe, genera un ID incremental automático.
    """
    print("\n[📚 Alta de Libro]")
    isbn = input("Ingrese el código ISBN: ").strip()
    
    # Validamos elemento a elemento recorriendo la lista según lo pedido
    libro_existente = None
    for l in libros:
        if l["ISBN"] == isbn:
            libro_existente = l
            break # Cortamos el ciclo si encontramos la coincidencia
            
    if libro_existente:
        # Uso de acumulador: convertimos a entero, sumamos 1 y volvemos a texto para el .txt
        nueva_cant = int(libro_existente["Cantidad"]) + 1
        libro_existente["Cantidad"] = str(nueva_cant)
        print(f"✔️ Libro existente detectado. Se acumuló stock. Cantidad actual: {nueva_cant}")
    else:
        # ID automático basado en el tamaño actual de la lista (incremental)
        nuevo_id = len(libros) + 1
        titulo = input("Título del libro: ").strip()
        autor = input("Autor del libro: ").strip()
        
        nuevo_l = crear_libro(nuevo_id, isbn, titulo, autor)
        libros.append(nuevo_l)
        print(f"✔️ Nuevo libro registrado con éxito. ID automático asignado: {nuevo_id}")

def listar_libros(libros):
    """
    Muestra en pantalla el catálogo completo recorriendo la lista.
    """
    print("\n--- 📋 CATÁLOGO DE LIBROS ---")
    if not libros:
        print("No hay libros registrados en el catálogo.")
        return
        
    for l in libros:
        print(f"ID: {l['IDLibro']} | ISBN: {l['ISBN']} | Título: {l['Titulo']} | Autor: {l['Autor']} | Stock: {l['Cantidad']}")
        