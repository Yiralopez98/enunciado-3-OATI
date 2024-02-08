import mysql.connector

from consumidor import Consumidor
from producto import Producto
from orden import Orden

class Sistema:
    def __init__(self):
        self.consumidores = []
        self.productos = []
        self.ordenes = []

    def conectar_mysql(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="gestion_pedidos"
        )
        self.cursor = self.connection.cursor()

    def desconectar_mysql(self):
        self.cursor.close()
        self.connection.close()

    def agregar_consumidor(self, consumidor):
        self.consumidores.append(consumidor)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_orden(self, consumidor, productos):
        orden = Orden(len(self.ordenes) + 1, consumidor, productos)
        self.ordenes.append(orden)

    def eliminar_consumidor(self, consumidor):
        self.consumidores.remove(consumidor)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def eliminar_orden(self, orden):
        self.ordenes.remove(orden)

    def consultar_consumidores(self):
        for consumidor in self.consumidores:
            print(consumidor)

    def consultar_productos(self):
        for producto in self.productos:
            print(producto)

    def consultar_ordenes(self):
        for orden in self.ordenes:
            print(orden)

    def modificar_info_consumidor(self, consumidor, nueva_info):
        index = self.consumidores.index(consumidor)
        self.consumidores[index] = nueva_info

    def modificar_info_producto(self, producto, nueva_info):
        index = self.productos.index(producto)
        self.productos[index] = nueva_info
