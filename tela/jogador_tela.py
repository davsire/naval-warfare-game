from tela.abstract_tela import AbstractTela


class JogadorTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_login_jogador(self):
        self.mostra_titulo('LOGANDO JOGAR')
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        return usuario, senha

    def obtem_dados_jogador(self):
        nome = input('Digite seu nome: ')
        dia, mes, ano = input(
                'Digite sua data de nascimento separada por espaços: ').split()
        usuario = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')
        return nome, dia, mes, ano, usuario, senha

    def obtem_id_jogador(self) -> int:
        id = int(input('Digite o id do jogador: '))
        return id

    def mostra_cadastro_jogador(self):
        self.mostra_titulo('CADASTRANDO JOGADOR')
        nome, dia, mes, ano, usuario, senha = self.obtem_dados_jogador()
        return nome, dia, mes, ano, usuario, senha

    def mostra_edicao_jogador(self):
        self.mostra_titulo('EDITANDO JOGADOR')
        self.obtem_dados_jogador()

    def mostra_perfil_jogador(self, id: int, nome: str, data_nascimento: str):
        # Temporario
        self.mostra_mensagem(f'Jogador{id} - Nome: {nome}, Data de Nascimento: {data_nascimento}')
