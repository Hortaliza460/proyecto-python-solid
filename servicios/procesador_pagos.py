class ProcesadorPagos:

    def procesar(self, metodo_pago, monto):

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")

        metodo_pago.pagar(monto)