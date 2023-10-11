from entidade.oceano import Oceano
from tela.oceano_tela import OceanoTela
from exception.posicao_embarcacao_error import PosicaoEmbarcacaoErro
from exception.conflito_embarcacao_error import ConflitoEmbarcacaoErro


class OceanoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__oceano_tela = OceanoTela()
        self.__tamanho_minimo_oceano = 5
        self.__tamanho_maximo_oceano = 15
        self.__oceanos = []
        self.__embarcacoes_iniciais = ['B', 'B', 'B', 'S', 'S', 'F', 'F', 'P']
        self.__indice_letras = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
            'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        }

    def cadastrar_oceano(self) -> tuple:
        self.__oceano_tela.mostra_titulo('CADASTRANDO OCEANO')
        tamanho_oceano = self.__oceano_tela.obtem_tamanho_oceano(
            self.__tamanho_minimo_oceano,
            self.__tamanho_maximo_oceano,
        )
        oceano_jogador = Oceano(tamanho_oceano)
        oceano_pc = Oceano(tamanho_oceano)

        self.__oceano_tela.mostra_mensagem('Seu oceano:')
        self.__oceano_tela.mostra_oceano(oceano_jogador)

        self.preencher_oceano_jogador(oceano_jogador)
        self.preencher_oceano_pc(oceano_pc)

        return oceano_jogador, oceano_pc

    def preencher_oceano_jogador(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        self.__oceano_tela.mostra_titulo('ADICIONANDO EMBARCAÇÕES')
        while len(disponiveis):
            try:
                # TODO: avisar o tamanho do barco
                sigla = self.__oceano_tela.obtem_sigla_embarcacao(disponiveis)
                pos_inicial = self.obter_posicao(oceano.tamanho)
                pos_final = pos_inicial if sigla == 'B' else \
                    self.obter_posicao(oceano.tamanho)
                pos_inicial, pos_final = self.ordernar_posicoes(pos_inicial,
                                                                pos_final)
                oceano.adicionar_embarcacao(sigla, pos_inicial, pos_final)
                disponiveis.remove(sigla)
                self.__oceano_tela.mostra_oceano(oceano)
            except PosicaoEmbarcacaoErro as e:
                self.__oceano_tela.mostra_mensagem(e)
            except ConflitoEmbarcacaoErro as e:
                self.__oceano_tela.mostra_mensagem(e)

    def preencher_oceano_pc(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        while len(disponiveis):
            break

    def obter_posicao(self, tamanho_oceano: int) -> tuple:
        linhas_mapa = range(tamanho_oceano)
        colunas_mapa = list(self.__indice_letras.keys())[:tamanho_oceano]
        while True:
            try:
                linha, coluna = self.__oceano_tela.obter_posicao()
                linha = int(linha) - 1
                coluna = coluna.upper()
                if linha not in linhas_mapa or coluna not in colunas_mapa:
                    raise ValueError
                return linha, self.__indice_letras[coluna]
            except ValueError:
                self.__oceano_tela.mostra_mensagem(
                    'Digite uma linha e coluna existentes no mapa!'
                )

    def ordernar_posicoes(self, pos_inicial: tuple, pos_final: tuple) -> tuple:
        x_inicial, y_inicial = pos_inicial
        x_final, y_final = pos_final

        if x_inicial > x_final or y_inicial > y_final:
            pos_inicial = (x_final, y_final)
            pos_final = (x_inicial, y_inicial)

        return pos_inicial, pos_final
