import random
import string
from entidade.oceano import Oceano
from tela.oceano_tela import OceanoTela
from exception.posicao_embarcacao_error import PosicaoEmbarcacaoErro
from exception.conflito_embarcacao_error import ConflitoEmbarcacaoErro


class OceanoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__oceano_tela = OceanoTela()
        self.__tamanho_minimo_oceano = 5
        self.__tamanho_maximo_oceano = 25
        self.__oceanos = []
        self.__embarcacoes_iniciais = ['B', 'B', 'B', 'S', 'S', 'F', 'F', 'P']
        self.__indice_letras = {letra: index
                                for index, letra
                                in enumerate(list(string.ascii_uppercase))}
        self.__tamanho_embarcacoes = {'B': 1, 'S': 2, 'F': 3, 'P': 4}

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

        self.preencher_oceano_aleatorio(oceano_pc)
        if self.__oceano_tela.obtem_opcao_cadastro_oceano() == 1:
            self.preencher_oceano_jogador(oceano_jogador)
        else:
            self.preencher_oceano_aleatorio(oceano_jogador)
            self.__oceano_tela.mostra_mensagem('Seu oceano:')
            self.__oceano_tela.mostra_oceano(oceano_jogador)

        return oceano_jogador, oceano_pc

    def preencher_oceano_jogador(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        self.__oceano_tela.mostra_titulo('ADICIONANDO EMBARCAÇÕES')
        while len(disponiveis):
            try:
                sigla = self.__oceano_tela.obtem_sigla_embarcacao(disponiveis)
                tamanho = self.__tamanho_embarcacoes[sigla]
                self.__oceano_tela.mostra_mensagem('** Tamanho da embarcação: '
                                                   f'{tamanho} espaço(s) **')
                pos_inicial = self.obter_posicao(oceano.tamanho)
                pos_final = pos_inicial if sigla == 'B' else \
                    self.obter_posicao(oceano.tamanho)
                pos_inicial, pos_final = self.ordernar_posicoes(pos_inicial,
                                                                pos_final)
                oceano.adicionar_embarcacao(sigla, pos_inicial, pos_final)
                disponiveis.remove(sigla)
                self.__oceano_tela.mostra_oceano(oceano)
            except (PosicaoEmbarcacaoErro, ConflitoEmbarcacaoErro) as e:
                self.__oceano_tela.mostra_mensagem(e)

    def preencher_oceano_aleatorio(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        while len(disponiveis):
            try:
                sigla = disponiveis[-1]
                tamanho_embarcacao = self.__tamanho_embarcacoes[sigla]
                pos_inicial, pos_final = self.obter_posicoes_aleatorias(
                    oceano.tamanho, tamanho_embarcacao
                )
                oceano.adicionar_embarcacao(sigla, pos_inicial, pos_final)
                disponiveis.remove(sigla)
            except ConflitoEmbarcacaoErro:
                pass

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

    def obter_posicoes_aleatorias(self,
                                  tamanho_oceano: int,
                                  tamanho_embarcacao: int) -> tuple:
        is_horizontal = bool(round(random.random()))
        coord_fixa = random.randrange(tamanho_oceano)
        coord_inicial = random.randint(0, tamanho_oceano - tamanho_embarcacao)
        coord_final = coord_inicial + (tamanho_embarcacao - 1)

        pos_inicial = (coord_fixa, coord_inicial) if is_horizontal \
            else (coord_inicial, coord_fixa)
        pos_final = (coord_fixa, coord_final) if is_horizontal \
            else (coord_final, coord_fixa)
        return pos_inicial, pos_final

    def ordernar_posicoes(self, pos_inicial: tuple, pos_final: tuple) -> tuple:
        x_inicial, y_inicial = pos_inicial
        x_final, y_final = pos_final

        if x_inicial > x_final or y_inicial > y_final:
            pos_inicial = (x_final, y_final)
            pos_final = (x_inicial, y_inicial)

        return pos_inicial, pos_final
