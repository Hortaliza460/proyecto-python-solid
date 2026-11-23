class ReportePedidos:

    def mostrar(self, pedidos):

        print("===== SISTEMA DE VENTAS =====")

        for pedido in pedidos:
            print("Cliente:", pedido.cliente.nombre)

            for producto in pedido.productos:
                print(producto.mostrar_informacion())

            print("Total: S/", pedido.calcular_total())
            print("-----------------------------")