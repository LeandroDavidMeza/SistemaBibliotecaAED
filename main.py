from persistencia import asegurar_directorio, cargar_datos, guardar_datos
from logica import CAMPOS_LIBROS, CAMPOS_USUARIOS, CAMPOS_PRESTAMOS, crear_libro, crear_usuario

# Configuración de rutas
RUTA_DATOS = 'datos/'
ARCHIVO_LIBROS = RUTA_DATOS + 'libros.txt'
ARCHIVO_USUARIOS = RUTA_DATOS + 'usuarios.txt'
ARCHIVO_PRESTAMOS = RUTA_DATOS + 'prestamos.txt'

def menu_principal():
    """
    Punto de entrada principal de la aplicación.
    """
    # 1. Asegurar que exista la carpeta de datos
    asegurar_directorio(RUTA_DATOS)
    
    # 2. Cargar datos en memoria
    libros = cargar_datos(ARCHIVO_LIBROS, CAMPOS_LIBROS)
    usuarios = cargar_datos(ARCHIVO_USUARIOS, CAMPOS_USUARIOS)
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS, CAMPOS_PRESTAMOS)

    salir = False
    while not salir:
        print("\n--- SISTEMA DE GESTIÓN BIBLIOTECARIA ---")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Guardar cambios y Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n-- GESTIÓN DE LIBROS --")
            print("1. Agregar Libro")
            print("2. Listar Libros")
            sub_opcion = input("Seleccione una opción: ")
            
            if sub_opcion == '1':
                id_libro = input("ID del Libro: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                nuevo_libro = crear_libro(id_libro, titulo, autor)
                libros.append(nuevo_libro)
                print("Libro agregado temporalmente en memoria.")
            elif sub_opcion == '2':
                for libro in libros:
                    print(libro)
            else:
                print("Opción no válida.")

        elif opcion == '2':
            print("\n-- GESTIÓN DE USUARIOS --")
            print("1. Agregar Usuario")
            print("2. Listar Usuarios")
            sub_opcion = input("Seleccione una opción: ")
            
            if sub_opcion == '1':
                id_usuario = input("ID del Usuario: ")
                dni = input("DNI: ")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                nuevo_usuario = crear_usuario(id_usuario, dni, nombre, apellido, email, telefono)
                usuarios.append(nuevo_usuario)
                print("Usuario agregado temporalmente en memoria.")
            elif sub_opcion == '2':
                for usuario in usuarios:
                    print(usuario)
            else:
                print("Opción no válida.")

        elif opcion == '3':
            print("\n-- GESTIÓN DE PRÉSTAMOS --")
            print("1. Registrar Préstamo")
            print("2. Registrar Devolución")
            print("(Funcionalidad en desarrollo)")

        elif opcion == '4':
            # 3. Guardar todos los cambios al salir
            guardar_datos(ARCHIVO_LIBROS, libros, CAMPOS_LIBROS)
            guardar_datos(ARCHIVO_USUARIOS, usuarios, CAMPOS_USUARIOS)
            guardar_datos(ARCHIVO_PRESTAMOS, prestamos, CAMPOS_PRESTAMOS)
            print("Datos guardados exitosamente. Sistema cerrado.")
            salir = True

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()