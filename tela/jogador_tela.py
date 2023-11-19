from tela.abstract_tela import AbstractTela, OpcaoBotao
import PySimpleGUI as sg


class JogadorTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_login_jogador(self) -> tuple:
        dados = {
            'usuario': 'Digite seu usuário: ',
            'senha': 'Digite sua senha: ',
        }
        layout = [
            *self.obtem_layout_titulo('LOGIN JOGADOR'),
            *self.obtem_layout_obtem_dados(dados, 'Login')
        ]

        self._window = sg.Window('Batalha Naval',
                                 layout,
                                 element_justification='center')
        botao, valores = self.open()
        if not botao:
            botao = OpcaoBotao.VOLTAR
        self.close()
        return botao, valores

    def obtem_id_jogador(self) -> int:
        while True:
            try:
                id_jogador = int(input('Digite o ID do jogador: '))
                return id_jogador
            except ValueError:
                self.mostra_mensagem('Digite um ID válido!')

    def mostra_perfil_jogador(self,
                              id_jogador: int,
                              nome: str,
                              data_nascimento: str,
                              usuario: str,
                              pontuacao_total: int,
                              is_logado: bool = False):
        dados = {
            'ID': id_jogador,
            'Nome': nome,
            'Data de Nascimento': data_nascimento,
            'Nome de usuário': usuario,
            'Pontuação total': pontuacao_total,
        }
        opcoes = [
            'Histórico de jogos',
            'Voltar ao menu'
        ]
        if is_logado:
            opcoes.insert(1, 'Editar perfil')
            opcoes.insert(2, 'Excluir perfil')
        layout = [
            *self.obtem_layout_titulo('PERFIL DE JOGADOR'),
            *self.obtem_layout_mostra_dados(dados),
            *self.obtem_layout_opcoes(opcoes),
        ]

        self._window = sg.Window('Batalha Naval',
                                 layout,
                                 element_justification='center')
        opcao_escolhida, _ = self.open()
        if not opcao_escolhida:
            opcao_escolhida = 4
        self.close()
        return opcao_escolhida

    def mostra_historico_jogos(self, jogos: list):
        self.mostra_titulo('HISTÓRICO DE JOGOS')
        self.mostra_mensagem('-' * 35)
        if len(jogos):
            for index, jogo in enumerate(jogos, start=1):
                vencedor = jogo.vencedor.name if jogo.vencedor else '~'
                print(f'{index} - ID: {jogo.id} - '
                      f'Vencedor: {vencedor} - '
                      f'Data: {jogo.data_hora}')
        else:
            self.mostra_mensagem('O jogador ainda não tem jogos registrados!')
        self.mostra_mensagem('-' * 35)

    def mostra_menu_historico_jogo(self) -> int:
        self.mostra_opcoes([
            'Acessar relatório de jogo',
            'Voltar ao menu'
        ])
        return self.obtem_opcao(
            'O que deseja acessar?\nSelecione uma opção: ',
            [1, 2]
        )
