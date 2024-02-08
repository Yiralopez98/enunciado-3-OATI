class Orden:
    def __init__(self, id, consumidor, productos):
        self.id = id
        self.consumidor = consumidor
        self.productos = productos

    def __str__(self):
        productos_str = ", ".join([str(producto) for producto in self.productos])
        return f"{self.id} - {self.consumidor} - {productos_str}"