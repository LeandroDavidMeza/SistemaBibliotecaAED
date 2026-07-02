def mostrar_menu():
    print("\n--- SISTEMA DE BIBLIOTECA ---")
    print("1. Registrar Préstamo")
    print("2. Registrar Devolución")
    print("3. Ver Estadísticas")
    print("4. Salir")

def ejecutar_sistema():
    total_prestamos = 0
    stock_libros = 5
    
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            print("\n[Procesando Préstamo...]")
            if stock_libros > 0:
                stock_libros = stock_libros - 1
                total_prestamos = total_prestamos + 1
                print("¡Préstamo realizado con éxito!")
                print(f"Libros restantes en stock: {stock_libros}")
            else:
                print("Error: No quedan libros disponibles para prestar.")
                
        elif opcion == "2":
            print("\n[Procesando Devolución...]")
            stock_libros = stock_libros + 1
            print("Libro devuelto. ¡Gracias!")
            
        elif opcion == "3":
            print("\n--- ESTADÍSTICAS ---")
            print(f"Cantidad total de préstamos realizados: {total_prestamos}")
            print(f"Libros disponibles actualmente: {stock_libros}")
            
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de biblioteca. Hasta luego!")
            ejecutando = False
            
        else:
            print("\nOpción inválida. Por favor, elija un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_sistema()
    