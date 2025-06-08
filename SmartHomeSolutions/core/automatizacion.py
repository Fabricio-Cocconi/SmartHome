from dispositivos import dispositivos

# Esta función alterna el estado de todas las luces.
# Si todas están encendidas, las apaga. Si hay alguna apagada, las enciende todas.
def alternar_luces():
    luces = [d for d in dispositivos if d.tipo == "luz"]
    if not luces:
        print("No se encuentran luces disponibles para automatización.")
        return

    # Verificamos si todas las luces están encendidas
    luces_encendidas = all(luz.estado for luz in luces)

    if luces_encendidas:
        print("\nApagando luces:")
        for luz in luces:
            luz.estado = False
            print(f"{luz.nombre} - Apagado")
    else:
        print("\nEncendiendo luces:")
        for luz in luces:
            luz.estado = True
            print(f"{luz.nombre} - Encendido")

# Esta función activa el "modo desayuno":
# Enciende todas las luces que tengan "cocina" en su nombre y todas las cafeteras.
def modo_desayuno():
    # Buscamos luces que sean de la cocina
    luces_cocina = [d for d in dispositivos if d.tipo == "luz" and "cocina" in d.nombre.lower()]
    # Buscamos todas las cafeteras
    cafeteras = [d for d in dispositivos if d.tipo == "cafetera"]

    # Si no hay luces de cocina ni cafeteras, avisamos al usuario
    if not luces_cocina and not cafeteras:
        print("No hay luces de cocina ni cafetera registradas.")
        return

    # Encendemos todas las luces de la cocina
    for luz in luces_cocina:
        luz.estado = True
        print(f"Luz '{luz.nombre}' - Encendida")

    # Encendemos todas las cafeteras
    for cafetera in cafeteras:
        cafetera.estado = True
        print(f"Cafetera '{cafetera.nombre}' - Encendida")

    print("¡Modo desayuno activado!")