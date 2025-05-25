# API REST - Módulo de Ventas

Esta API permite la gestión del módulo de ventas, incluyendo la administración de usuarios compradores, productos, carrito de compras, órdenes de despacho, validación de stock y emisión de boletas.

- Python 3.10
- Django 5.2
- Django REST Framework
- drf-yasg (Swagger)
- Docker

# Clonar repositorio

git clone https://github.com/neirafran223/API-ventas.git
cd ventas_api

# Levantar con Docker

docker-compose up --build

La API requiere autenticación con token para la mayoría de sus endpoints.

### Obtener Token (ejemplo TokenAuth)

POST /api/token/
Body:
{
"username": "usuario",
"password": "tu_contraseña"
}

Respuesta:
{
"token": "tu_token"
}

### Usar el token

Agrega el siguiente header a tus peticiones:

Authorization: Token tu_token

### 🔸 Usuarios

**POST /api/register/**  
Crear un nuevo usuario comprador.

**POST /api/login/**  
Inicia sesión y devuelve un token de autenticación.

---

### 🔸 Productos

**GET /api/productos/**  
Lista todos los productos disponibles.

**POST /api/productos/**  
Crea un nuevo producto (requiere autenticación y ser admin).

---

### 🔸 Carrito de compras

**GET /api/carrito/**  
Ver productos en el carrito del usuario autenticado.

**POST /api/carrito/agregar/**  
Agregar un producto al carrito.

**DELETE /api/carrito/eliminar/<id>/**  
Eliminar un producto del carrito.

---

### 🔸 Órdenes de despacho

**POST /api/ordenes/crear/**  
Generar una orden a partir del carrito.

---

### 🔸 Boletas

**GET /api/boletas/**  
Ver boletas del usuario autenticado.

Puedes visualizar y probar la API directamente desde el navegador:

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Desarrollado por: Francisco Neira  
Email: fr.neirat@duocuc.cl
