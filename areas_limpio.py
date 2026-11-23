import math


def area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)


def area_rectangulo(base: float, altura: float) -> float:
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


def mostrar_areas() -> None:
    resultados = {
        "Círculo": area_circulo(radio=5),
        "Rectángulo": area_rectangulo(base=4, altura=6),
        "Triángulo": area_triangulo(base=4, altura=6),
    }
    for figura, area in resultados.items():
        print(f"{figura}: {area:.2f}")


if __name__ == "__main__":
    mostrar_areas()
