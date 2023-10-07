from controlador.principal_ctrl import PrincipalCtrl
from tela.jogador_tela import JogadorTela
from entidade.jogador import Jogador


class JogadorCtrl:
    def __init__(self, controlador_principal: PrincipalCtrl):
        self.__controlador_principal = controlador_principal
        self.__jogador_tela = JogadorTela()
        self.__jogadores = []

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    def obter_jogador_por_id(self, id: int) -> Jogador:
        pass

    def logar_jogador(self):
        pass

    def mostrar_jogador(self):
        pass

    def cadastrar_jogador(self):
        pass

    def excluir_jogador(self, jogador_logado: Jogador):
        pass

    def editar_jogador(self, jogador_logado: Jogador):
        pass