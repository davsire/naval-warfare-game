import string
from tela.abstract_tela import AbstractTela
from entidade.jogo import Jogo
from entidade.embarcacao import Embarcacao


class JogoTela(AbstractTela):
    def __init__(self):
        self.__letras_colunas = list(string.ascii_uppercase)

    def mostra_situacao_jogo(self, jogo: Jogo):
        print('-' * 35)
        print('Pontuações:')
        print(f'Jogador: {jogo.pontuacao_jogador} - PC: {jogo.pontuacao_pc}')
        print('-' * 35)
        self.mostra_oceanos(jogo)

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
