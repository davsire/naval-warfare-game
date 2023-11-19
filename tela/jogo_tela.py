import string
from entidade.jogo import Vencedor
from tela.abstract_tela import AbstractTela, OpcaoBotao
from entidade.embarcacao import Embarcacao
import PySimpleGUI as sg


class JogoTela(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__letras_colunas = list(string.ascii_uppercase)

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

    def mostra_pontuacoes(self, pontuacao_jogador: int, pontuacao_pc: int):
        print('-' * 35)
        print('Pontuações:')
        print(f'Jogador: {pontuacao_jogador} - PC: {pontuacao_pc}')
        print('-' * 35)

    def mostra_fim_jogo(self, vencedor: Vencedor):
        if vencedor == Vencedor.JOGADOR:
            print('~' * 35)
            print('Parabéns!!! Você venceu a partida!')
            print('~' * 35)
        else:
            print('~' * 35)
            print('Que pena, a vitória não veio dessa vez...')
            print('~' * 35)

    def mostra_oceanos(self, mapa_jogador: list, mapa_pc: list):
        letras_colunas = self.__letras_colunas[:len(mapa_jogador)]
        print('** Seu oceano / Oceano do PC **')
        print(f'{" " * 3}{" ".join(letras_colunas)}', end='')
        print(f'{" " * 7}{" ".join(letras_colunas)}')

        for linha in range(len(mapa_jogador)):
            linha_jogador = mapa_jogador[linha]
            linha_pc = mapa_pc[linha]
            numero_linha = f'{linha + 1:<2}'

            print(f'{numero_linha}', end=' ')
            for posicao in linha_jogador:
                if isinstance(posicao, Embarcacao):
                    print(posicao.sigla.name, end=' ')
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
            [sg.Column(self.obtem_layout_lista(jogadas), scrollable=True)],
            [sg.Button('Voltar', size=10)]
        ]
        self.open(layout)
        self.close()
