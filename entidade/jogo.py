from enum import Enum
from datetime import datetime
from entidade.oceano import Oceano
from entidade.jogador import Jogador


class Vencedor(Enum):
    JOGADOR = 1
    PC = 2


class Jogo:
    def __init__(self,
                 id: int,
                 jogador: Jogador,
                 oceano_jogador: Oceano,
                 oceano_pc: Oceano):
        self.__id = id
        self.__data_hora = datetime.now()
        self.__jogador = jogador
        self.__oceano_jogador = oceano_jogador
        self.__oceano_pc = oceano_pc
        self.__vencedor = None
        self.__pontuacao_jogador = 0
        self.__pontuacao_pc = 0
        self.__jogadas = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def data_hora(self) -> str:
        return self.__data_hora.strftime('%d/%m/%Y %H:%M')

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    @property
    def oceano_jogador(self) -> Oceano:
        return self.__oceano_jogador

    @property
    def oceano_pc(self) -> Oceano:
        return self.__oceano_pc

    @property
    def vencedor(self) -> Vencedor:
        return self.__vencedor

    @property
    def pontuacao_jogador(self) -> int:
        return self.__pontuacao_jogador

    @property
    def pontuacao_pc(self) -> int:
        return self.__pontuacao_pc

    @property
    def jogadas(self) -> list:
        return self.__jogadas

    @vencedor.setter
    def vencedor(self, vencedor: Vencedor):
        if isinstance(vencedor, Vencedor):
            self.__vencedor = vencedor

    def aumentar_pontuacao_jogador(self, pontuacao: int):
        self.__pontuacao_jogador += pontuacao

    def aumentar_pontuacao_pc(self, pontuacao: int):
        self.__pontuacao_pc += pontuacao

    def adicionar_jogada_jogador(self,
                                 acertou: bool,
                                 afundou: bool = False,
                                 pontuacao: int = 0):
        jogada = 'JOGADOR: '
        jogada += self.montar_mensagem_jogada(acertou, afundou, pontuacao)
        self.__jogadas.append(jogada)

    def adicionar_jogada_pc(self,
                            acertou: bool,
                            afundou: bool = False,
                            pontuacao: int = 0):
        jogada = 'PC: '
        jogada += self.montar_mensagem_jogada(acertou, afundou, pontuacao)
        self.__jogadas.append(jogada)

    def montar_mensagem_jogada(self,
                               acertou: bool,
                               afundou: bool = False,
                               pontuacao: int = 0) -> str:
        mensagem = ''
        if acertou:
            mensagem += 'Acertou uma embarcação '
            if afundou:
                mensagem += 'e afundou ela '
            mensagem += f'(+{pontuacao} ponto(s))'
        else:
            mensagem += 'Errou o tiro'
        return mensagem
