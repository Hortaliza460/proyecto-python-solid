class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        return f"{self.nombre} - S/ {self.precio:.2f}"