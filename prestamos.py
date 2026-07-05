# ---------------------------------------------------------------------------
# Módulo de PRÉSTAMOS
# Cada préstamo es un diccionario y todos comparten las mismas claves.
# Este módulo "enlaza" usuarios con libros a través de sus ID.
# ---------------------------------------------------------------------------
from utilidades import leer_texto, leer_entero, leer_fecha, generar_nuevo_id, dias_entre, leer_decimal
from usuarios import buscar_usuario
from libros import buscar_libro

CAMPOS_PRESTAMOS = [
    "IDPrestamo", "IDLibro", "IDUsuario",
    "FechaSalida", "FechaDevolucionPactada", "FechaDevolucionReal", "Estado", "Multa"
]


def crear_prestamo(id_prestamo, id_libro, id_usuario, fecha_salida, fecha_pactada):
    """Retorna un diccionario estructurado para un préstamo activo."""
    return {
        "IDPrestamo": str(id_prestamo),
        "IDLibro": str(id_libro),
        "IDUsuario": str(id_usuario),
        "FechaSalida": fecha_salida,
        "FechaDevolucionPactada": fecha_pactada,
        "FechaDevolucionReal": "N/A",
        "Estado": "Activo",
        "Multa": "0",
    }


def registrar_prestamo_sistema(usuarios, libros, prestamos):
    """
    Registra un préstamo. El socio se puede identificar por ID o por DNI,
    y el libro por ID o por ISBN. Valida que ambos existan y que haya
    stock disponible. Al aprobarse, resta 1 al stock DISPONIBLE del libro.
    """
    print("\n[🚀 Registrar Préstamo]")

    # 1. Identificar al socio (por ID o DNI) recorriendo la lista
    criterio_usuario = leer_texto("Ingrese ID o DNI del socio: ")
    usuario = buscar_usuario(usuarios, criterio_usuario)
    if usuario is None:
        print("❌ Error: no existe ningún socio con ese ID/DNI.")
        return

    # 2. Identificar el libro (por ID o ISBN) recorriendo la lista
    criterio_libro = leer_texto("Ingrese ID o ISBN del libro: ")
    libro = buscar_libro(libros, criterio_libro)
    if libro is None:
        print("❌ Error: no existe ningún libro con ese ID/ISBN.")
        return

    # 3. Validar stock disponible
    if int(libro["StockDisponible"]) <= 0:
        print(f"❌ Error: no quedan ejemplares disponibles de '{libro['Titulo']}'.")
        return

    # 4. Fechas completas con día, mes y año (validadas con try/except)
    f_salida = leer_fecha("Fecha de salida (DD/MM/AAAA): ")
    f_pactada = leer_fecha("Fecha pactada de devolución (DD/MM/AAAA): ")

    # La devolución pactada tiene que caer después de la salida
    if dias_entre(f_salida, f_pactada) <= 0:
        print("❌ Error: la fecha pactada debe ser posterior a la de salida.")
        return

    # 5. ID automático e incremental para el préstamo
    nuevo_id = generar_nuevo_id(prestamos, "IDPrestamo")
    nuevo_p = crear_prestamo(nuevo_id, libro["IDLibro"], usuario["IDUsuario"], f_salida, f_pactada)
    prestamos.append(nuevo_p)

    # 6. Restamos 1 al stock DISPONIBLE (el total no cambia)
    libro["StockDisponible"] = str(int(libro["StockDisponible"]) - 1)

    print(f"✔️ Préstamo aprobado. ID de transacción: {nuevo_id}")
    print(f"   Socio: {usuario['Nombre']} {usuario['Apellido']} | Libro: {libro['Titulo']}")


