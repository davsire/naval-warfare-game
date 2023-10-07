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
        pass

    def obtem_id_jogador(self) -> int:
        pass

    def mostra_cadastro_jogador(self):
        pass

    def mostra_edicao_jogador(self):
        pass

    def mostra_perfil_jogador(self):
        pass
