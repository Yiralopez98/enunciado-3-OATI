# Sistema de Gestión de Ventas

Este es un sistema de gestión de ventas desarrollado en Python. Permite gestionar consumidores, productos y órdenes de compra.

## Estructura del proyecto
- `app/`: Contiene los archivos de código fuente de la aplicación.
- `database/`: Contiene el script para crear la base de datos.

## Requisitos
- Python 3.x
- MySQL Server
- XAMPP (opcional, para gestionar MySQL)

## Instalación
1. Clona o descarga este repositorio.
2. Instala las dependencias necesarias con `pip install mysql-connector-python`.
3. Ejecuta el script `create_database.py` en el directorio `database/` para crear la base de datos.

## Base de datos
-- Crear la base de datos
CREATE DATABASE gestion_pedidos;

-- Usar la base de dato
USE gestion_pedidos;

-- Crear la tabla para los consumidores
CREATE TABLE Consumidores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(15)
);

-- Crear la tabla para los productos detallados
CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100),
    precio DECIMAL(10, 2),
    cantidad_en_stock INT
);

-- Crear la tabla para las ordenes
CREATE TABLE Ordenes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consumidor_id INT,
    FOREIGN KEY (consumidor_id) REFERENCES Consumidores(id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla para los productos en una orden
CREATE TABLE Orden_Productos (
    orden_id INT,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (orden_id) REFERENCES Ordenes(id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);
