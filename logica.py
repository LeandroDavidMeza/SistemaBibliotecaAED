# Definición estricta de las estructuras de datos
CAMPOS_LIBROS = ["IDLibro", "Titulo", "Autor", "Disponibilidad"]
CAMPOS_USUARIOS = ["IDUsuario", "DNI", "Nombre", "Apellido", "Email", "Telefono"]
CAMPOS_PRESTAMOS = ["IDPrestamo", "IDLibro", "IDUsuario", "FechaSalida", "FechaDevolucionPactada", "FechaDevolucionReal", "Estado"]

def crear_libro(id_libro, titulo, autor, disponibilidad="Si"):
    """
    Retorna un diccionario con la estructura de un libro.
    Por defecto, un libro nuevo ingresa como disponible.
    """
    return {
        "IDLibro": id_libro,
        "Titulo": titulo,
        "Autor": autor,
        "Disponibilidad": disponibilidad
    }

def crear_usuario(id_usuario, dni, nombre, apellido, email, telefono):
    """
    Retorna un diccionario con la estructura de un usuario.
    """
    return {
        "IDUsuario": id_usuario,
        "DNI": dni,
        "Nombre": nombre,
        "Apellido": apellido,
        "Email": email,
        "Telefono": telefono
    }
def crear_prestamo(id_prestamo, id_libro, id_usuario, fecha_salida, fecha_pactada):
    return {
        "IDPrestamo": id_prestamo,
        "IDLibro": id_libro,
        "IDUsuario": id_usuario,
        "FechaSalida": fecha_salida,
        "FechaDevolucionPactada": fecha_pactada,
        "FechaDevolucionReal": "N/A",
        "Estado": "Activo"
    }

def registrar_prestamo_sistema(usuarios, libros, prestamos):
    print("\n[Nuevo Préstamo]")
    id_usuario = input("ID del Usuario (Socio): ")
    
    # Validamos si existe el usuario
    usuario_existe = False
    for u in usuarios:
        if u["IDUsuario"] == id_usuario:
            usuario_existe = True
            break
    if not usuario_existe:
        print("❌ Error: El ID de usuario no existe.")
        return
    
    id_libro = input("ID del Libro a prestar: ")
    
    # Validamos libro y disponibilidad
    libro_encontrado = None
    for l in libros:
        if l["IDLibro"] == id_libro:
            libro_encontrado = l
            break
            
    if libro_encontrado is None:
        print("❌ Error: El ID del libro no existe.")
    elif libro_encontrado["Disponibilidad"] == "No":
        print("❌ Error: El libro ya está prestado.")
    else:
        id_prestamo = f"P-{len(prestamos) + 1}"
        f_salida = input("Fecha de salida (ej: 02/07): ")
        f_pactada = input("Fecha de devolución pactada (ej: 09/07): ")
        
        nuevo_p = crear_prestamo(id_prestamo, id_libro, id_usuario, f_salida, f_pactada)
        prestamos.append(nuevo_p)
        
        libro_encontrado["Disponibilidad"] = "No"
        print(f"✔️ ¡Préstamo aprobado con código {id_prestamo}!")

def registrar_devolucion_sistema(libros, prestamos):
    print("\n[Registrar Devolución]")
    id_p = input("Ingrese el ID del Préstamo (ej: P-1): ")
    
    prestamo_encontrado = None
    for p in prestamos:
        if p["IDPrestamo"] == id_p and p["Estado"] == "Activo":
            prestamo_encontrado = p
            break
            
    if prestamo_encontrado is None:
        print("❌ Error: No se encontró un préstamo activo con ese ID.")
    else:
        f_real = input("Ingrese la fecha real de devolución (ej: 12/07): ")
        dias_demora = int(input("Días de demora (0 si entregó a tiempo): "))
        
        prestamo_encontrado["FechaDevolucionReal"] = f_real
        prestamo_encontrado["Estado"] = "Devuelto"
        
        for l in libros:
            if l["IDLibro"] == prestamo_encontrado["IDLibro"]:
                l["Disponibilidad"] = "Si"
                break
                
        if dias_demora > 0:
            monto_multa = dias_demora * 500
            print(f"⚠️ ¡Atención! El libro tiene {dias_demora} días de demora.")
            print(f"💰 Monto de la multa a pagar: ${monto_multa}")
        else:
            print("✔️ ¡Excelente! Devuelto a tiempo sin multas.")
            
    def listar_prestamos(prestamos):
        print("\n--- Lista de Préstamos ---")
        if len(prestamos) == 0:
            print("No hay préstamos registrados en el sistema.")
            return
        for p in prestamos:
            print(f"Código: {p['IDPrestamo']} | Libro ID: {p['IDLibro']} | Usuario ID: {p['IDUsuario']} | Estado: {p['Estado']}")
        