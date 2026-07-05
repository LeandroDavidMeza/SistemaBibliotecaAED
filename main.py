from persistencia import asegurar_directorio, cargar_datos, guardar_datos
import libros as mod_libros
import usuarios as mod_usuarios
import prestamos as mod_prestamos
import estadisticas as mod_estadisticas 

# Configuración de las rutas para guardar los archivos de texto
RUTA_DATOS = 'datos/'
ARCHIVO_LIBROS = RUTA_DATOS + 'libros.txt'
ARCHIVO_USUARIOS = RUTA_DATOS + 'usuarios.txt'
ARCHIVO_PRESTAMOS = RUTA_DATOS + 'prestamos.txt'

def menu_estadisticas(libros, usuarios, prestamos):
    """Submenú de estadísticas del sistema."""
    print("\n-- 📊 ESTADÍSTICAS --")
    print("1. Estadísticas generales")
    print("2. Top 3 libros con mayor stock")
    print("3. Libros más y menos solicitados")
    print("4. Reporte de multas (total, por socio y por libro)")
    sub = input("Seleccione una opción: ").strip()

    if sub == '1':
        mod_estadisticas.mostrar_estadisticas_sistema(libros, usuarios, prestamos)
    elif sub == '2':
        mod_estadisticas.top_libros_por_stock(libros)
    elif sub == '3':
        mod_estadisticas.libros_mas_y_menos_solicitados(prestamos, libros)
    elif sub == '4':
        mod_estadisticas.mostrar_reporte_multas(prestamos, usuarios, libros)
    else:
        print("Opción no válida.")

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
        print("\n--- SISTEMA DE GESTIÓN BIBLIOTECARIA ---")
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
            else:
                print("Opción no válida.")

        elif opcion == '2':
            print("\n-- GESTIÓN DE USUARIOS --")
            print("1. Registrar Socio")
            print("2. Listar Socios")
            sub = input("Seleccione una opción: ")
            if sub == '1': 
                mod_usuarios.agregar_usuario(usuarios)
            elif sub == '2': 
                mod_usuarios.listar_usuarios(usuarios)
            else:
                print("Opción no válida.")

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
            else:
                print("Opción no válida.")

        elif opcion == '4':
            menu_estadisticas(libros, usuarios, prestamos)

        elif opcion == '5':
            guardar_datos(ARCHIVO_LIBROS, libros, mod_libros.CAMPOS_LIBROS)
            guardar_datos(ARCHIVO_USUARIOS, usuarios, mod_usuarios.CAMPOS_USUARIOS)
            guardar_datos(ARCHIVO_PRESTAMOS, prestamos, mod_prestamos.CAMPOS_PRESTAMOS)
            print("¡Cambios guardados con éxito! Sistema cerrado de forma segura.")
            salir = True
            
        else:
            print("Opción no válida. Intente nuevamente.")



if __name__ == "__main__":
    menu_principal()