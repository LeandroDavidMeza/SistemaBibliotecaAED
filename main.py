from persistencia import asegurar_directorio, cargar_datos, guardar_datos
# Importamos los nuevos archivos/módulos que vamos a crear en los próximos pasos
import libros as mod_libros
import usuarios as mod_usuarios
import prestamos as mod_prestamos

# Configuración de las rutas para guardar los archivos de texto
RUTA_DATOS = 'datos/'
ARCHIVO_LIBROS = RUTA_DATOS + 'libros.txt'
ARCHIVO_USUARIOS = RUTA_DATOS + 'usuarios.txt'
ARCHIVO_PRESTAMOS = RUTA_DATOS + 'prestamos.txt'

def menu_principal():
    """
    Punto de entrada principal de la aplicación.
    Controla el menú global y delega las acciones a cada módulo.
    """
    # 1. Asegurar que exista la carpeta 'datos/' en la computadora
    asegurar_directorio(RUTA_DATOS)
    
    # 2. Cargar los datos desde los archivos .txt usando los campos de cada módulo
    libros = cargar_datos(ARCHIVO_LIBROS, mod_libros.CAMPOS_LIBROS)
    usuarios = cargar_datos(ARCHIVO_USUARIOS, mod_usuarios.CAMPOS_USUARIOS)
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS, mod_prestamos.CAMPOS_PRESTAMOS)

    salir = False
    while not salir:
        print("\n--- SISTEMA DE GESTIÓN BIBLIOTECARIA (REFACTORIZADO) ---")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Ver Estadísticas Generales")
        print("5. Guardar cambios y Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n-- GESTIÓN DE LIBROS --")
            print("1. Agregar Libro (Control de Stock e ISBN)")
            print("2. Listar Catálogo")
            sub = input("Seleccione una opción: ")
            if sub == '1': 
                mod_libros.agregar_libro(libros)
            elif sub == '2': 
                mod_libros.listar_libros(libros)

        elif opcion == '2':
            print("\n-- GESTIÓN DE USUARIOS --")
            print("1. Registrar Socio")
            print("2. Listar Socios")
            sub = input("Seleccione una opción: ")
            if sub == '1': 
                mod_usuarios.agregar_usuario(usuarios)
            elif sub == '2': 
                mod_usuarios.listar_usuarios(usuarios)

        elif opcion == '3':
            print("\n-- GESTIÓN DE PRÉSTAMOS --")
            print("1. Registrar Préstamo")
            print("2. Registrar Devolución")
            print("3. Listar Historial de Préstamos")
            sub = input("Seleccione una opción: ")
            if sub == '1': 
                mod_prestamos.registrar_prestamo_sistema(usuarios, libros, prestamos)
            elif sub == '2': 
                mod_prestamos.registrar_devolucion_sistema(libros, prestamos)
            elif sub == '3': 
                mod_prestamos.listar_prestamos(prestamos)

        elif opcion == '4':
            # Delegamos el módulo de estadísticas a prestamos.py
            mod_prestamos.mostrar_estadisticas_sistema(libros, usuarios, prestamos)

        elif opcion == '5':
            # Guardar todos los cambios definitivos al cerrar el programa
            guardar_datos(ARCHIVO_LIBROS, libros, mod_libros.CAMPOS_LIBROS)
            guardar_datos(ARCHIVO_USUARIOS, usuarios, mod_usuarios.CAMPOS_USUARIOS)
            guardar_datos(ARCHIVO_PRESTAMOS, prestamos, mod_prestamos.CAMPOS_PRESTAMOS)
            print("¡Cambios guardados con éxito! Sistema cerrado de forma segura.")
            salir = True
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()