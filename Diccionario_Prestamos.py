Diccionario_Prestamos = {}
def mostrar_menu():
    print("\n--- SISTEMA DE BIBLIOTECA CENTRALIZADO ---")
    print("1. Registrar nuevo Préstamo (Enlazado)")
    print("2. Ver todos los Préstamos activos")
    print("3. Ver Inventario de Libros")
    print("4. Salir")

def ejecutar_sistema():
    # --- NUESTRAS TRES BASES DE DATOS (DICCIONARIOS) ---
    
    # Usuarios precargados (Clave: DNI)
    diccionario_usuarios = {
        "123": {"nombre": "Ramiro Ponzio", "comision": "ISI"},
        "456": {"nombre": "Juan Pérez", "comision": "ISI"}
    }
    
    # Libros precargados (Clave: ID de libro)
    diccionario_libros = {
        "L01": {"titulo": "El Aleph", "stock": 3, "pedidos": 0},
        "L02": {"titulo": "Don Quijote", "stock": 2, "pedidos": 0}
    }
    
    # Préstamos (Clave: ID de préstamo) -> Acá se enlazan los otros dos
    diccionario_prestamos = {}
    
    contador_prestamos = 1
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n[Nuevo Préstamo Enlazado]")
            dni = input("Ingrese el DNI del usuario: ")
            
            # VALIDACIÓN: ¿Existe el usuario?
            if dni not in diccionario_usuarios:
                print("Error: El usuario no está registrado en el sistema.")
                continue # Esto vuelve al menú principal sin romper nada
                
            id_libro = input("Ingrese el ID del libro (L01 o L02): ")
            
            # VALIDACIÓN: ¿Existe el libro?
            if id_libro not in diccionario_libros:
                print("Error: El código de libro no existe.")
                continue
                
            # VALIDACIÓN: ¿Hay stock disponible?
            if diccionario_libros[id_libro]["stock"] <= 0:
                print(f"Error: No queda stock disponible de '{diccionario_libros[id_libro]['titulo']}'.")
                continue
            
            # SI PASÓ TODAS LAS VALIDACIONES, ENLAZAMOS:
            id_prestamo = f"P-{contador_prestamos}"
            
            # Guardamos solo las CLAVES (DNI e ID de libro)
            diccionario_prestamos[id_prestamo] = {
                "dni_usuario": dni,
                "id_libro": id_libro
            }
            
            # Actualizamos el inventario de libros (Restamos stock y sumamos contador)
            diccionario_libros[id_libro]["stock"] -= 1
            diccionario_libros[id_libro]["pedidos"] += 1
            contador_prestamos += 1
            
            print(f"¡Préstamo registrado con éxito bajo el código {id_prestamo}!")
            
        elif opcion == "2":
            print("\n--- LISTA DE PRÉSTAMOS ENLAZADOS ---")
            if len(diccionario_prestamos) == 0:
                print("No hay préstamos registrados.")
            else:
                for cod_p, datos in diccionario_prestamos.items():
                    # Buscamos los datos reales usando las claves guardadas
                    usuario_real = diccionario_usuarios[datos["dni_usuario"]]["nombre"]
                    libro_real = diccionario_libros[datos["id_libro"]]["titulo"]
                    
                    print(f"Préstamo: {cod_p} | Alumno: {usuario_real} | Libro: {libro_real}")
                    
        elif opcion == "3":
            print("\n--- INVENTARIO DE LIBROS ---")
            for cod_l, datos in diccionario_libros.items():
                print(f"ID: {cod_l} | Título: {datos['titulo']} | Stock: {datos['stock']} | Total Pedidos: {datos['pedidos']}")
                
        elif opcion == "4":
            print("\n¡Sistema cerrado con éxito!")
            ejecutando = False
            
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    ejecutar_sistema()