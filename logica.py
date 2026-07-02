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