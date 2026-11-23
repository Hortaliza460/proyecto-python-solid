from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2


class CalculadoraAreas:
    def sumar_areas(self, figuras: list[Figura]) -> float:
        return sum(figura.calcular_area() for figura in figuras)


def main() -> None:
    figuras = [
        Circulo(5),
        Rectangulo(4, 6),
        Triangulo(10, 4),
    ]
    calculadora = CalculadoraAreas()
    print(f"Área total: {calculadora.sumar_areas(figuras):.2f}")


if __name__ == "__main__":
    main()
