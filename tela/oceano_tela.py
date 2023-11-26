import string
from tela.abstract_tela import AbstractTela, OpcaoBotao
from entidade.embarcacao import Embarcacao, SiglaEmbarcacao
import PySimpleGUI as sg


class OceanoTela(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__letras_colunas = list(string.ascii_uppercase)
        self.__nomes_embarcacoes = {
            SiglaEmbarcacao.B.name: 'Bote',
            SiglaEmbarcacao.S.name: 'Submarino',
            SiglaEmbarcacao.F.name: 'Fragata',
            SiglaEmbarcacao.P.name: 'Porta Aviões',
        }
        self.__cores_mapa = {
            SiglaEmbarcacao.B.name: '#ebbb78',
            SiglaEmbarcacao.S.name: '#7bf263',
            SiglaEmbarcacao.F.name: '#9a74e8',
            SiglaEmbarcacao.P.name: '#86b4e3',
            'X': 'red',
            '*': 'white',
            '~': '#4a9ee0',
        }

    def obtem_sigla_mapa(self, posicao_mapa) -> str:
        if isinstance(posicao_mapa, Embarcacao):
            return posicao_mapa.sigla.name
        return '~'

    def obtem_layout_oceano(self, mapa: list):
        letras_colunas = self.__letras_colunas[:len(mapa)]
        layout_header = [
            [
                sg.Text('', size=2),
                *[sg.Button(coluna,
                            size=(3, 1),
                            p=(2, 2),
                            disabled=True,
                            button_color=('black', 'lightgray'),
                            disabled_button_color=('black', 'lightgray'))
                    for coluna in letras_colunas]
            ]
        ]
        layout_mapa = [
            [
                sg.Button(index_linha + 1,
                          size=(2, 2),
                          p=(2, 2),
                          disabled=True,
                          button_color=('black', 'lightgray'),
                          disabled_button_color=('black', 'lightgray')),
                *[
                    sg.Button(self.obtem_sigla_mapa(posicao),
                              size=(3, 2),
                              p=(2, 2),
                              disabled=True,
                              button_color=(
                                  self.__cores_mapa[
                                      self.obtem_sigla_mapa(posicao)
                                  ],
                                  'darkblue'
                              ),
                              disabled_button_color=(
                                  self.__cores_mapa[
                                      self.obtem_sigla_mapa(posicao)
                                  ],
                                  'darkblue'
                              ))
                    for posicao in linha
                ]
            ]
            for index_linha, linha in enumerate(mapa)
        ]

        return layout_header + layout_mapa

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

    def obtem_sigla_embarcacao(self, disponiveis: list) -> str:
        layout = [
            *self.obtem_layout_titulo('ESCOLHA SUA EMBARCAÇÃO'),
            [
                [sg.Button(nome,
                           key=sigla,
                           size=15,
                           disabled=(not disponiveis.count(sigla))),
                 sg.Text(f'({disponiveis.count(sigla)} disponíveis)')]
                for sigla, nome in self.__nomes_embarcacoes.items()
            ]
        ]
        botao, _ = self.open(layout)
        self.close()
        if not botao:
            botao = OpcaoBotao.VOLTAR
        return botao

    def obtem_posicoes(self, mapa: list,
                       tamanho: int,
                       is_bote: bool) -> tuple:
        layout = [
            self.obtem_layout_titulo('POSICIONANDO EMBARCAÇÃO'),
            self.obtem_layout_oceano(mapa),
            [sg.Text(f'** Tamanho da embarcação: {tamanho} espaço(s) **')],
            [
                sg.Text('Digite a linha e coluna iniciais:', size=35),
                sg.InputText('1', size=5, key='pos_i_linha'),
                sg.InputText('A', size=5, key='pos_i_coluna')
            ],
            [
                sg.Text('Digite a linha e coluna finais:', size=35),
                sg.InputText('1', size=5, key='pos_f_linha'),
                sg.InputText('A', size=5, key='pos_f_coluna')
            ] if not is_bote else [],
            [
                sg.Submit('Confirmar'),
                sg.Cancel('Voltar', key=OpcaoBotao.VOLTAR)
            ]
        ]

        botao, valores = self.open(layout)
        self.close()
        if not botao:
            botao = OpcaoBotao.VOLTAR

        pos_inicial = (valores['pos_i_linha'], valores['pos_i_coluna'])
        pos_final = pos_inicial if is_bote \
            else (valores['pos_f_linha'], valores['pos_f_coluna'])

        return pos_inicial, pos_final, botao

    def mostra_oceano_inicial(self, mapa: list):
        layout = [
            self.obtem_layout_titulo('SEU OCEANO'),
            self.obtem_layout_oceano(mapa),
            self.obtem_layout_opcoes([
                'Posicionar embarcações',
                'Gerar oceano aleatório',
            ])
        ]
        botao, _ = self.open(layout)
        self.close()
        if not botao:
            botao = OpcaoBotao.VOLTAR
        return botao

    def mostra_oceano(self, mapa: list):
        layout = [
            self.obtem_layout_titulo('SEU OCEANO'),
            self.obtem_layout_oceano(mapa),
            self.obtem_layout_opcoes([
                'Continuar'
            ])
        ]
        self.open(layout)
        self.close()
