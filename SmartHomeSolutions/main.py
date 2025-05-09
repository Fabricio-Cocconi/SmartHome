# main.py

from core.dispositivos import gestordispositivos
from core.automatizacion import ReglaAutomatizacion

def main():
    gestor = gestordispositivos()

    # Automatización: si hay una luz apagada, encenderla automáticamente
    def condicion():
        return any(d.tipo.lower() == "luz" and d.estado == "apagado" for d in gestor.dispositivos)

    def accion():
        for d in gestor.dispositivos:
            if d.tipo.lower() == "luz" and d.estado == "apagado":
                d.encender()

    regla = ReglaAutomatizacion(condicion, accion, "Encender luces si están apagadas")

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
            gestor.listar_dispositivos()
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            gestor.buscar_dispositivo(nombre)
        elif opcion == "4":
            nombre = input("Nombre del dispositivo a eliminar: ").strip()
            gestor.eliminar_dispositivo(nombre)
        elif opcion == "5":
            regla.evaluar()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
