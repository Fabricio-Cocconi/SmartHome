# core/automatizacion.py

class ReglaAutomatizacion:
    def __init__(self, funcion_condicion, funcion_accion, descripcion=""):
        """
        Inicializa una regla de automatización.

        :param funcion_condicion: Función que evalúa si se cumple la condición.
        :param funcion_accion: Función que ejecuta la acción si la condición se cumple.
        :param descripcion: Descripción de la regla de automatización.
        """
        self.funcion_condicion = funcion_condicion
        self.funcion_accion = funcion_accion
        self.descripcion = descripcion

    def evaluar(self):
        """
        Evalúa la condición y ejecuta la acción si se cumple.
        """
        if self.funcion_condicion():
            print(f"⚙️ Automatización activada: {self.descripcion}")
            self.funcion_accion()
        else:
            print(f"🔁 Condición no cumplida: {self.descripcion}")
