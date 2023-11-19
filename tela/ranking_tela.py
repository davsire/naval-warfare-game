from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg


class RankingTela(AbstractTela):
    def __init__(self):
        super().__init__()

    def abrir_ranking(self, ranking: list):
        layout = [
            *self.obtem_layout_titulo('RANKING DOS JOGADORES'),
            *self.obtem_layout_lista(ranking),
            *self.obtem_layout_opcoes([
                'Acessar perfil por ID',
                'Voltar ao menu'
            ]),
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 2
        self.close()
        return opcao_escolhida
