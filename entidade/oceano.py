from entidade.embarcacao import Embarcacao
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from exception.posicao_embarcacao_error import PosicaoEmbarcacaoErro
from exception.conflito_embarcacao_error import ConflitoEmbarcacaoErro


class Oceano:
    def __init__(self, tamanho: int):
        self.__tamanho = tamanho
        self.__mapa = [[None for _ in range(tamanho)] for _ in range(tamanho)]

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    @property
    def mapa(self) -> list:
        return self.__mapa

    def adicionar_embarcacao(self,
                             sigla_embarcacao: str,
                             coord_inicio: tuple,
                             coord_final: tuple):
        embarcacao = self.criar_embarcacao(sigla_embarcacao)

        self.verificar_tamanho_embarcacao(embarcacao,
                                          coord_inicio,
                                          coord_final)
        self.verificar_conflito_embarcacao(coord_inicio, coord_final)

        x_inicio, y_inicio = coord_inicio
        x_final, y_final = coord_final
        for linha in range(x_inicio, x_final + 1):
            for coluna in range(y_inicio, y_final + 1):
                self.__mapa[linha][coluna] = embarcacao

    def criar_embarcacao(self, sigla_embarcacao: str) -> Embarcacao:
        lista_embarcacoes = {
            'B': Bote,
            'S': Submarino,
            'F': Fragata,
            'P': PortaAvioes,
        }
        return lista_embarcacoes[sigla_embarcacao]()

    def verificar_tamanho_embarcacao(self,
                                     embarcacao: Embarcacao,
                                     coord_inicio: tuple,
                                     coord_final: tuple):
        x_inicio, y_inicio = coord_inicio
        x_final, y_final = coord_final
        comprimento = max(abs(x_final - x_inicio), abs(y_final - y_inicio))
        largura = min(abs(x_final - x_inicio), abs(y_final - y_inicio))
        if comprimento != (embarcacao.tamanho - 1) or largura != 0:
            raise PosicaoEmbarcacaoErro

    def verificar_conflito_embarcacao(self,
                                      coord_inicio: tuple,
                                      coord_final: tuple):
        x_inicio, y_inicio = coord_inicio
        x_final, y_final = coord_final
        for linha in range(x_inicio, x_final + 1):
            for coluna in range(y_inicio, y_final + 1):
                if isinstance(self.__mapa[linha][coluna], Embarcacao):
                    raise ConflitoEmbarcacaoErro(linha + 1, coluna + 1)
