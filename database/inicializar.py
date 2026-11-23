from database.conexion import Conexion


def main():
    conexion = Conexion()
    conexion.crear_tablas()
    print("Base de datos creada correctamente")


if __name__ == "__main__":
    main()
