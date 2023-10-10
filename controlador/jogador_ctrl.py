from tela.jogador_tela import JogadorTela
from entidade.jogador import Jogador


class JogadorCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogador_tela = JogadorTela()
        self.__jogadores = []
        self.__proximo_id = 1

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    def obter_jogador_por_id(self, id: int) -> Jogador:
        for jogador in self.jogadores:
            if jogador.id == id:
                return jogador
        self.__jogador_tela.mostra_mensagem(
            'Não existe um jogador com esse ID.')

    def logar_jogador(self) -> Jogador:
        usuario, senha = self.__jogador_tela.mostra_login_jogador()
        for jogador in self.jogadores:
            if usuario == jogador.usuario and \
                    senha == jogador.senha:
                return jogador
        self.__jogador_tela.mostra_mensagem('Usuário ou senha incorretos.')

    def mostrar_jogador(self):
        id = self.__jogador_tela.obtem_id_jogador()
        jogador = self.obter_jogador_por_id(id)
        if jogador:
            self.__jogador_tela.mostra_perfil_jogador(jogador)

    def mostrar_jogador_logado(self):
        jogador = self.__controlador_principal.jogador_logado
        if jogador:
            self.__jogador_tela.mostra_perfil_jogador(jogador)
            opcoes_acoes = {
                1: self.editar_jogador,
                2: self.excluir_jogador,
                3: self.__controlador_principal.iniciar_app,
            }

            opcao_escolhida = self.__jogador_tela.mostra_menu_perfil()
            opcoes_acoes[opcao_escolhida]()

    def cadastrar_jogador(self) -> Jogador:
        # Implementar verificacao
        nome, dia, mes, ano, usuario, senha = self.__jogador_tela\
            .mostra_cadastro_jogador()
        novo_jogador = Jogador(self.__proximo_id, nome, f'{dia}/{mes}/{ano}',
                               usuario, senha)
        self.__jogadores.append(novo_jogador)
        self.__proximo_id += 1
        return novo_jogador

    def excluir_jogador(self):
        jogador_logado = self.__controlador_principal.jogador_logado
        self.__jogadores.remove(jogador_logado)
        self.__jogador_tela.mostra_mensagem('Jogador excluido com sucesso.')
        self.__controlador_principal.logout()

    def editar_jogador(self):
        nome, dia, mes, ano, usuario, senha = self.__jogador_tela\
            .mostra_editar_jogador()
        jogador_logado = self.__controlador_principal.jogador_logado
        jogador_logado.nome = nome
        jogador_logado.data_nascimento = f'{dia}/{mes}/{ano}'
        jogador_logado.usuario = usuario
        jogador_logado.senha = senha
