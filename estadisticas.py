# ---------------------------------------------------------------------------
# Módulo de ESTADÍSTICAS
# Reúne en un solo lugar todas las métricas del sistema: métricas generales,
# ranking de libros por stock, libros más y menos solicitados y el reporte
# de multas (total, por socio y por libro, junto con los atrasos).
# Todas las funciones reciben las listas ya cargadas y solo las recorren.
# ---------------------------------------------------------------------------
from utilidades import dias_entre
from usuarios import buscar_usuario
from libros import buscar_libro


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


def top_libros_por_stock(libros, cantidad=3):
    """
    Recorre la lista de libros consultando la cantidad (StockTotal) de cada uno
    y muestra los 'cantidad' libros con mayor stock.
    """
    print(f"\n--- 🏆 TOP {cantidad} LIBROS CON MAYOR STOCK ---")
    if not libros:
        print("No hay libros cargados para analizar.")
        return

    # Ordenamos una copia de la lista de mayor a menor según StockTotal
    ordenados = sorted(libros, key=lambda libro: int(libro["StockTotal"]), reverse=True)

    posicion = 1
    for libro in ordenados[:cantidad]:
        print(f"{posicion}º) {libro['Titulo']} → {libro['StockTotal']} ejemplares")
        posicion += 1


def libros_mas_y_menos_solicitados(prestamos, libros, cantidad=3):
    """
    Muestra los tres libros más solicitados y los tres menos solicitados
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

    print(f"🔝 Más solicitados:")
    posicion = 1
    for id_libro, veces in pares_ordenados[:cantidad]:
        libro = buscar_libro(libros, id_libro)
        titulo = libro["Titulo"] if libro is not None else f"(ID {id_libro})"
        print(f"   {posicion}º) {titulo} → {veces} préstamo(s)")
        posicion += 1

    print(f"🔻 Menos solicitados:")
    posicion = 1
    # Los últimos de la lista ordenada, mostrados de menor a mayor
    for id_libro, veces in reversed(pares_ordenados[-cantidad:]):
        libro = buscar_libro(libros, id_libro)
        titulo = libro["Titulo"] if libro is not None else f"(ID {id_libro})"
        print(f"   {posicion}º) {titulo} → {veces} préstamo(s)")
        posicion += 1


def total_multas(prestamos):
    """
    Acumulador: recorre los préstamos y suma el monto de todas las multas.
    Devuelve el total (float) para poder reutilizarlo en otros lados.
    """
    total = 0.0
    for p in prestamos:
        total += float(p["Multa"])
    return total


def mostrar_reporte_multas(prestamos, usuarios, libros):
    """
    Reporte completo de multas: total general recaudado, desglose por socio
    y por libro, junto con la cantidad de atrasos y los días acumulados.
    """
    print("\n--- 💰 REPORTE DE MULTAS ---")
    if not prestamos:
        print("No hay préstamos para analizar.")
        return

    # Total general (reutiliza la función de arriba)
    print(f"🔹 Total recaudado en multas: ${total_multas(prestamos):.2f}")

    # Acumuladores por socio y por libro. Contamos como "atraso" toda
    # devolución cuya fecha real quedó después de la pactada.
    multa_por_usuario = {}
    dias_por_usuario = {}
    atrasos_por_usuario = {}
    multa_por_libro = {}

    for p in prestamos:
        monto = float(p["Multa"])

        # Días de atraso reales (solo si ya fue devuelto)
        dias = 0
        if p["FechaDevolucionReal"] != "N/A":
            dias = dias_entre(p["FechaDevolucionPactada"], p["FechaDevolucionReal"])
            if dias < 0:
                dias = 0

        if monto > 0 or dias > 0:
            uid = p["IDUsuario"]
            lid = p["IDLibro"]
            multa_por_usuario[uid] = multa_por_usuario.get(uid, 0.0) + monto
            dias_por_usuario[uid] = dias_por_usuario.get(uid, 0) + dias
            atrasos_por_usuario[uid] = atrasos_por_usuario.get(uid, 0) + 1
            multa_por_libro[lid] = multa_por_libro.get(lid, 0.0) + monto

    # Desglose por socio
    print("\n👤 Multas por socio:")
    if not multa_por_usuario:
        print("   (Ningún socio tiene atrasos registrados.)")
    else:
        for uid in multa_por_usuario:
            u = buscar_usuario(usuarios, uid)
            nombre = f"{u['Nombre']} {u['Apellido']}" if u is not None else f"(ID {uid})"
            print(f"   {nombre}: ${multa_por_usuario[uid]:.2f} "
                  f"({atrasos_por_usuario[uid]} atraso/s, {dias_por_usuario[uid]} día/s)")

    # Desglose por libro
    print("\n📚 Multas por libro:")
    if not multa_por_libro:
        print("   (Ningún libro generó multas.)")
    else:
        for lid in multa_por_libro:
            libro = buscar_libro(libros, lid)
            titulo = libro["Titulo"] if libro is not None else f"(ID {lid})"
            print(f"   {titulo}: ${multa_por_libro[lid]:.2f}")