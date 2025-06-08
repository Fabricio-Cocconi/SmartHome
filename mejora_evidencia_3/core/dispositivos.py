from utilidades import mostrar_detalles_dispositivos

# Definimos la clase Dispositivo, que representa cualquier aparato del sistema
class Dispositivo:
    def __init__(self, nombre, tipo, estado=False):
        self.nombre = nombre  # Nombre identificador del dispositivo
        self.tipo = tipo      # Tipo: luz, cafetera o cámara
        self.estado = estado  # Estado: encendido (True) o apagado (False)

    def cambiar_estado(self, encender=True):
        # Cambia el estado del dispositivo (encender o apagar)
        self.estado = encender

# Lista global donde se guardan todos los dispositivos registrados
dispositivos = []

# Permite al usuario agregar un nuevo dispositivo al sistema
def agregar_dispositivo():
    print("\nAgregar dispositivo")
    nombre = input("Nombre del dispositivo: ")
    tipo = input("Tipo de dispositivo (luz/cafetera/cámara): ").lower()
    # Solo aceptamos los tipos válidos
    if tipo not in ["luz", "cafetera", "cámara"]:
        print("Tipo no válido.")
        return
    # Creamos y guardamos el nuevo dispositivo
    dispositivos.append(Dispositivo(nombre, tipo))
    print(f"Dispositivo '{nombre}' de tipo '{tipo}' agregado.")

# Permite modificar el nombre o tipo de un dispositivo ya existente
def modificar_dispositivo():
    print("\nModificar dispositivo")
    nombre = input("Nombre del dispositivo a modificar: ")
    for dispositivo in dispositivos:
        if dispositivo.nombre == nombre:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_tipo = input("Nuevo tipo (luz/cafetera/cámara): ").lower()
            if nuevo_tipo not in ["luz", "cafetera", "cámara"]:
                print("Tipo no válido.")
                return
            dispositivo.nombre = nuevo_nombre
            dispositivo.tipo = nuevo_tipo
            print("Dispositivo modificado.")
            return
    print("Dispositivo no encontrado.")

# Enciende o apaga todos los dispositivos de un tipo específico
def cambiar_estado_dispositivos(tipo, encender):
    for dispositivo in dispositivos:
        if dispositivo.tipo == tipo:
            dispositivo.cambiar_estado(encender)
            estado_actual = "Encendido" if encender else "Apagado"
            print(f"{dispositivo.nombre} - {estado_actual}")

# Menú para automatizaciones: permite controlar varios dispositivos a la vez
def menu_automatizacion():
    while True:
        print("\nAutomatización")
        print("1. Encender luces")
        print("2. Encender cafeteras")
        print("3. Encender cámaras")
        print("4. Apagar luces")
        print("5. Apagar cafeteras")
        print("6. Apagar cámaras")
        print("7. Activar modo desayuno")  # Automatización especial
        print("8. Volver al menú anterior")

        opcion = input("Seleccione una opción (1-8): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 8:
            opcion = int(opcion)
        else:
            print("Por favor, ingrese un número válido entre 1 y 8.")
            continue

        if opcion == 1:
            # Enciende todas las luces
            cambiar_estado_dispositivos("luz", True)
        elif opcion == 2:
            # Enciende todas las cafeteras
            cambiar_estado_dispositivos("cafetera", True)
        elif opcion == 3:
            # Enciende todas las cámaras
            cambiar_estado_dispositivos("cámara", True)
        elif opcion == 4:
            # Apaga todas las luces
            cambiar_estado_dispositivos("luz", False)
        elif opcion == 5:
            # Apaga todas las cafeteras
            cambiar_estado_dispositivos("cafetera", False)
        elif opcion == 6:
            # Apaga todas las cámaras
            cambiar_estado_dispositivos("cámara", False)
        elif opcion == 7:
            # Activa el modo desayuno (enciende luces de cocina y cafetera)
            from automatizacion import modo_desayuno
            modo_desayuno()
        elif opcion == 8:
            # Sale del menú de automatización
            break

# Menú principal para gestionar dispositivos: agregar, modificar, automatizar, ver detalles o salir
def gestionar_dispositivos():
    while True:
        print("\nGestión de Dispositivos")
        print("1. Agregar dispositivo")
        print("2. Modificar dispositivo")
        print("3. Automatización")
        print("4. Mostrar detalles de dispositivos")
        print("5. Volver al menú anterior")
        
        opcion = input("Seleccione una opción (1-5): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            opcion = int(opcion)
        else:
            print("Por favor, ingrese un número válido entre 1 y 5.")
            continue

        if opcion == 1:
            # Agrega un nuevo dispositivo
            agregar_dispositivo()
        elif opcion == 2:
            # Modifica un dispositivo existente
            modificar_dispositivo()
        elif opcion == 3:
            # Accede al menú de automatización
            menu_automatizacion()
        elif opcion == 4:
            # Muestra todos los dispositivos y su estado
            print("\nDetalles de Dispositivos:")
            mostrar_detalles_dispositivos(dispositivos)
        elif opcion == 5:
            # Sale de la gestión de dispositivos
            break