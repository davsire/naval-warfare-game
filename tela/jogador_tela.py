from tela.abstract_tela import AbstractTela
from entidade.jogador import Jogador


class JogadorTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_login_jogador(self) -> tuple:
        self.mostra_titulo('LOGIN JOGADOR')
        usuario = self.obtem_informacao('Digite seu usuario: ').strip()
        senha = self.obtem_informacao('Digite sua senha: ').strip()
        return usuario, senha

    def obtem_id_jogador(self) -> int:
        while True:
            try:
                id_jogador = int(input('Digite o ID do jogador: '))
                return id_jogador
            except ValueError:
                print('Digite um ID válido!')

    def mostra_perfil_jogador(self, jogador: Jogador):
        self.mostra_titulo('PERFIL DE JOGADOR')
        self.mostra_mensagem('-'*35)
        self.mostra_mensagem(f'ID: {jogador.id}\n'
                             f'Nome: {jogador.nome}\n'
                             f'Data de Nascimento: {jogador.data_nascimento}\n'
                             f'Nome de usuário: {jogador.usuario}')
        self.mostra_mensagem('-'*35)

    def mostra_historico_jogos(self, jogador: Jogador):
        self.mostra_titulo('HISTÓRICO DE JOGOS')
        self.mostra_mensagem('-' * 35)
        if len(jogador.jogos):
            for index, jogo in enumerate(jogador.jogos, start=1):
                print(f'{index} - ID: {jogo.id} - '
                      f'Vencedor: {jogo.vencedor.name} - '
                      f'Data: {jogo.data_hora}')
        else:
            self.mostra_mensagem('O jogador ainda não tem jogos registrados!')
        self.mostra_mensagem('-' * 35)

    def mostra_menu_perfil(self) -> int:
        self.mostra_opcoes([
            'Histórico de Jogos',
            'Voltar ao menu'
        ])
        return self.obtem_opcao(
            'O que deseja acessar?\nSelecione uma opção: ',
            [1, 2]
        )

    def mostra_menu_perfil_logado(self) -> int:
        self.mostra_opcoes([
            'Histórico de Jogos',
            'Editar Perfil',
            'Excluir Perfil',
            'Voltar ao menu'
        ])
        return self.obtem_opcao(
            'O que deseja acessar?\nSelecione uma opção: ',
            [1, 2, 3, 4]
        )

    def mostra_menu_historico_jogo(self) -> int:
        self.mostra_opcoes([
            'Acessar relatório de jogo',
            'Voltar ao menu'
        ])
        return self.obtem_opcao(
            'O que deseja acessar?\nSelecione uma opção: ',
            [1, 2]
        )
