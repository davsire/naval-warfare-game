import string
from entidade.jogo import Vencedor
from tela.abstract_tela import AbstractTela
from entidade.jogo import Jogo
from entidade.embarcacao import Embarcacao


class JogoTela(AbstractTela):
    def __init__(self):
        self.__letras_colunas = list(string.ascii_uppercase)

    def obtem_id_jogo(self) -> int:
        while True:
            try:
                id_jogo = int(input('Digite o ID do jogo: '))
                return id_jogo
            except ValueError:
                print('Digite um id válido!')

    def mostra_situacao_jogo(self, jogo: Jogo):
        print('-' * 35)
        print('Pontuações:')
        print(f'Jogador: {jogo.pontuacao_jogador} - PC: {jogo.pontuacao_pc}')
        print('-' * 35)
        self.mostra_oceanos(jogo)

    def mostra_fim_jogo(self, vencedor: Vencedor):
        if vencedor == Vencedor.JOGADOR:
            print('~' * 35)
            print('Parabéns!!! Você venceu a partida!')
            print('~' * 35)
        else:
            print('~' * 35)
            print('Que pena, a vitória não veio dessa vez...')
            print('~' * 35)

    def mostra_oceanos(self, jogo: Jogo):
        oceano_jogador = jogo.oceano_jogador
        oceano_pc = jogo.oceano_pc
        letras_colunas = self.__letras_colunas[:oceano_jogador.tamanho]
        print('** Seu oceano / Oceano do PC **')
        print(f'{" " * 3}{" ".join(letras_colunas)}', end='')
        print(f'{" " * 7}{" ".join(letras_colunas)}')

        for linha in range(len(oceano_jogador.mapa)):
            linha_jogador = oceano_jogador.mapa[linha]
            linha_pc = oceano_pc.mapa[linha]
            numero_linha = f'{linha + 1:<2}'

            print(f'{numero_linha}', end=' ')
            for posicao in linha_jogador:
                if isinstance(posicao, Embarcacao):
                    print(posicao.sigla, end=' ')
                elif isinstance(posicao, str):
                    print(posicao, end=' ')
                elif not posicao:
                    print('~', end=' ')
                else:
                    print('X', end=' ')
            print(" " * 3, end='')

            print(f'{numero_linha}', end=' ')
            for posicao in linha_pc:
                if isinstance(posicao, Embarcacao) or not posicao:
                    print('~', end=' ')
                elif isinstance(posicao, list):
                    embarcacao = posicao[0]
                    print(embarcacao.sigla_escondida(), end=' ')
                else:
                    print(posicao, end=' ')
            print('')

    def mostra_relatorio_jogo(self, jogo: Jogo):
        self.mostra_titulo('RELATÓRIO DE JOGO')
        print('-' * 35)
        print(f'ID: {jogo.id}\n'
              f'Vencedor: {jogo.vencedor.name}\n'
              f'Data: {jogo.data_hora}\n'
              f'Pontuação do jogador: {jogo.pontuacao_jogador} pts\n'
              f'Pontuação do PC: {jogo.pontuacao_pc} pts')
        print('-' * 35)

    def mostra_jogadas(self, jogo: Jogo):
        print('-' * 35)
        print('\n'.join(jogo.jogadas))
        print('-' * 35)

    def mostra_menu_relatorio_jogo(self) -> int:
        self.mostra_opcoes([
            'Visualizar mapas finais da partida',
            'Visualizar jogadas da partida',
            'Voltar ao menu'
        ])
        return self.obtem_opcao('O que deseja acessar?\nSelecione uma opção: ',
                                [1, 2, 3])
