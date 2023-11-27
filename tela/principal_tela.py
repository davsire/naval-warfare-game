from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg


class PrincipalTela(AbstractTela):
    def __init__(self):
        super().__init__()
        sg.ChangeLookAndFeel('DarkGrey14')
        sg.set_options(font=('Fixedsys', 14))

    def mostra_menu_login(self) -> int:
        layout = [
            *self.obtem_layout_titulo('BEM-VINDO AO JOGO BATALHA NAVAL!'),
            *self.obtem_layout_opcoes(
                ['Login',
                 'Cadastrar',
                 'Sair do jogo'],
            )
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 3
        self.close()
        return opcao_escolhida

    def mostra_menu_principal(self) -> int:
        layout = [
            *self.obtem_layout_titulo('BATALHA NAVAL!'),
            *self.obtem_layout_opcoes(
                ['Jogar',
                 'Perfil de jogador',
                 'Ranking',
                 'Logout'],
            )
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 4
        self.close()
        return opcao_escolhida
