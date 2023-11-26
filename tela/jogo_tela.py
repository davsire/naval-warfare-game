import string
from entidade.jogo import Vencedor
from tela.abstract_tela import AbstractTela, OpcaoBotao
from entidade.embarcacao import Embarcacao, SiglaEmbarcacao
import PySimpleGUI as sg


class JogoTela(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__letras_colunas = list(string.ascii_uppercase)
        self.__cores_mapa = {
            SiglaEmbarcacao.B.name: '#ebbb78',
            SiglaEmbarcacao.S.name: '#7bf263',
            SiglaEmbarcacao.F.name: '#9a74e8',
            SiglaEmbarcacao.P.name: '#86b4e3',
            'X': 'red',
            '*': 'white',
            '~': '#4a9ee0',
        }

    def obtem_id_jogo(self) -> tuple:
        dados = {'id_jogo': 'Digite o ID do jogo:'}
        while True:
            layout = [
                *self.obtem_layout_titulo('BUSCAR JOGO'),
                *self.obtem_layout_obtem_dados(dados, 'Buscar')
            ]
            botao, valores = self.open(layout)
            self.close()
            if botao == OpcaoBotao.VOLTAR or not botao:
                return OpcaoBotao.VOLTAR, None
            try:
                id_jogo = int(valores['id_jogo'])
                return botao, id_jogo
            except ValueError:
                self.mostra_mensagem('Digite um ID válido!')

    def obtem_sigla_mapa_jogador(self, posicao_mapa) -> str:
        if isinstance(posicao_mapa, Embarcacao):
            return posicao_mapa.sigla.name
        elif isinstance(posicao_mapa, str):
            return posicao_mapa
        elif not posicao_mapa:
            return '~'
        return 'X'

    def obtem_sigla_mapa_pc(self, posicao_mapa) -> str:
        if isinstance(posicao_mapa, Embarcacao) or not posicao_mapa:
            return '~'
        elif isinstance(posicao_mapa, list):
            embarcacao = posicao_mapa[0]
            return embarcacao.sigla_escondida()
        return posicao_mapa

    def obtem_layout_oceano(self,
                            mapa: list,
                            obtem_sigla_func,
                            permite_acao=False):
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
                    sg.Button(obtem_sigla_func(posicao),
                              key=f'{index_linha}-{index_coluna}'
                              if permite_acao else None,
                              size=(3, 2),
                              p=(2, 2),
                              disabled=(not permite_acao),
                              button_color=(
                                  self.__cores_mapa[obtem_sigla_func(posicao)],
                                  'darkblue'
                              ),
                              disabled_button_color=(
                                  self.__cores_mapa[obtem_sigla_func(posicao)],
                                  'darkblue'
                              ))
                    for index_coluna, posicao in enumerate(linha)
                ]
            ]
            for index_linha, linha in enumerate(mapa)
        ]

        return layout_header + layout_mapa

    def mostra_fim_jogo(self, vencedor: Vencedor):
        resultado = 'Parabéns!!! Você venceu a partida!' \
                    if vencedor == Vencedor.JOGADOR else \
                    'Que pena, a vitória não veio dessa vez...'

        layout = [
            [sg.Text('~' * 55)],
            [sg.Text(resultado)],
            [sg.Text('~' * 55)],
            [sg.Button('Continuar')]
        ]

        self.open(layout)
        self.close()

    def mostra_situacao_jogo(self,
                             mapa_jogador: list,
                             mapa_pc: list,
                             pontuacao_jogador: int,
                             pontuacao_pc: int,
                             permite_acao: bool,
                             timeout_tela: int):
        layout = [
            self.obtem_layout_titulo('PREPARAR CANHÕES! ATIRAR!'),
            [sg.Text('-' * 55)],
            [sg.Text('Pontuações:')],
            [sg.Text(f'Jogador: {pontuacao_jogador} - PC: {pontuacao_pc}')],
            [sg.Text('-' * 55)],
            [sg.Text('** Seu oceano / Oceano do PC **')],
            [
                sg.Column(self.obtem_layout_oceano(
                    mapa_jogador, self.obtem_sigla_mapa_jogador, False
                )),
                sg.Column(self.obtem_layout_oceano(
                    mapa_pc, self.obtem_sigla_mapa_pc, permite_acao
                ))
            ],
            [sg.Text(
                '** Clique em uma posição no mapa adversário para atirar **'
            )] if permite_acao else []
        ]

        botao, _ = self.open(layout, timeout_tela)
        if not botao:
            botao = OpcaoBotao.VOLTAR
        else:
            botao = (int(coord) for coord in botao.split('-'))
        self.close()
        return botao

    def mostra_oceanos(self, mapa_jogador: list, mapa_pc: list):
        layout = [
            self.obtem_layout_titulo('MAPAS FINAIS DA PARTIDA'),
            [sg.Text('** Seu oceano / Oceano do PC **')],
            [
                sg.Column(self.obtem_layout_oceano(
                    mapa_jogador, self.obtem_sigla_mapa_jogador, False
                )),
                sg.Column(self.obtem_layout_oceano(
                    mapa_pc, self.obtem_sigla_mapa_pc, False
                ))
            ],
            [sg.Button('Voltar', size=10)],
        ]

        self.open(layout)
        self.close()

    def mostra_relatorio_jogo(self,
                              id_jogo: int,
                              jogador_nome: str,
                              jogador_usuario: str,
                              vencedor: str,
                              data_hora: str,
                              pontuacao_jogador: int,
                              pontuacao_pc: int):
        dados = {
            'ID': id_jogo,
            'Jogador': f'{jogador_nome} ({jogador_usuario})',
            'Vencedor': vencedor,
            'Data': data_hora,
            'Pontuação do jogador': pontuacao_jogador,
            'Pontuação do PC': pontuacao_pc
        }
        layout = [
            *self.obtem_layout_titulo('RELATÓRIO DE JOGO'),
            *self.obtem_layout_mostra_dados(dados),
            *self.obtem_layout_opcoes([
                'Visualizar mapas finais da partida',
                'Visualizar jogadas da partida',
                'Voltar ao menu'
            ])
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 3
        self.close()
        return opcao_escolhida


    def mostra_jogadas(self, jogadas: list):
        layout = [
            *self.obtem_layout_titulo('JOGADAS DA PARTIDA'),
            [sg.Column(self.obtem_layout_lista(jogadas),
                       scrollable=True,
                       vertical_scroll_only=True)],
            [sg.Button('Voltar', size=10)]
        ]
        self.open(layout)
        self.close()
