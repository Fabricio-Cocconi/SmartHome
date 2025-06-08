
from core.dispositivos import GestorDispositivos
from core.automatizacion import ReglaAutomatizacion

def main():
    gestor = GestorDispositivos()

    def condicion():
        """Evalúa si hay luces encendidas o apagadas y decide el cambio de estado."""
        return any(d.tipo.lower() == "luz" for d in gestor.dispositivos)

    def accion():
        """Alterna el estado de las luces (enciende si está apagada, apaga si está encendida)."""
        for dispositivo in gestor.dispositivos:
            if dispositivo.tipo.lower() == "luz":
                dispositivo.toggle()

    regla = ReglaAutomatizacion(condicion, accion, "Alternar luces encendidas/apagadas")

    while True:
        print("\n=== MENÚ ===")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Ejecutar automatización")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del dispositivo: ").strip()
            tipo = input("Tipo (Luz, Cámara, Termostato...): ").strip()
            gestor.agregar_dispositivo(nombre, tipo)
        elif opcion == "2":
            dispositivos = gestor.listar_dispositivos()
            for dispositivo in dispositivos:
                print(dispositivo)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            dispositivo = gestor.buscar_dispositivo(nombre)
            print(dispositivo if dispositivo else "❌ Dispositivo no encontrado.")
        elif opcion == "4":
            nombre = input("Nombre del dispositivo a eliminar: ").strip()
            print(gestor.eliminar_dispositivo(nombre))
        elif opcion == "5":
            regla.evaluar()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()