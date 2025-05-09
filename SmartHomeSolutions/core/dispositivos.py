# core/dispositivos.py

class Dispositivo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"
        print(f"💡 {self.nombre} ha sido encendido.")

    def apagar(self):
        self.estado = "apagado"
        print(f"💡 {self.nombre} ha sido apagado.")

    def __str__(self):
        return f"{self.tipo} - {self.nombre} ({self.estado})"


class gestordispositivos:
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, nombre, tipo):
        dispositivo = Dispositivo(nombre, tipo)
        self.dispositivos.append(dispositivo)
        print("✅ Dispositivo agregado.")

    def listar_dispositivos(self):
        if not self.dispositivos:
            print("📭 No hay dispositivos.")
        else:
            for i, dispositivo in enumerate(self.dispositivos, 1):
                print(f"{i}. {dispositivo}")

    def buscar_dispositivo(self, nombre):
        resultados = [d for d in self.dispositivos if d.nombre.lower() == nombre.lower()]
        if resultados:
            for d in resultados:
                print(f"🔍 Encontrado: {d}")
        else:
            print("❌ Dispositivo no encontrado.")

    def eliminar_dispositivo(self, nombre):
        original = len(self.dispositivos)
        self.dispositivos = [d for d in self.dispositivos if d.nombre.lower() != nombre.lower()]
        if len(self.dispositivos) < original:
            print("🗑️ Dispositivo eliminado.")
        else:
            print("❌ Dispositivo no encontrado.")

