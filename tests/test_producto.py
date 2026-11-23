from modelos.producto import Producto


def test_crear_producto():
    producto = Producto("Laptop", 2500)
    assert producto.nombre == "Laptop"
    assert producto.precio == 2500


def test_mostrar_informacion():
    producto = Producto("Mouse", 50)
    assert producto.mostrar_informacion() == "Mouse - S/ 50.00"
