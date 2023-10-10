from entidade.oceano import Oceano
from tela.oceano_tela import OceanoTela
from exception.posicao_embarcacao_error import PosicaoEmbarcacaoErro
from exception.conflito_embarcacao_error import ConflitoEmbarcacaoErro


class OceanoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__oceano_tela = OceanoTela()
        self.__oceanos = []
        self.__embarcacoes_iniciais = ['B', 'B', 'B', 'S', 'S', 'F', 'F', 'P']
        self.__nomes_embarcacoes = {
            'B': 'Bote',
            'S': 'Submarino',
            'F': 'Fragata',
            'P': 'Porta Aviões',
        }

    def cadastrar_oceano(self) -> tuple:
        tamanho_oceano = self.__oceano_tela.obtem_tamanho_oceano()
        oceano_jogador = Oceano(tamanho_oceano)
        oceano_pc = Oceano(tamanho_oceano)

        self.__oceano_tela.mostra_mensagem('Seu oceano:')
        self.__oceano_tela.mostra_oceano(oceano_jogador)

        self.preencher_oceano_jogador(oceano_jogador)
        self.preencher_oceano_jogador(oceano_pc)

        return oceano_jogador, oceano_pc

    def preencher_oceano_jogador(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        self.__oceano_tela.mostra_titulo('ADICIONANDO EMBARCAÇÕES')
        while len(disponiveis):
            try:
                sigla = self.__oceano_tela.obtem_sigla_embarcacao(disponiveis)
                pos_inicial = self.__oceano_tela.obter_posicao(oceano.tamanho)
                pos_final = pos_inicial if sigla == 'B' else \
                    self.__oceano_tela.obter_posicao(oceano.tamanho)
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
