from abc import ABC, abstractmethod


class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, identificador: str, tamanho: int):
        self.__identificador = identificador
        self.__tamanho = tamanho
        self.__vida = tamanho

    @property
    def identificador(self) -> str:
        return 'X' if self.__vida else self.__identificador

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    @property
    def afundou(self) -> bool:
        return not self.__vida

    def tomar_dano(self):
        self.__vida -= 1
