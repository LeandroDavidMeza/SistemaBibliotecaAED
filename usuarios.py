# Estructura homogénea requerida por la cátedra para el diccionario de usuarios
CAMPOS_USUARIOS = ["IDUsuario", "DNI", "Nombre", "Apellido", "Email", "Telefono"]

def crear_usuario(id_usuario, dni, nombre, apellido, email, telefono):
    """
    Retorna un diccionario estructurado para representar un socio/usuario.
    Mantiene las claves idénticas para toda la colección.
    """
    return {
        "IDUsuario": str(id_usuario),
        "DNI": dni,
        "Nombre": nombre,
        "Apellido": apellido,
        "Email": email,
        "Telefono": telefono
    }

def agregar_usuario(usuarios):
    """
    Registra un nuevo socio. 
    Recorre la lista buscando que el DNI no esté repetido.
    Asigna un ID incremental de forma automática.
    """
    print("\n[👤 Alta de Usuario/Socio]")
    dni = input("DNI del usuario: ").strip()
    
    # Validación elemento a elemento: buscamos si el DNI ya existe
    for u in usuarios:
        if u["DNI"] == dni:
            print("❌ Error: Ya existe un usuario registrado con ese número de DNI.")
            return # Cancelamos el alta si ya está registrado
            
    # ID automático incremental basado en la cantidad actual de usuarios registrados
    nuevo_id = len(usuarios) + 1
    
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()
    
    nuevo_u = crear_usuario(nuevo_id, dni, nombre, apellido, email, telefono)
    usuarios.append(nuevo_u)
    print(f"✔️ Usuario registrado con éxito. ID automático asignado: {nuevo_id}")

def listar_usuarios(usuarios):
    """
    Recorre y muestra en pantalla la lista de socios cargados.
    """
    print("\n--- 📋 LISTADO DE USUARIOS ---")
    if not usuarios:
        print("No hay usuarios registrados en el sistema.")
        return
        
    for u in usuarios:
        print(f"ID: {u['IDUsuario']} | DNI: {u['DNI']} | Nombre: {u['Nombre']} {u['Apellido']} | Email: {u['Email']} | Teléfono: {u['Telefono']}")
    
def buscar_usuario(usuarios, criterio):
    """
    Busca un usuario por IDUsuario o por DNI.
    Retorna el diccionario del usuario si lo encuentra, o None si no existe.
    """
    for u in usuarios:
        if u["IDUsuario"] == criterio or u["DNI"] == criterio:
            return u
    return None
        
        