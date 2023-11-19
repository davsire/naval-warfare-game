from tela.ranking_tela import RankingTela


class RankingCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__ranking_tela = RankingTela()

    def mostra_ranking(self):
        while True:
            jogadores = self.__controlador_principal.jogador_ctrl.jogadores
            jogadores_ord = sorted(jogadores,
                                   key=lambda jogador: jogador.pontuacao_total,
                                   reverse=True)
            ranking = [
                f'ID: {jogador.id} - Nome: {jogador.nome}'
                f' - Pontuacao total: {jogador.pontuacao_total}'
                for jogador in jogadores_ord
            ]

            opcao_escolhida = self.__ranking_tela.abrir_ranking(ranking)
            self.redirecionar(opcao_escolhida)

    def redirecionar(self, opcao_escolhida: int):
        opcoes_acoes = {
                1: self.__controlador_principal.jogador_ctrl.mostrar_jogador,
                2: self.__controlador_principal.abrir_menu_principal,
            }
        opcoes_acoes[opcao_escolhida]()
