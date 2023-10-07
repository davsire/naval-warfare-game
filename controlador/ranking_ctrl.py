from controlador.principal_ctrl import PrincipalCtrl
from tela.ranking_tela import RankingTela


class RankingCtrl:
    def __init__(self, controlador_principal: PrincipalCtrl):
        self.__controlador_principal = controlador_principal
        self.__tela_ranking = RankingTela()

    def listar_jogadores(self):
        pass
