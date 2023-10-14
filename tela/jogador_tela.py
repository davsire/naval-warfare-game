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
        id = int(self.obtem_informacao('Digite o id do jogador: '))
        return id

    def mostra_perfil_jogador(self, jogador: Jogador):
        self.mostra_mensagem('-'*35)
        self.mostra_mensagem(f'ID: {jogador.id}\n'
                             f'Nome: {jogador.nome}\n'
                             f'Data de Nascimento: {jogador.data_nascimento}\n'
                             f'Nome de usuário: {jogador.usuario}')
        self.mostra_mensagem('-'*35)

    def mostra_historico_jogos(self, jogador: Jogador):
        # Implementar
        self.mostra_titulo('HISTÓRICO DE JOGOS')
        
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
