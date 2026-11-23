from datos.interfaces import Guardable


class RegistroPedidos:
    def __init__(self, repositorio: Guardable):
        self.repositorio = repositorio

    def registrar(self, pedido):
        self.repositorio.guardar(pedido)
