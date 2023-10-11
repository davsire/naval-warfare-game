from tela.abstract_tela import AbstractTela
from entidade.oceano import Oceano
from entidade.embarcacao import Embarcacao


class OceanoTela(AbstractTela):
    def __init__(self):
        self.__letras_colunas = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O'
        ]
        self.__nomes_embarcacoes = {
            'B': 'Bote',
            'S': 'Submarino',
            'F': 'Fragata',
            'P': 'Porta Aviões',
        }

    def obtem_tamanho_oceano(self, minimo: int, maximo: int) -> int:
        while True:
            self.mostra_mensagem('O tamanho do oceano deve ser maior ou igual '
                                 f'a {minimo} espaços e menor '
                                 f'ou igual a {maximo} espaços!')
            try:
                tamanho = int(input('Digite o tamanho dos oceanos do jogo: '))
                if tamanho < minimo or \
                        tamanho > maximo:
                    raise ValueError
                return tamanho
            except ValueError:
                print('Digite um número válido!')

    def obtem_sigla_embarcacao(self, disponiveis: list) -> str:
        while True:
            self.mostra_embarcacoes_disponiveis(disponiveis)
            sigla_embarcacao = input('Digite a sigla da embarcação: ')
            if sigla_embarcacao.upper() in disponiveis:
                return sigla_embarcacao.upper()
            print('Digite a sigla de uma embarcação disponível!')

    def mostra_embarcacoes_disponiveis(self, disponiveis: list):
        for sigla, nome in self.__nomes_embarcacoes.items():
            print(f'{nome} ({sigla}) - {disponiveis.count(sigla)} disponíveis')

    def obter_posicao(self) -> tuple:
        while True:
            try:
                # TODO: avisar qual eh o inicio e final
                linha, coluna = input(
                    'Digite a linha e coluna separadas por hífen (ex: 1-A): '
                ).split('-')
                if not linha or not coluna:
                    raise ValueError
                return linha, coluna
            except ValueError:
                print('É necessário digitar uma linha e uma coluna!')

    def mostra_oceano(self, oceano: Oceano):
        letras_colunas = self.__letras_colunas[:oceano.tamanho]
        print(f'{" " * 3}{" ".join(letras_colunas)}')
        for index, linha in enumerate(oceano.mapa, start=1):
            print(f'{index:<2}', end=' ')
            for embarcacao in linha:
                if isinstance(embarcacao, Embarcacao):
                    print(embarcacao.sigla, end=' ')
                else:
                    print('~', end=' ')
            print('')
