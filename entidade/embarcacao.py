from enum import Enum
from abc import ABC, abstractmethod


class SiglaEmbarcacao(Enum):
    B = 'B',
    S = 'S',
    F = 'F',
    P = 'P',


class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, sigla: SiglaEmbarcacao, tamanho: int):
        self.__sigla = sigla
        self.__tamanho = tamanho
        self.__vida = tamanho

    @property
    def sigla(self) -> SiglaEmbarcacao:
        return self.__sigla

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    @property
    def afundou(self) -> bool:
        return not self.__vida

    def sigla_escondida(self) -> str:
        return self.sigla.name if self.afundou else 'X'

    def tomar_dano(self):
        if self.__vida:
            self.__vida -= 1
