from usuarios import registrar_usuario, iniciar_sesion
from roles import cambiar_rol_usuario
from dispositivos import agregar_dispositivo, modificar_dispositivo, gestionar_dispositivos, dispositivos
from automatizacion import alternar_luces, modo_desayuno
from utilidades import mostrar_detalles_dispositivos

# Menú exclusivo para administradores
def menu_admin(usuario):
    while True:
        print("\nMenú de Administrador")
        print("1. Gestión de dispositivos")
        print("2. Registrar nuevo usuario")
        print("3. Cambiar rol de usuario")
        print("4. Cerrar sesión")
        print("5. Apagar programa")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Permite agregar, modificar o ver dispositivos
            gestionar_dispositivos()
        elif opcion == "2":
            # Permite registrar un nuevo usuario en el sistema
            registrar_usuario()
        elif opcion == "3":
            # Cambia el rol de un usuario existente
            cambiar_rol_usuario(usuario)
        elif opcion == "4":
            # Sale del menú de administrador y vuelve al login
            return  
        elif opcion == "5":
            # Termina el programa completamente
            exit()

# Menú para usuarios estándar (no administradores)
def menu_usuario_estandar(usuario):
    while True:
        print("\nMenú de Usuario Estándar")
        print("1. Consultar dispositivos")
        print("2. Activar/Desactivar luces")
        print("3. Activar modo desayuno")
        print("4. Cerrar sesión")
        print("5. Apagar programa")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Muestra todos los dispositivos registrados
            mostrar_detalles_dispositivos(dispositivos)
        elif opcion == "2":
            # Permite encender o apagar todas las luces
            alternar_luces()
        elif opcion == "3":
            # Activa el modo desayuno (enciende luces de cocina y cafetera)
            modo_desayuno()
        elif opcion == "4":
            # Sale del menú de usuario y vuelve al login
            return
        elif opcion == "5":
            # Termina el programa completamente
            exit()

# Función principal que inicia el programa
def ejecutar_programa():
    registrar_usuario()  # Si no hay usuarios, pide registrar el primero (admin)
    while True:
        usuario = iniciar_sesion()  # Solicita login
        if usuario:
            if usuario.role == "admin":
                menu_admin(usuario)  # Si es admin, muestra menú de admin
            else:
                menu_usuario_estandar(usuario)  # Si no, menú de usuario estándar

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_programa()