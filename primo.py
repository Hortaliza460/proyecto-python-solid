import math


def _tiene_divisor_impar(numero: int) -> bool:
    limite = math.isqrt(numero)
    return any(numero % divisor == 0 for divisor in range(3, limite + 1, 2))


def es_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    return not _tiene_divisor_impar(numero)