def registrar_devolucion_sistema(libros, prestamos):
    """
    Registra la devolución de un préstamo activo, suma 1 al stock DISPONIBLE
    del libro y calcula la multa si hubo demora.
    """
    print("\n[🔙 Registrar Devolución]")
    id_p = leer_texto("Ingrese el ID del préstamo a cerrar (ej: 1): ")

    # Buscamos el préstamo activo elemento a elemento
    prestamo = None
    for p in prestamos:
        if p["IDPrestamo"] == id_p and p["Estado"] == "Activo":
            prestamo = p
            break

    if prestamo is None:
        print("❌ Error: no se encontró un préstamo activo con ese ID.")
        return

    f_real = leer_fecha("Fecha real de devolución (DD/MM/AAAA): ")

    prestamo["FechaDevolucionReal"] = f_real
    prestamo["Estado"] = "Devuelto"

    # Devolvemos el ejemplar al stock disponible
    for libro in libros:
        if libro["IDLibro"] == prestamo["IDLibro"]:
            libro["StockDisponible"] = str(int(libro["StockDisponible"]) + 1)
            break

    # Multa automática: días de atraso (calculados) × costo por día (ingresado)
    dias_demora = dias_entre(prestamo["FechaDevolucionPactada"], f_real)
    if dias_demora > 0:
        costo_dia = leer_decimal(f"Se registran {dias_demora} día(s) de atraso. Costo por día: $", minimo=0)
        monto_multa = dias_demora * costo_dia
        prestamo["Multa"] = str(monto_multa)          # <-- se guarda
        print(f"⚠️ Devolución con {dias_demora} día(s) de atraso.")
        print(f"💰 Multa: {dias_demora} × ${costo_dia} = ${monto_multa}")
    else:
        prestamo["Multa"] = "0"                         # <-- devuelto a tiempo
        print("✔️ Devuelto a tiempo y sin multas.")


def listar_prestamos(prestamos):
    """Recorre y muestra el historial completo de préstamos."""
    print("\n--- 📋 HISTORIAL GENERAL DE PRÉSTAMOS ---")
    if not prestamos:
        print("No se registran préstamos en el sistema.")
        return

    for p in prestamos:
        print(
            f"ID: {p['IDPrestamo']} | Libro ID: {p['IDLibro']} | "
            f"Socio ID: {p['IDUsuario']} | Salida: {p['FechaSalida']} | "
            f"Estado: {p['Estado']} | Multa: ${p['Multa']}"
        )


def mostrar_estadisticas_sistema(libros, usuarios, prestamos):
    """Métricas generales del sistema usando contadores y acumuladores."""
    print("\n--- 📊 ESTADÍSTICAS GENERALES ---")
    print(f"🔹 Socios registrados: {len(usuarios)}")
    print(f"🔹 Préstamos históricos: {len(prestamos)}")

    # Contador con ciclo for: préstamos activos
    prestamos_activos = 0
    for p in prestamos:
        if p["Estado"] == "Activo":
            prestamos_activos += 1
    print(f"🔹 Préstamos activos (en la calle): {prestamos_activos}")

    # Acumuladores de stock total y disponible
    total_ejemplares = 0
    total_disponibles = 0
    for libro in libros:
        total_ejemplares += int(libro["StockTotal"])
        total_disponibles += int(libro["StockDisponible"])
    print(f"🔹 Stock total de ejemplares (comprados): {total_ejemplares}")
    print(f"🔹 Stock disponible en estantería ahora: {total_disponibles}")


def libros_mas_y_menos_solicitados(prestamos, libros, cantidad=3):
    """
    Muestra los los tres libros más solicitados, y los tres menos solicitados
    (incluyendo los que nunca han sido prestados).
    """
    print(f"\n--- 📈 LIBROS MÁS Y MENOS SOLICITADOS ---")
    if not prestamos:
        print("Todavía no hay préstamos para analizar.")
        return

    # Contador (diccionario) que acumula préstamos por IDLibro
    conteo = {}
    for libro in libros:                 # Arranca todo el catálogo en 0
        conteo[libro["IDLibro"]] = 0
    for p in prestamos:                  # Después suma los préstamos reales
        conteo[p["IDLibro"]] = conteo.get(p["IDLibro"], 0) + 1

    # Pasamos el contador a una lista de pares (IDLibro, cantidad_de_prestamos)
    pares = []
    for id_libro in conteo:
        pares.append((id_libro, conteo[id_libro]))

    # Ordenamos de mayor a menor según la cantidad de préstamos
    pares_ordenados = sorted(pares, key=lambda par: par[1], reverse=True)

    def titulo_de(id_libro):
        """Busca el título del libro recorriendo la lista por IDLibro."""
        for libro in libros:
            if libro["IDLibro"] == id_libro:
                return libro["Titulo"]
        return f"(ID {id_libro})"

    print(f"🔝 Más solicitados:")
    posicion = 1
    for id_libro, veces in pares_ordenados[:cantidad]:
        print(f"   {posicion}º) {titulo_de(id_libro)} → {veces} préstamo(s)")
        posicion += 1

    print(f"🔻 Menos solicitados:")
    posicion = 1
    # Los últimos de la lista ordenada, mostrados de menor a mayor
    for id_libro, veces in reversed(pares_ordenados[-cantidad:]):
        print(f"   {posicion}º) {titulo_de(id_libro)} → {veces} préstamo(s)")
        posicion += 1
