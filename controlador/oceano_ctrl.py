import random
import string
from entidade.oceano import Oceano
from entidade.embarcacao import SiglaEmbarcacao
from tela.oceano_tela import OceanoTela
from dao.oceano_dao import OceanoDAO
from exception.posicao_embarcacao_error import PosicaoEmbarcacaoErro
from exception.conflito_embarcacao_error import ConflitoEmbarcacaoErro
from tela.abstract_tela import OpcaoBotao


class OceanoCtrl:
    __instancia = None

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__oceano_tela = OceanoTela()
        self.__oceano_dao = OceanoDAO()
        self.__tamanho_minimo_oceano = 5
        self.__tamanho_maximo_oceano = 15
        self.__embarcacoes_iniciais = ['B', 'B', 'B', 'S', 'S', 'F', 'F', 'P']
        self.__indice_letras = {letra: index
                                for index, letra
                                in enumerate(list(string.ascii_uppercase))}
        self.__tamanho_embarcacoes = {SiglaEmbarcacao.B.name: 1,
                                      SiglaEmbarcacao.S.name: 2,
                                      SiglaEmbarcacao.F.name: 3,
                                      SiglaEmbarcacao.P.name: 4}

    def __new__(cls, controlador_principal):
        if OceanoCtrl.__instancia is None:
            OceanoCtrl.__instancia = object.__new__(cls)
        return OceanoCtrl.__instancia

    @property
    def __proximo_id(self):
        ultimo_id = max([oceano.id for oceano in self.oceanos], default=0)
        return ultimo_id + 1

    @property
    def oceanos(self) -> list:
        return self.__oceano_dao.get_all()

    def salvar_oceano(self, tamanho_oceano: int):
        oceano = Oceano(self.__proximo_id, tamanho_oceano)
        self.__oceano_dao.add(oceano)
        return oceano

    def remover_oceano(self, oceano: Oceano):
        self.__oceano_dao.remove(oceano)

    def cadastrar_oceano(self) -> tuple:
        opcao, tamanho_oceano = self.__oceano_tela.obtem_tamanho_oceano(
            self.__tamanho_minimo_oceano,
            self.__tamanho_maximo_oceano,
        )
        if opcao == OpcaoBotao.VOLTAR:
            self.__controlador_principal.iniciar_app()
        oceano_jogador = self.salvar_oceano(tamanho_oceano)
        oceano_pc = self.salvar_oceano(tamanho_oceano)

        opcao_cadastro = self.__oceano_tela.mostra_oceano_inicial(
            oceano_jogador.mapa
        )

        if opcao_cadastro == OpcaoBotao.VOLTAR:
            self.__controlador_principal.iniciar_app()

        self.preencher_oceano_aleatorio(oceano_pc)
        if opcao_cadastro == 1:
            self.preencher_oceano_jogador(oceano_jogador)
        else:
            self.preencher_oceano_aleatorio(oceano_jogador)

        return oceano_jogador, oceano_pc

    def preencher_oceano_jogador(self, oceano: Oceano):
        disponiveis = self.__embarcacoes_iniciais.copy()
        while len(disponiveis):
            try:
                sigla = self.__oceano_tela.obtem_sigla_embarcacao(disponiveis)
                if sigla == OpcaoBotao.VOLTAR:
                    self.__controlador_principal.iniciar_app()

                pos_inicial, pos_final, opcao = self.obter_posicoes(oceano,
                                                                    sigla)
                if opcao == OpcaoBotao.VOLTAR:
                    continue
                pos_inicial, pos_final = self.ordernar_posicoes(pos_inicial,
                                                                pos_final)

                oceano.adicionar_embarcacao(sigla, pos_inicial, pos_final)
                disponiveis.remove(sigla)
                self.__oceano_tela.mostra_oceano(oceano.mapa)
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

    def obter_posicoes(self, oceano: Oceano, sigla: str) -> tuple:
        is_bote = sigla == SiglaEmbarcacao.B.name
        linhas_mapa = range(oceano.tamanho)
        colunas_mapa = list(self.__indice_letras.keys())[:oceano.tamanho]
        while True:
            try:
                pos_inicial, pos_final, opcao = (
                    self.__oceano_tela.obtem_posicoes(
                        oceano.mapa, self.__tamanho_embarcacoes[sigla], is_bote
                    )
                )

                if opcao == OpcaoBotao.VOLTAR:
                    return None, None, opcao

                linha_inicial = int(pos_inicial[0]) - 1
                linha_final = int(pos_final[0]) - 1
                coluna_inicial = pos_inicial[1].upper()
                coluna_final = pos_final[1].upper()

                if any([linha_inicial not in linhas_mapa,
                        linha_final not in linhas_mapa,
                        coluna_inicial not in colunas_mapa,
                        coluna_final not in colunas_mapa]):
                    raise ValueError

                pos_inicial = (linha_inicial,
                               self.__indice_letras[coluna_inicial])
                pos_final = (linha_final,
                             self.__indice_letras[coluna_final])

                return pos_inicial, pos_final, None
            except ValueError:
                self.__oceano_tela.mostra_mensagem(
                    'As linhas e colunas devem existir no mapa!'
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
