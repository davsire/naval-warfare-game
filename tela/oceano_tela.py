from tela.abstract_tela import AbstractTela
from entidade.oceano import Oceano
from entidade.embarcacao import Embarcacao


class OceanoTela(AbstractTela):
    def __init__(self):
        self.__tamanho_minimo = 5
        self.__tamanho_maximo = 15
        self.__indice_letras = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
        }
        self.__nomes_embarcacoes = {
            'B': 'Bote',
            'S': 'Submarino',
            'F': 'Fragata',
            'P': 'Porta Aviões',
        }

    def obtem_tamanho_oceano(self) -> int:
        self.mostra_titulo('CADASTRANDO OCEANO')
        while True:
            self.mostra_mensagem('O tamanho do oceano deve ser maior que '
                                 f'{self.__tamanho_minimo} espaços e '
                                 f'menor que {self.__tamanho_maximo} espaços!')
            try:
                tamanho = int(input('Digite o tamanho dos oceanos do jogo: '))
                if tamanho < self.__tamanho_minimo or \
                        tamanho > self.__tamanho_maximo:
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

    def obter_posicao(self, tamanho_oceano: int) -> tuple:
        while True:
            linha, coluna = input(
                'Digite a linha e coluna separas por hífen (ex: 1-A): '
            ).split('-')

            return linha, coluna

    def mostra_oceano(self, oceano: Oceano):
        letras_colunas = list(self.__indice_letras.keys())[:oceano.tamanho]
        print(f'{" " * 4}{" ".join(letras_colunas)}')
        for index, linha in enumerate(oceano.mapa, start=1):
            print(f'{index:<2}', end=' ')
            for embarcacao in linha:
                if isinstance(embarcacao, Embarcacao):
                    print(embarcacao.sigla, end=' ')
                else:
                    print('~', end=' ')
            print('')
