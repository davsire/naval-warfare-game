from tela.abstract_tela import AbstractTela


class PrincipalTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_menu_login(self) -> int:
        self.mostra_titulo('BEM-VINDO AO JOGO BATALHA NAVAL!')
        self.mostra_opcoes([
            'Login',
            'Cadastrar',
            'Sair do jogo'
        ])
        return self.obtem_opcao('Selecione uma opção: ', [1, 2, 3])

    def mostra_menu_principal(self) -> int:
        self.mostra_titulo('BATALHA NAVAL')
        self.mostra_opcoes([
            'Jogar',
            'Perfil de jogador',
            'Ranking',
            'Logout'
        ])
        return self.obtem_opcao('O que deseja acessar?\nSelecione uma opção: ', [1, 2, 3, 4])
