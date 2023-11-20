from tela.jogador_tela import JogadorTela
from tela.abstract_tela import OpcaoBotao
from dao.jogador_dao import JogadorDAO
from entidade.jogador import Jogador
from exception.nao_encontrado_error import NaoEncontradoErro


class JogadorCtrl:
    __instancia = None

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogador_tela = JogadorTela()
        self.__jogador_dao = JogadorDAO()

    def __new__(cls, controlador_principal):
        if JogadorCtrl.__instancia is None:
            JogadorCtrl.__instancia = object.__new__(cls)
        return JogadorCtrl.__instancia

    @property
    def __proximo_id(self):
        ultimo_id = max([jogador.id for jogador in self.jogadores], default=0)
        return ultimo_id + 1

    @property
    def jogadores(self) -> list:
        return self.__jogador_dao.get_all()

    def obter_jogador_por_id(self, id_jogador: int) -> Jogador:
        try:
            return self.__jogador_dao.get(id_jogador)
        except NaoEncontradoErro as e:
            self.__jogador_tela.mostra_mensagem(e)

    def salvar_jogador(self, jogador: Jogador):
        self.__jogador_dao.add(jogador)

    def remover_jogador(self, jogador: Jogador):
        try:
            self.__jogador_dao.remove(jogador)
            for jogo in jogador.jogos:
                self.__controlador_principal.jogo_ctrl.remover_jogo(jogo)
        except NaoEncontradoErro as e:
            self.__jogador_tela.mostra_mensagem(e)

    def logar_jogador(self) -> Jogador:
        while True:
            opcao, dados = self.__jogador_tela.mostra_login_jogador()
            if opcao == OpcaoBotao.VOLTAR:
                self.__controlador_principal.iniciar_app()
            for jogador in self.jogadores:
                if dados['usuario'] == jogador.usuario and \
                        dados['senha'] == jogador.senha:
                    return jogador
            self.__jogador_tela.mostra_mensagem('Usuário ou senha incorretos.')

    def mostrar_jogador(self, jogador: Jogador = None):
        if not jogador:
            id_jogador = self.__jogador_tela.obtem_id_jogador()
            jogador = self.obter_jogador_por_id(id_jogador)
        if jogador:
            is_logado = jogador == self.__controlador_principal.jogador_logado
            voltar_menu = self.__controlador_principal.iniciar_app
            opcoes_acoes = {
                1: self.mostrar_historico_jogos,
                2: self.editar_jogador if is_logado else voltar_menu,
                3: self.excluir_jogador,
                4: voltar_menu,
            }
            while True:
                opcao_escolhida = self.__jogador_tela.mostra_perfil_jogador(
                    jogador.id,
                    jogador.nome,
                    jogador.data_nascimento,
                    jogador.usuario,
                    jogador.pontuacao_total,
                    is_logado
                )
                if opcao_escolhida == 1:
                    opcoes_acoes[opcao_escolhida](jogador)
                else:
                    opcoes_acoes[opcao_escolhida]()

    def tratar_usario(self) -> str:
        jogador_logado = self.__controlador_principal.jogador_logado
        usuarios = [jogador.usuario for jogador in self.jogadores]
        while True:
            usuario = self.__jogador_tela.obtem_informacao(
                'Digite seu usuário: ').strip()
            if usuario not in usuarios or \
                    (jogador_logado and jogador_logado.usuario == usuario):
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
        senha = self.__jogador_tela.obtem_informacao(
            'Digite sua senha: ').strip()
        return nome, data_nascimento, usuario, senha

    def cadastrar_jogador(self) -> Jogador:
        self.__jogador_tela.mostra_titulo('CADASTRANDO JOGADOR')
        nome, data_nasc, usuario, senha = self.obter_informacoes_jogador()
        novo_jogador = Jogador(self.__proximo_id, nome, data_nasc,
                               usuario, senha)
        self.salvar_jogador(novo_jogador)
        return novo_jogador

    def excluir_jogador(self):
        self.__jogador_tela.mostra_mensagem('** Ao excluir sua conta, os '
                                            'registros dos seus jogos serão '
                                            'perdidos! **')
        confirmacao = self.__jogador_tela.confirma_acao(
            'Tem certeza que deseja excluir sua conta?'
        )
        if confirmacao:
            jogador_logado = self.__controlador_principal.jogador_logado
            self.remover_jogador(jogador_logado)
            self.__jogador_tela.mostra_mensagem(
                'Jogador excluído com sucesso!'
            )
            self.__controlador_principal.logout()

    def editar_jogador(self):
        self.__jogador_tela.mostra_titulo('EDITANDO JOGADOR')
        nome, data_nasc, usuario, senha = self.obter_informacoes_jogador()
        jogador_logado = self.__controlador_principal.jogador_logado
        jogador_logado.nome = nome
        jogador_logado.data_nascimento = data_nasc
        jogador_logado.usuario = usuario
        jogador_logado.senha = senha
        self.salvar_jogador(jogador_logado)

    def mostrar_historico_jogos(self, jogador: Jogador):
        opcoes_acoes = {
            1: self.__controlador_principal.jogo_ctrl.mostrar_relatorio_jogo,
            2: self.__controlador_principal.iniciar_app
        }
        jogos = [
            f'ID: {jogo.id} - '
            f'Vencedor: {jogo.vencedor.name if jogo.vencedor else "~"} - '
            f'Data: {jogo.data_hora}'
            for jogo in jogador.jogos
        ]
        if not len(jogos):
            jogos.append('O jogador ainda não tem jogos registrados!')
        while True:
            opcao_escolhida = self.__jogador_tela.mostra_historico_jogos(jogos)
            opcoes_acoes[opcao_escolhida]()
