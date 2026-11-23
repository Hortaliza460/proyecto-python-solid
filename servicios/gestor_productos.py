class GestorProductos:

    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def listar(self):
        return self.productos

    def buscar(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

        return None