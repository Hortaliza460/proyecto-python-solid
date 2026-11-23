class Repositorio:

    def __init__(self):
        self.datos = []

    def guardar(self, elemento):
        self.datos.append(elemento)

    def obtener_todos(self):
        return self.datos