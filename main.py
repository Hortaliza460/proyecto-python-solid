from modelos.producto import Producto
from modelos.cliente import Cliente
from modelos.pedido import Pedido
from servicios.gestor_productos import GestorProductos
from servicios.gestor_pedidos import GestorPedidos
from servicios.reporte_pedidos import ReportePedidos
from servicios.metodos_pago import (
    PagoEfectivo,
    PagoTarjeta,
    PagoTransferencia,
)
from servicios.procesador_pagos import ProcesadorPagos
from datos.repositorio import Repositorio


def main():
    cliente = Cliente("Juan", "juan@gmail.com")
    producto1 = Producto("Laptop", 2500)
    producto2 = Producto("Mouse", 50)

    gestor_productos = GestorProductos()
    gestor_productos.agregar(producto1)
    gestor_productos.agregar(producto2)

    pedido = Pedido(cliente)
    for producto in gestor_productos.listar():
        pedido.agregar_producto(producto)

    gestor_pedidos = GestorPedidos()
    gestor_pedidos.agregar(pedido)

    repositorio = Repositorio()
    repositorio.guardar(pedido)

    reporte = ReportePedidos()
    reporte.mostrar(gestor_pedidos.listar())

    procesador = ProcesadorPagos()
    total = pedido.calcular_total()

    print("\n===== PROCESAMIENTO DE PAGO =====")
    metodo = PagoEfectivo()
    procesador.procesar(metodo, total)


if __name__ == "__main__":
    main()