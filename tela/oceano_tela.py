import string
from tela.abstract_tela import AbstractTela, OpcaoBotao
from entidade.embarcacao import Embarcacao
import PySimpleGUI as sg


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

    def obtem_tamanho_oceano(self, minimo: int, maximo: int) -> tuple:
        dados = {
            'tamanho_oceano': 'Digite o tamanho dos oceanos do jogo:'
        }
        while True:
            layout = [
                *self.obtem_layout_titulo('CADASTRANDO OCEANO'),
                [sg.Text(
                    'O tamanho do oceano deve ser maior ou igual '
                    f'a {minimo} espaços e menor '
                    f'ou igual a {maximo} espaços!',
                    size=(50, 2),
                    justification='center',
                    pad=(0, 10)
                )],
                *self.obtem_layout_obtem_dados(dados, 'Confirmar'),
            ]
            botao, valores = self.open(layout)
            self.close()
            if botao == OpcaoBotao.VOLTAR or not botao:
                return OpcaoBotao.VOLTAR, None
            try:
                tamanho = int(valores['tamanho_oceano'])
                if tamanho < minimo or \
                        tamanho > maximo:
                    raise ValueError
                return botao, tamanho
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
