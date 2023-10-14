from tela.ranking_tela import RankingTela
from controlador.jogador_ctrl import JogadorCtrl


class RankingCtrl:
    def __init__(self, controlador_principal, controlador_jogador):
        self.__controlador_principal = controlador_principal
        self.__controlador_jogador = controlador_jogador
        self.__tela_ranking = RankingTela()

    def listar_jogadores(self):
        self.__tela_ranking.mostra_titulo(
            'RANKING DOS JOGADORES')
        controlador_jogador = self.__controlador_jogador
        jogadores = controlador_jogador.jogadores
        ranking = []
        for jogador in jogadores:
            if len(ranking) == 0:
                ranking.append(jogador)
            elif len(ranking) == 1:
                if jogador.pontuacao_total > ranking[0].pontuacao_total:
                    ranking.insert(0, jogador)
                else:
                    ranking.append(jogador)
            elif len(ranking) > 1:
                for i in range(len(ranking)):
                    if jogador.pontuacao_total > ranking[i].pontuacao_total:
                        ranking.insert(i, jogador)
                else:
                    ranking.append(jogador)
        self.__tela_ranking.mostra_jogadores(ranking)
        self.menu_ranking()

    def acessar_perfil(self):
        controlador_jogador = self.__controlador_jogador
        jogador = controlador_jogador.mostrar_jogador()
        opcoes_acoes = {
                1: self.mostrar_historico_jogos,
                2: self.__controlador_principal.iniciar_app,
            }

        opcao_escolhida = self.__ranking_tela.mostra_menu_perfil()
        if opcao_escolhida == 1:
            opcoes_acoes[opcao_escolhida](jogador)
        else:
            opcoes_acoes[opcao_escolhida]()

    def menu_ranking(self):
        opcoes_acoes = {
                1: self.acessar_perfil,
                2: self.__controlador_principal.iniciar_app,
            }

        opcao_escolhida = self.__tela_ranking.mostra_menu_ranking()
        opcoes_acoes[opcao_escolhida]()
