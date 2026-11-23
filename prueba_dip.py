from modelos.cliente import Cliente
from modelos.pedido import Pedido
from datos.repositorio_pedidos import RepositorioPedidos
from servicios.registro_pedidos import RegistroPedidos


def main():
    cliente = Cliente("Maria", "maria@gmail.com")
    pedido = Pedido(cliente)
    repositorio = RepositorioPedidos()
    registro = RegistroPedidos(repositorio)
    registro.registrar(pedido)
    print("Pedido registrado correctamente")
    print("Cantidad de pedidos:", len(repositorio.obtener_todos()))


if __name__ == "__main__":
    main()
