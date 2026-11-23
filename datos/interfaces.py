from abc import ABC, abstractmethod


class Guardable(ABC):
    @abstractmethod
    def guardar(self, elemento):
        pass


class Consultable(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass
