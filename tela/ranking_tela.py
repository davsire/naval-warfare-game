from tela.abstract_tela import AbstractTela


class RankingTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_jogadores(self, ranking):
        print('-' * 35)
        for index, jogador in enumerate(ranking, start=1):
            print(f'{index} - ID: {jogador.id} - Nome: {jogador.nome}'
                  f' - Pontuacao total: {jogador.pontuacao_total}')
        print('-' * 35)

    def mostra_menu_ranking(self) -> int:
        self.mostra_opcoes([
            'Acessar perfil por ID',
            'Voltar ao menu'
        ])
        return self.obtem_opcao(
            'O que deseja acessar?\nSelecione uma opção: ',
            [1, 2]
        )
