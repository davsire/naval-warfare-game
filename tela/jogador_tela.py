from tela.abstract_tela import AbstractTela
from entidade.jogador import Jogador


class JogadorTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_login_jogador(self) -> tuple:
        self.mostra_titulo('LOGIN JOGADOR')
        usuario = input('Digite seu usuario: ').strip()
        senha = input('Digite sua senha: ').strip()
        return usuario, senha

    def obtem_dados_jogador(self) -> tuple:
        nome = input('Digite seu nome: ')
        dia, mes, ano = input(
                'Digite sua data de nascimento separada por espaços: ').split()
        usuario = input('Digite seu usuário: ').strip()
        senha = input('Digite sua senha: ').strip()
        return nome, dia, mes, ano, usuario, senha

    def obtem_id_jogador(self) -> int:
        id = int(input('Digite o id do jogador: '))
        return id

    def mostra_cadastro_jogador(self) -> tuple:
        self.mostra_titulo('CADASTRANDO JOGADOR')
        return self.obtem_dados_jogador()

    def mostra_edicao_jogador(self):
        # Implementar
        self.mostra_titulo('EDITANDO JOGADOR')
        self.obtem_dados_jogador()

    def mostra_perfil_jogador(self, jogador: Jogador):
        # Temporario
        self.mostra_mensagem(f'Jogador ID:{jogador.id} - Nome: {jogador.nome}, Data de Nascimento: {jogador.data_nascimento}')
