# Esta clase representa a un usuario del sistema, con su nombre, contraseña y rol (admin o estándar)
class Usuario:
    def __init__(self, username, password, role="estándar"):
        self.username = username
        self.password = password
        self.role = role

# Lista global donde se guardan todos los usuarios registrados
usuarios = []

# Función para registrar un nuevo usuario en el sistema
def registrar_usuario():
    # Pedimos al usuario que ingrese su nombre y contraseña
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    # El primer usuario registrado será administrador, los demás serán estándar
    role = "admin" if not usuarios else "estándar"

    # Creamos el usuario y lo agregamos a la lista
    usuarios.append(Usuario(username, password, role))
    print(f"Usuario '{username}' registrado con rol '{role}'")

# Función para iniciar sesión en el sistema
def iniciar_sesion():
    # Pedimos al usuario que ingrese sus credenciales
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")

    # Buscamos un usuario que coincida con los datos ingresados
    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            print(f"Inicio de sesión exitoso. Bienvenido {username}!")
            return usuario  # Si lo encontramos, lo devolvemos

    # Si no se encuentra el usuario, mostramos un mensaje de error
    print("Error: Usuario o contraseña incorrectos.")
    return None