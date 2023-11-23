from tela.abstract_tela import AbstractTela, OpcaoBotao
import PySimpleGUI as sg


class JogadorTela(AbstractTela):
    def __init__(self):
        super().__init__()

    def mostra_login_jogador(self) -> tuple:
        dados = {
            'usuario': 'Digite seu usuário: ',
            'senha': 'Digite sua senha: ',
        }
        layout = [
            *self.obtem_layout_titulo('LOGIN JOGADOR'),
            *self.obtem_layout_obtem_dados(dados, 'Login')
        ]

        botao, valores = self.open(layout)
        if not botao:
            botao = OpcaoBotao.VOLTAR
        self.close()
        return botao, valores

    def mostra_obter_informacoes_jogador(self, label_confirmar: str, dados_atuais: dict):
        dados = {
            'nome': 'Digite seu nome: ',
            'data_nasc': 'Digite sua data de nascimento',
            'usuario': 'Digite seu usuário: ',
            'senha': 'Digite sua senha: ',
        }
        layout = [
            *self.obtem_layout_titulo('CADASTRO JOGADOR'),
            *self.obtem_layout_obtem_dados(dados, label_confirmar, dados_atuais)
        ]
        botao, valores = self.open(layout)
        if not botao:
            botao = OpcaoBotao.VOLTAR
        self.close()
        return botao, valores

    def obtem_id_jogador(self) -> tuple:
        dados = {'id_jogador': 'Digite o ID do jogador:'}
        while True:
            layout = [
                *self.obtem_layout_titulo('BUSCAR JOGADOR'),
                *self.obtem_layout_obtem_dados(dados, 'Buscar')
            ]
            botao, valores = self.open(layout)
            self.close()
            if botao == OpcaoBotao.VOLTAR or not botao:
                return OpcaoBotao.VOLTAR, None
            try:
                id_jogador = int(valores['id_jogador'])
                return botao, id_jogador
            except ValueError:
                self.mostra_mensagem('Digite um ID válido!')

    def mostra_perfil_jogador(self,
                              id_jogador: int,
                              nome: str,
                              data_nascimento: str,
                              usuario: str,
                              pontuacao_total: int,
                              is_logado: bool = False):
        dados = {
            'ID': id_jogador,
            'Nome': nome,
            'Data de Nascimento': data_nascimento,
            'Nome de usuário': usuario,
            'Pontuação total': pontuacao_total,
        }
        opcoes = [
            'Histórico de jogos',
            'Voltar ao menu'
        ]
        if is_logado:
            opcoes.insert(1, 'Editar perfil')
            opcoes.insert(2, 'Excluir perfil')
        layout = [
            *self.obtem_layout_titulo('PERFIL DE JOGADOR'),
            *self.obtem_layout_mostra_dados(dados),
            *self.obtem_layout_opcoes(opcoes),
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 4
        self.close()
        return opcao_escolhida

    def mostra_excluir_jogador(self, mensagem):
        layout = [
            self.confirma_acao(mensagem, 'Excluir')
        ]
        botao, valores = self.open(layout)
        self.close()
        if botao == 'Excluir':
            return True
        else:
            return False

    def mostra_historico_jogos(self, jogos: list):
        layout = [
            *self.obtem_layout_titulo('HISTÓRICO DE JOGOS'),
            *self.obtem_layout_lista(jogos),
            *self.obtem_layout_opcoes([
                'Acessar relatório de jogo',
                'Voltar ao menu'
            ])
        ]

        opcao_escolhida, _ = self.open(layout)
        if not opcao_escolhida:
            opcao_escolhida = 2
        self.close()
        return opcao_escolhida
