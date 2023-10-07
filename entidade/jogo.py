from datetime import date
from entidade.oceano import Oceano


class Jogo:
    def __init__(self, id: int, oceano_jogador: Oceano, oceano_pc: Oceano):
        self.__id = id
        self.__data_hora = date.today()
        self.__oceano_jogador = oceano_jogador
        self.__oceano_pc = oceano_pc
        self.__vencedor = None
        self.__pontuacao_jogador = 0
        self.__pontuacao_pc = 0
        self.__jogadas_jogador = []
        self.__jogadas_pc = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def data_hora(self) -> date:
        return self.__data_hora

    @property
    def oceano_jogador(self) -> Oceano:
        return self.__oceano_jogador

    @property
    def oceano_pc(self) -> Oceano:
        return self.__oceano_pc

    @property
    def vencedor(self) -> str:
        return self.__vencedor

    @property
    def pontuacao_jogador(self) -> int:
        return self.__pontuacao_jogador

    @property
    def pontuacao_pc(self) -> int:
        return self.__pontuacao_pc

    @property
    def jogadas_jogador(self) -> list:
        return self.__jogadas_jogador

    @property
    def jogadas_pc(self) -> list:
        return self.__jogadas_pc

    @vencedor.setter
    def vencedor(self, vencedor: str):
        if isinstance(vencedor, str):
            self.__vencedor = vencedor

    def aumentar_pontuacao_jogador(self, pontuacao: int):
        self.__pontuacao_jogador += pontuacao

    def aumentar_pontuacao_pc(self, pontuacao: int):
        self.__pontuacao_pc += pontuacao

    def adicionar_jogada_jogador(self):
        # TODO: implementar lógica de adicionar jogada depois
        pass

    def adicionar_jogada_pc(self):
        # TODO: implementar lógica de adicionar jogada depois
        pass
