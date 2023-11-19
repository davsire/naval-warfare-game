from tela.ranking_tela import RankingTela


class RankingCtrl:
    __instancia = None

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__ranking_tela = RankingTela()

    def __new__(cls):
        if RankingCtrl.__instancia is None:
            RankingCtrl.__instancia = object.__new__(cls)
        return RankingCtrl.__instancia

    def listar_jogadores(self):
        self.__ranking_tela.mostra_titulo('RANKING DOS JOGADORES')
        jogadores = self.__controlador_principal.jogador_ctrl.jogadores
        ranking = sorted(jogadores,
                         key=lambda jogador: jogador.pontuacao_total,
                         reverse=True)
        self.__ranking_tela.mostra_jogadores(ranking)
        self.abrir_menu_ranking()

    def abrir_menu_ranking(self):
        controlador_jogador = self.__controlador_principal.jogador_ctrl
        opcoes_acoes = {
                1: controlador_jogador.mostrar_jogador,
                2: self.__controlador_principal.abrir_menu_principal,
            }
        while True:
            opcao_escolhida = self.__ranking_tela.mostra_menu_ranking()
            opcoes_acoes[opcao_escolhida]()
