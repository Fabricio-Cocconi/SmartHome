# 🏠 SmartHome Solutions – Proyecto Integrador

Este proyecto forma parte del Módulo Programador 2025 y propone el desarrollo de una solución orientada a objetos para gestionar dispositivos inteligentes en el hogar. La aplicación permite registrar usuarios, controlar dispositivos (como luces, cámaras y electrodomésticos) y automatizar funciones del hogar mediante una interfaz modular, ética y segura.

---

## 📌 Descripción del Proyecto

La empresa ficticia **SmartHome Solutions** ha contratado al equipo para crear una plataforma que permita:
- Registrar usuarios y gestionar su información.
- Agregar, buscar, listar y eliminar dispositivos inteligentes por usuario.
- Consultar el estado en tiempo real de cada dispositivo.
- Aplicar reglas automáticas como encender luces o activar cámaras.
- Seguir principios del **AWS Well-Architected Framework** (seguridad, fiabilidad, eficiencia y sostenibilidad).
- Considerar la privacidad de datos personales recolectados en el hogar.

Como parte de la primera entrega perteneciente a la evidencia de aprendizaje 2 es solo una version beta donde solo podemos agregar dispositivos y prender luces
---

## 🧱 Arquitectura del Proyecto

El sistema está diseñado de forma modular y extensible:
- **Lenguaje:** Python
- **Paradigma:** Programación Orientada a Objetos (POO)
- **Estructura modular:** separación por archivos y funciones
- **Base de datos:** diseñada con un DER lógico que asocia usuarios, casas y dispositivos
- **Automatización:** activación automática de acciones según reglas simples

---

## 🗃️ Modelo de Base de Datos (resumen del DER)

Las entidades definidas para el modelo relacional del sistema son:

- **Usuario** (`nombre`, `edad`, `email`, `contraseña`)
- **Casa** (`dirección`, `propietario`)
- **Electrodoméstico** (`tipo`, `marca`, `modelo`, `estado`)
- **Modo** (`fecha_hora`, `estado`, `usuario`, `electrodoméstico`)
- **Permiso** (`usuario`, `nivel_acceso`)

**Relaciones principales:**
- Un usuario puede tener varias casas.
- Una casa contiene múltiples electrodomésticos.
- Un usuario puede controlar múltiples dispositivos.
- Cada electrodoméstico registra estados a lo largo del tiempo.
- Los permisos definen qué puede hacer cada usuario sobre los dispositivos.

📎 El DER fue elaborado en Lucidchart y puede consultarse aquí:  
https://lucid.app/lucidchart/67dfc60a-19e9-41ff-8fb7-88316b902f8b

---

## 🛡️ Política de Privacidad y Ética Profesional

El sistema SmartHome cumple con normativas de protección de datos y aplica buenas prácticas éticas:

### 🔐 Datos recolectados:
- Identificación: nombre, correo electrónico, contraseña
- Ubicación: dirección de la vivienda
- Dispositivos: tipo, uso y estado de electrodomésticos
- Historial: registros de uso por el usuario

### 🎯 Finalidad del tratamiento:
- Garantizar acceso seguro
- Administrar dispositivos de forma personalizada
- Automatizar tareas del hogar
- Cumplir con regulaciones legales

### 🛠️ Medidas de seguridad:
- Encriptación de datos almacenados y transmitidos
- Autenticación segura y control de accesos
- Auditorías regulares y monitoreo de actividad

### 👤 Derechos de los usuarios:
- Acceder, corregir, eliminar o restringir sus datos
- Contactar a soporte en: `privacidad@smarthome.com.ar`

### 🧑‍🤝‍🧑 Plan de gestión ética:
- Roles asignados: gerente de privacidad, desarrolladores, analistas de datos
- Evaluación periódica de políticas
- Revisión normativa anual
- Formación continua sobre protección de datos

---

## 📚 Funcionalidades Implementadas (Fase 1)

- Agregar, listar, buscar y eliminar dispositivos inteligentes
- Automatización simple: encender luces si están apagadas
- Estructura lista para escalar con persistencia y más automatizaciones

---

## ✍️ Créditos

Proyecto desarrollado por:

- Fabricio Andres Cocconi Huenz 
- Agustina Gonzalez Carnero
- Juan Ignacio Angel Llampa
- Ana Rocio Merlo
- Joaquin Quiroga Varela
- Melisa Yohana Guzmán

Como parte de la **Evidencia 2 del Módulo Programador – Proyecto Integrador 2025**.
