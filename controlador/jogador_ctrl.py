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
            opcao, id_jogador = self.__jogador_tela.obtem_id_jogador()
            if opcao == OpcaoBotao.VOLTAR:
                return
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

    def tratar_usario(self, usuario) -> bool:
        jogador_logado = self.__controlador_principal.jogador_logado
        usuarios = [jogador.usuario for jogador in self.jogadores]
        return usuario not in usuarios or \
            (jogador_logado and jogador_logado.usuario == usuario)

    def tratar_data_nascimento(self, data_nasc: str) -> bool:
        try:
            dia, mes, ano = data_nasc.split()
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            if not (0 < dia < 32) or not (0 < mes < 13) or \
                    not (ano > 0):
                raise ValueError
            return True
        except ValueError:
            return False

    def valida_dados(self, dados: dict):
        erros = []
        if not self.tratar_data_nascimento(dados['data_nasc']):
            erros.append('A data de nascimento está inválida!')
        if not self.tratar_usario(dados['usuario']):
            erros.append('O nome de usuário ja está em uso!')
        if '' in dados.values():
            erros.append('Todos os campos devem ser preenchidos!')

        if len(erros):
            self.__jogador_tela.mostra_mensagem('\n---\n'.join(erros))
        return not len(erros)

    def obter_informacoes_jogador(self, acao: str, dados_atuais) -> tuple:
        while True:
            opcao, dados = self.__jogador_tela\
                .mostra_obter_informacoes_jogador(acao, dados_atuais)
            dados_atuais = dados
            if opcao == OpcaoBotao.VOLTAR:
                self.__controlador_principal.iniciar_app()
            if self.valida_dados(dados):
                break
        return dados['nome'], dados['data_nasc'],\
            dados['usuario'], dados['senha']

    def cadastrar_jogador(self) -> Jogador:
        dados_atuais = {}
        nome, data_nasc, usuario, senha = self.obter_informacoes_jogador(
            'Cadastrar', dados_atuais
        )
        novo_jogador = Jogador(self.__proximo_id, nome, data_nasc,
                               usuario, senha)
        self.salvar_jogador(novo_jogador)
        self.__jogador_tela.mostra_mensagem('Jogador cadastrado com sucesso!')
        return novo_jogador

    def excluir_jogador(self):
        confirmacao = self.__jogador_tela.mostra_excluir_jogador(
            '** Ao excluir sua conta, os registros dos seus jogos serão '
            'perdidos! ** \n\n'
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
        jogador_logado = self.__controlador_principal.jogador_logado
        dados_atuais = {
            'nome': jogador_logado.nome,
            'data_nasc': jogador_logado.data_nascimento,
            'usuario': jogador_logado.usuario,
            'senha': jogador_logado.senha,
        }
        nome, data_nasc, usuario, senha = self.obter_informacoes_jogador(
            'Editar', dados_atuais
        )
        jogador_logado.nome = nome
        jogador_logado.data_nascimento = data_nasc
        jogador_logado.usuario = usuario
        jogador_logado.senha = senha
        self.salvar_jogador(jogador_logado)
        self.__jogador_tela.mostra_mensagem('Dados alterados com sucesso!')

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
