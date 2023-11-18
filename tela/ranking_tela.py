from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg


class RankingTela(AbstractTela):
    def __init__(self):
        pass

    def abrir_ranking(self, ranking: list):
        layout = [
            *self.obtem_layout_lista(ranking, 'RANKING DOS JOGADORES'),
            *self.obtem_layout_opcoes([
                'Acessar perfil por ID',
                'Voltar ao menu'
            ]),
        ]

        self._window = sg.Window('Batalha Naval',
                                 layout,
                                 element_justification='center')
        opcao_escolhida, _ = self.open()
        if not opcao_escolhida:
            opcao_escolhida = 2
        self.close()
        return opcao_escolhida
