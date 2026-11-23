from abc import ABC, abstractmethod


class MetodoPago(ABC):

    @abstractmethod
    def pagar(self, monto):
        pass


class PagoEfectivo(MetodoPago):

    def pagar(self, monto):
        print(f"Pago en efectivo: S/ {monto:.2f}")


class PagoTarjeta(MetodoPago):

    def pagar(self, monto):
        print(f"Pago con tarjeta: S/ {monto:.2f}")


class PagoTransferencia(MetodoPago):

    def pagar(self, monto):
        print(f"Pago por transferencia: S/ {monto:.2f}")