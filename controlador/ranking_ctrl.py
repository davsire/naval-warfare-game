from tela.ranking_tela import RankingTela
from controlador.jogador_ctrl import JogadorCtrl


class RankingCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_ranking = RankingTela()

    def listar_jogadores(self):
        self.__tela_ranking.mostra_titulo(
            'RANKING DOS JOGADORES')
        controlador_jogador = self.__controlador_principal.jogador_ctrl
        jogadores = controlador_jogador.jogadores
        ranking = sorted(jogadores,
                         key=lambda jogador: jogador.pontuacao_total,
                         reverse=True)
        self.__tela_ranking.mostra_jogadores(ranking)
        self.menu_ranking()

    def menu_ranking(self):
        controlador_jogador = self.__controlador_principal.jogador_ctrl
        opcoes_acoes = {
                1: controlador_jogador.mostrar_jogador(),
                2: self.__controlador_principal.abrir_menu_principal,
            }

        opcao_escolhida = self.__tela_ranking.mostra_menu_ranking()
        opcoes_acoes[opcao_escolhida]()
