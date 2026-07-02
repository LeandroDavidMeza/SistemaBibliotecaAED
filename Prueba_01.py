def mostrar_menu():
    print("\--- SISTEMA DE BIBLIOTECA ---")
    print("Seleccione el número según la acción a ejecutar")
    print("1. Registrar Préstamo")
    print("2. Registrar Devolución (Con cálculo de multa)")
    print("3. Ver Estadísticas y Caja")
    print("4. Salir")

def ejecutar_sistema():
    # --- CONTADORES Y ACUMULADORES ---
    total_prestamos = 0
    stock_libros = 5
    dinero_recaudado = 0  # Acumulador para la plata de las multas
    PRECIO_MULTA_DIARIA = 500  # Valor fijo por día de demora
    
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
            
            # --- VALIDACIÓN DE DÍAS DE DEMORA ---
            dias_demora = int(input("Ingrese los días de demora (0 si se entregó a tiempo): "))
            
            if dias_demora < 0:
                print("Error: Los días de demora no pueden ser negativos.")
            elif dias_demora > 0:
                # Calculamos la multa simple
                multa = dias_demora * PRECIO_MULTA_DIARIA
                dinero_recaudado = dinero_recaudado + multa  # Sumamos al acumulador
                print(f"¡Atención! El libro tiene {dias_demora} días de demora.")
                print(f"Monto de la multa a pagar: ${multa}")
            else:
                print("¡Perfecto! El libro fue devuelto a tiempo. Sin multa.")
            
            # En cualquier caso, el libro vuelve al stock
            stock_libros = stock_libros + 1
            print("Libro devuelto con éxito al stock.")
            
        elif opcion == "3":
            print("\n--- ESTADÍSTICAS ---")
            print(f"Cantidad total de préstamos realizados: {total_prestamos}")
            print(f"Libros disponibles actualmente: {stock_libros}")
            print(f"Total de dinero recaudado por multas: ${dinero_recaudado}")
            
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de biblioteca. Hasta luego!")
            ejecutando = False
            
        else:
            print("\nOpción inválida. Por favor, elija un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_sistema()
