from tela.principal_tela import PrincipalTela
from entidade.jogador import Jogador
from controlador.jogo_ctrl import JogoCtrl
from controlador.jogador_ctrl import JogadorCtrl
from controlador.ranking_ctrl import RankingCtrl
from controlador.oceano_ctrl import OceanoCtrl


class PrincipalCtrl:
    def __init__(self):
        self.__jogador_logado = None
        self.__principal_tela = PrincipalTela()
        self.__jogo_ctrl = JogoCtrl(self)
        self.__jogador_ctrl = JogadorCtrl(self)
        self.__ranking_ctrl = RankingCtrl(self)
        self.__oceano_ctrl = OceanoCtrl(self)

    @property
    def jogador_logado(self) -> Jogador:
        return self.__jogador_logado

    @property
    def jogo_ctrl(self):
        return self.__jogo_ctrl

    @property
    def jogador_ctrl(self):
        return self.__jogador_ctrl

    @property
    def ranking_ctrl(self):
        return self.__ranking_ctrl

    @property
    def oceano_ctrl(self):
        return self.__oceano_ctrl

    def abrir_login_jogador(self):
        self.__jogador_logado = self.__jogador_ctrl.logar_jogador()
        self.iniciar_app()

    def abrir_cadastro_jogador(self):
        self.__jogador_logado = self.__jogador_ctrl.cadastrar_jogador()
        self.iniciar_app()

    def abrir_jogo(self):
        self.__jogo_ctrl.iniciar_jogo()

    def abrir_perfil_jogador(self):
        self.__jogador_ctrl.mostrar_jogador(self.__jogador_logado)

    def abrir_ranking(self):
        self.__ranking_ctrl.abrir_ranking()

    def sair(self):
        exit(0)

    def logout(self):
        self.__jogador_logado = None
        self.iniciar_app()

    def iniciar_app(self):
        if self.__jogador_logado:
            self.abrir_menu_principal()
        else:
            self.abrir_menu_login()

    def abrir_menu_login(self):
        while True:
            opcoes_acoes = {
                1: self.abrir_login_jogador,
                2: self.abrir_cadastro_jogador,
                3: self.sair
            }

            opcao_escolhida = self.__principal_tela.mostra_menu_login()
            opcoes_acoes[opcao_escolhida]()

    def abrir_menu_principal(self):
        while True:
            opcoes_acoes = {
                1: self.abrir_jogo,
                2: self.abrir_perfil_jogador,
                3: self.abrir_ranking,
                4: self.logout,
            }

            opcao_escolhida = self.__principal_tela.mostra_menu_principal()
            opcoes_acoes[opcao_escolhida]()
