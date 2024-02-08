class Producto:
    def __init__(self, id, descripcion, precio, cantidad_en_stock):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock

    def __str__(self):
        return f"{self.id} - {self.descripcion} - {self.precio} - {self.cantidad_en_stock}"

    def actualizar_cantidad_en_stock(self, cantidad):
        self.cantidad_en_stock += cantidad
