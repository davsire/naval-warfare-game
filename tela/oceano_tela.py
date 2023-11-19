import string
from tela.abstract_tela import AbstractTela
from entidade.embarcacao import Embarcacao


class OceanoTela(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__letras_colunas = list(string.ascii_uppercase)
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
                self.mostra_mensagem('Digite um número válido!')

    def obtem_opcao_cadastro_oceano(self) -> int:
        self.mostra_mensagem('O que você deseja fazer?')
        self.mostra_opcoes([
            'Posicionar embarcações',
            'Gerar oceano aleatório',
        ])
        return self.obtem_opcao('Escolha uma opção: ', [1, 2])

    def mostra_embarcacoes_disponiveis(self, disponiveis: list):
        for sigla, nome in self.__nomes_embarcacoes.items():
            print(f'{nome} ({sigla}) - {disponiveis.count(sigla)} disponíveis')

    def obtem_sigla_embarcacao(self, disponiveis: list) -> str:
        while True:
            self.mostra_embarcacoes_disponiveis(disponiveis)
            sigla_embarcacao = input('Digite a sigla da embarcação: ')
            if sigla_embarcacao.upper() in disponiveis:
                return sigla_embarcacao.upper()
            print('Digite a sigla de uma embarcação disponível!')

    def obtem_posicao(self, aviso: str = '') -> tuple:
        while True:
            try:
                if aviso:
                    print(aviso)
                linha, coluna = input(
                    'Digite a linha e coluna separadas por hífen (ex: 1-A): '
                ).split('-')
                if not linha or not coluna:
                    raise ValueError
                return linha, coluna
            except ValueError:
                print('É necessário digitar uma linha e uma coluna!')

    def mostra_oceano(self, mapa: list):
        letras_colunas = self.__letras_colunas[:len(mapa)]
        print(f'{" " * 3}{" ".join(letras_colunas)}')
        for index, linha in enumerate(mapa, start=1):
            print(f'{index:<2}', end=' ')
            for embarcacao in linha:
                if isinstance(embarcacao, Embarcacao):
                    print(embarcacao.sigla.name, end=' ')
                else:
                    print('~', end=' ')
            print('')
