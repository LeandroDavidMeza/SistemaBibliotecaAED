# Estructura homogénea requerida por la cátedra para el diccionario de préstamos
CAMPOS_PRESTAMOS = ["IDPrestamo", "IDLibro", "IDUsuario", "FechaSalida", "FechaDevolucionPactada", "FechaDevolucionReal", "Estado"]

def crear_prestamo(id_prestamo, id_libro, id_usuario, fecha_salida, fecha_pactada):
    """
    Retorna un diccionario estructurado para un préstamo activo.
    Usa el año completo en las fechas y mantiene consistencia en las claves.
    """
    return {
        "IDPrestamo": str(id_prestamo),
        "IDLibro": str(id_libro),
        "IDUsuario": str(id_usuario),
        "FechaSalida": fecha_salida,
        "FechaDevolucionPactada": fecha_pactada,
        "FechaDevolucionReal": "N/A",
        "Estado": "Activo"
    }

def registrar_prestamo_sistema(usuarios, libros, prestamos):
    """
    Registra un préstamo. Valida existencia de socio, existencia de libro y stock disponible.
    Resta 1 al stock del libro si el préstamo es exitoso.
    """
    print("\n[🚀 Registrar Préstamo]")
    id_usuario = input("ID del Usuario (Socio): ").strip()
    
    # 1. Validación elemento a elemento: buscamos si el socio existe
    usuario_encontrado = False
    for u in usuarios:
        if u["IDUsuario"] == id_usuario:
            usuario_encontrado = True
            break
            
    if not usuario_encontrado:
        print("❌ Error: El ID de usuario ingresado no existe en el sistema.")
        return
        
    id_libro = input("ID del Libro a prestar: ").strip()
    
    # 2. Validación elemento a elemento: buscamos el libro en el catálogo
    libro_encontrado = None
    for l in libros:
        if l["IDLibro"] == id_libro:
            libro_encontrado = l
            break
            
    if not libro_encontrado:
        print("❌ Error: El ID del libro ingresado no existe en el catálogo.")
        return
        
    # 3. Validación de Disponibilidad basada en Cantidad (Stock)
    stock_actual = int(libro_encontrado["Cantidad"])
    if stock_actual <= 0:
        print("❌ Error: No quedan ejemplares disponibles de este libro en la estantería.")
        return
        
    # Asignación de ID automático incremental
    nuevo_id = len(prestamos) + 1
    
    # Fechas completas (Día, Mes, Año) sugeridas por el grupo
    f_salida = input("Fecha de salida (DD/MM/AAAA): ").strip()
    f_pactada = input("Fecha pactada de devolución (DD/MM/AAAA): ").strip()
    
    nuevo_p = crear_prestamo(nuevo_id, id_libro, id_usuario, f_salida, f_pactada)
    prestamos.append(nuevo_p)
    
    # Modificación del stock del libro (Resta 1 ejemplar)
    libro_encontrado["Cantidad"] = str(stock_actual - 1)
    print(f"✔️ ¡Préstamo aprobado con éxito! ID de transacción asignado: {nuevo_id}")

def registrar_devolucion_sistema(libros, prestamos):
    """
    Registra la devolución de un libro. Devuelve el ejemplar al stock
    y calcula multas si corresponde.
    """
    print("\n[🔙 Registrar Devolución]")
    id_p = input("Ingrese el ID del Préstamo a cerrar (ej: 1): ").strip()
    
    # Buscamos el préstamo activo elemento a elemento
    prestamo_encontrado = None
    for p in prestamos:
        if p["IDPrestamo"] == id_p and p["Estado"] == "Activo":
            prestamo_encontrado = p
            break
            
    if not prestamo_encontrado:
        print("❌ Error: No se encontró ningún préstamo activo registrado con ese ID.")
        return
        
    f_real = input("Fecha real de devolución (DD/MM/AAAA): ").strip()
    dias_demora = int(input("Días de demora (0 si entregó a tiempo): "))
    
    # Actualizamos el estado del préstamo
    prestamo_encontrado["FechaDevolucionReal"] = f_real
    prestamo_encontrado["Estado"] = "Devuelto"
    
    # Modificación del stock del libro (Suma 1 ejemplar devuelto)
    for l in libros:
        if l["IDLibro"] == prestamo_encontrado["IDLibro"]:
            l["Cantidad"] = str(int(l["Cantidad"]) + 1)
            break
            
    if dias_demora > 0:
        monto_multa = dias_demora * 500  # Multiplicador simple de multa
        print(f"⚠️ ¡Atención! Registro con {dias_demora} días de demora.")
        print(f"💰 Monto de la multa acumulada a pagar: ${monto_multa}")
    else:
        print("✔️ ¡Excelente! El socio devolvió el libro a tiempo y sin multas.")

def listar_prestamos(prestamos):
    """
    Recorre el historial completo de transacciones de préstamo.
    """
    print("\n--- 📋 HISTORIAL GENERAL DE PRÉSTAMOS ---")
    if not prestamos:
        print("No se registran transacciones de préstamo en el sistema.")
        return
        
    for p in prestamos:
        print(f"ID Transacción: {p['IDPrestamo']} | Libro ID: {p['IDLibro']} | Socio ID: {p['IDUsuario']} | Estado: {p['Estado']}")

def mostrar_estadisticas_sistema(libros, usuarios, prestamos):
    """
    Módulo de analítica solicitado por la cátedra. 
    Cruza los datos de las tres listas usando contadores puros.
    """
    print("\n--- 📊 ESTADÍSTICAS GENERALES DEL SISTEMA ---")
    
    # Contadores directos mediante tamaño de listas
    print(f"🔹 Cantidad total de socios registrados: {len(usuarios)}")
    print(f"🔹 Volumen histórico de préstamos realizados: {len(prestamos)}")
    
    # Contador estructurado mediante ciclo repetitivo for
    prestamos_activos = 0
    for p in prestamos:
        if p["Estado"] == "Activo":
            prestamos_activos += 1
            
    print(f"🔹 Préstamos activos circulando en la calle: {prestamos_activos}")
    
    # Acumulador del stock total de libros físicos disponibles en la biblioteca
    total_ejemplares_disponibles = 0
    for l in libros:
        total_ejemplares_disponibles += int(l["Cantidad"])
        
    print(f"🔹 Total de libros físicos disponibles en estanterías: {total_ejemplares_disponibles}")
    
    