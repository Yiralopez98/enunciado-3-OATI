class Consumidor:
    def __init__(self, id, nombre, apellido, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido} - {self.telefono}"
