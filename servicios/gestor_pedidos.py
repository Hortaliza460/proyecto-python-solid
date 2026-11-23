class GestorPedidos:

    def __init__(self):
        self.pedidos = []

    def agregar(self, pedido):
        self.pedidos.append(pedido)

    def listar(self):
        return self.pedidos

    def buscar_por_cliente(self, nombre):
        return [
            pedido for pedido in self.pedidos
            if pedido.cliente.nombre == nombre
        ]