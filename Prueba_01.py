# --- BASES DE DATOS GLOBALES (DICCIONARIOS) ---
# Empezamos con algunos datos precargados para poder probar de entrada
diccionario_usuarios = {
    "123": {"nombre": "Ramiro Ponzio", "comision": "ISI"},
    "456": {"nombre": "Victoria", "comision": "ISI"}
}

diccionario_libros = {
    "L01": {"titulo": "El Aleph", "stock": 3, "pedidos": 0},
    "L02": {"titulo": "Don Quijote", "stock": 2, "pedidos": 0}
}

diccionario_prestamos = {}
contador_prestamos = 1


def mostrar_menu():
    print("\n=========================================")
    print("      SISTEMA DE BIBLIOTECA - ISI")
    print("=========================================")
    print("1. [Vicky] Registrar Nuevo Usuario")
    print("2. [Ramiro] Registrar Préstamo (Enlazado)")
    print("3. Ver Todos los Préstamos Activos")
    print("4. Ver Inventario de Libros")
    print("5. Salir")
    print("=========================================")


def registrar_usuario():
    print("\n[MÓDULO: REGISTRAR NUEVO USUARIO]")
    dni = input("Ingrese el DNI del nuevo usuario: ")
    
    # Validaciones de DNI
    if not dni.isdigit():
        print("❌ Error: El DNI debe contener únicamente números.")
        return
    if dni in diccionario_usuarios:
        print("❌ Error: Ya existe un usuario registrado con ese DNI.")
        return
        
    nombre = input("Ingrese Nombre y Apellido: ")
    # Validación de Nombre vacío
    if nombre.strip() == "":
        print("❌ Error: El nombre no puede quedar vacío.")
        return
        
    comision = input("Ingrese la comisión (ej: ISI): ")
    
    # Guardamos en el diccionario de usuarios
    diccionario_usuarios[dni] = {
        "nombre": nombre,
        "comision": comision
    }
    print(f"✔️ ¡Usuario '{nombre}' registrado con éxito!")


def registrar_prestamo():
    global contador_prestamos # Para poder modificar el contador que está afuera
    
    print("\n[MÓDULO: REGISTRAR NUEVO PRÉSTAMO]")
    dni = input("Ingrese el DNI del usuario que solicita el libro: ")
    
    # VALIDACIÓN: ¿El DNI existe en el diccionario de Vicky?
    if dni not in diccionario_usuarios:
        print("❌ Error: El DNI ingresado no corresponde a un usuario registrado.")
        print("Por favor, registre al usuario primero (Opción 1).")
        return
        
    id_libro = input("Ingrese el ID del libro (L01 / L02): ")
    
    # VALIDACIÓN: ¿El libro existe en el inventario?
    if id_libro not in diccionario_libros:
        print("❌ Error: El código de libro no existe.")
        return
        
    # VALIDACIÓN: ¿Hay stock disponible?
    if diccionario_libros[id_libro]["stock"] <= 0:
        print(f"❌ Error: No queda stock disponible de '{diccionario_libros[id_libro]['titulo']}'.")
        return
    
    # SI TODO ESTÁ BIEN, ENLAZAMOS LOS DICCIONARIOS
    id_prestamo = f"P-{contador_prestamos}"
    
    # Guardamos solo el DNI y el ID del libro (Las relaciones)
    diccionario_prestamos[id_prestamo] = {
        "dni_usuario": dni,
        "id_libro": id_libro
    }
    
    # Actualizamos el stock del libro pedido
    diccionario_libros[id_libro]["stock"] -= 1
    diccionario_libros[id_libro]["pedidos"] += 1
    contador_prestamos += 1
    
    # Buscamos el nombre real para el cartel de éxito
    nombre_alumno = diccionario_usuarios[dni]["nombre"]
    titulo_libro = diccionario_libros[id_libro]["titulo"]
    
    print(f"✔️ ¡Préstamo {id_prestamo} aprobado! '{nombre_alumno}' se llevó '{titulo_libro}'.")


def mostrar_prestamos():
    print("\n[MÓDULO: PRÉSTAMOS ACTIVOS EN EL SISTEMA]")
    if len(diccionario_prestamos) == 0:
        print("No hay préstamos registrados en este momento.")
        return
        
    for cod_p, datos in diccionario_prestamos.items():
        # Cruzamos los datos usando los enlaces
        usuario_real = diccionario_usuarios[datos["dni_usuario"]]["nombre"]
        libro_real = diccionario_libros[datos["id_libro"]]["titulo"]
        print(f"📋 Código: {cod_p} | Alumno: {usuario_real} | Libro: {libro_real}")


def mostrar_inventario():
    print("\n[MÓDULO: INVENTARIO DE LIBROS]")
    for cod_l, datos in diccionario_libros.items():
        print(f"📖 ID: {cod_l} | Título: {datos['titulo']} | Stock: {datos['stock']} | Total Pedidos: {datos['pedidos']}")


# --- FUNCIÓN PRINCIPAL MAIN (EL CEREBRO DEL PROGRAMA) ---
def main():
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            mostrar_prestamos()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Saliendo del programa...")
            ejecutando = False
        else:
            print("\n❌ Opción inválida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    main()
    