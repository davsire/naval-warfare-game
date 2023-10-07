from tela.principal_tela import PrincipalTela
from entidade.jogador import Jogador


class PrincipalCtrl:
    def __init__(self):
        self.__jogador_logado = None
        self.__principal_tela = PrincipalTela()
        self.__jogo_ctrl = None
        self.__jogador_ctrl = None
        self.__ranking_ctrl = None
        self.__oceano_ctrl = None
        self.__relatorio_ctrl = None

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

    @property
    def relatorio_ctrl(self):
        return self.__relatorio_ctrl

    def abrir_login_jogador(self):
        print('LOGIN JOGADOR')
        # Login e redirecionamento temporário, implementar no respectivo controlador
        self.__jogador_logado = 'temp'
        self.iniciar_app()

    def abrir_cadastro_jogador(self):
        print('CADASTRO JOGADOR')
        # Cadastro e redirecionamento temporário, implementar no respectivo controlador
        self.__jogador_logado = 'temp'
        self.iniciar_app()

    def abrir_jogo(self):
        print('JOGO')

    def abrir_perfil_jogador(self):
        print('PEFIL')

    def abrir_ranking(self):
        print('RANKING')

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
