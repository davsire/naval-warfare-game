from tela.jogador_tela import JogadorTela
from entidade.jogador import Jogador


class JogadorCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogador_tela = JogadorTela()
        self.__jogadores = []

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    def obter_jogador_por_id(self, id: int) -> Jogador:
        for jogador in self.jogadores:
            if jogador.id == id:
                return jogador
        self.__jogador_tela.mostra_mensagem(
                'Não existe um jogador com esse ID.')

    def logar_jogador(self):
        usuario, senha = self.__jogador_tela.mostra_login_jogador()
        print(senha)
        for jogador in self.jogadores:
            if usuario == jogador.usuario and \
                senha == jogador.senha:
                return jogador
            else:
                self.__jogador_tela.mostra_mensagem(
                        'Usuário ou senha incorretos.')

    def mostrar_jogador(self):
        pass

    def cadastrar_jogador(self):
        pass

    def excluir_jogador(self, jogador_logado: Jogador):
        for jogador in self.jogadores:
            if jogador == jogador_logado:
                del self.jogadores[jogador]
                self.__jogador_tela.mostra_mensagem(
                        'Jogador excluido com sucesso.')

    def editar_jogador(self, jogador_logado: Jogador):
        pass
