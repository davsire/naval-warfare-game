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

    def mostrar_jogador(self) -> Jogador:
        id = self.__jogador_tela.obtem_id_jogador()
        jogador = self.obter_jogador_por_id(id)
        if jogador:
            self.__jogador_tela.mostra_perfil_jogador(jogador)
            return jogador

    def mostrar_jogador_logado(self):
        jogador = self.__controlador_principal.jogador_logado
        if jogador:
            self.__jogador_tela.mostra_perfil_jogador(jogador)
            opcoes_acoes = {
                1: self.mostrar_historico_jogos_logado,
                2: self.editar_jogador,
                3: self.excluir_jogador,
                4: self.__controlador_principal.iniciar_app,
            }

            opcao_escolhida = self.__jogador_tela.mostra_menu_perfil_logado()
            opcoes_acoes[opcao_escolhida]()

    def tratar_usario(self) -> str:
        usuarios = [jogador.usuario for jogador in self.jogadores]
        controlador_principal = self.__controlador_principal
        while True:
            usuario = self.__jogador_tela.obtem_informacao(
            'Digite seu usuário: ').strip()
            if controlador_principal.jogador_logado == None and\
                    usuario not in usuarios:
                return usuario
            elif usuario == controlador_principal.jogador_logado.usuario:
                return usuario
            elif usuario != controlador_principal.jogador_logado.usuario and\
                    usuario not in usuarios:
                return usuario
            else:
                self.__jogador_tela.mostra_mensagem(
                    'Nome de usuário já está em uso...')

    def tratar_data_nascimento(self) -> str:
        while True:
            try:
                dia, mes, ano = self.__jogador_tela.obtem_informacao(
                    f'Digite sua data de nascimento '
                    f'separada por espaços (ex: 01 01 2000): ').split()
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                if not (0 < dia < 32) or not (0 < mes < 13) or\
                        not (ano > 0):
                    raise ValueError
                return f'{dia}/{mes}/{ano}'
            except ValueError:
                self.__jogador_tela.mostra_mensagem(
                    'Data de nascimento inválida!')

    def obter_informacoes_jogador(self) -> tuple:
        nome = self.__jogador_tela.obtem_informacao(
            'Digite seu nome: ')
        data_nascimento = self.tratar_data_nascimento()
        usuario = self.tratar_usario()
        senha = input('Digite sua senha: ').strip()
        return nome, data_nascimento, usuario, senha

    def cadastrar_jogador(self) -> Jogador:
        self.__jogador_tela.mostra_titulo('CADASTRANDO JOGADOR')
        nome, data_nascimento, usuario, senha = self.obter_informacoes_jogador()
        novo_jogador = Jogador(self.__proximo_id, nome, data_nascimento,
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
        self.__jogador_tela.mostra_titulo('EDITANDO JOGADOR')
        nome, data_nascimento, usuario, senha = self.obter_informacoes_jogador()
        jogador_logado = self.__controlador_principal.jogador_logado
        jogador_logado.nome = nome
        jogador_logado.data_nascimento = data_nascimento
        jogador_logado.usuario = usuario
        jogador_logado.senha = senha

    def mostrar_historico_jogos_logado(self):
        jogador = self.__controlador_principal.jogador_logado
        self.__jogador_tela.mostra_historico_jogos(jogador)

    def mostrar_historico_jogos(self, jogador: Jogador):
        self.__jogador_tela.mostra_historico_jogos(jogador)
