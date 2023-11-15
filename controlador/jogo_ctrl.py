import random
from time import sleep
from entidade.jogo import Jogo, Vencedor
from entidade.embarcacao import Embarcacao
from tela.jogo_tela import JogoTela
from dao.jogo_dao import JogoDAO
from exception.nao_encontrado_error import NaoEncontradoErro


class JogoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogo_tela = JogoTela()
        self.__jogo_dao = JogoDAO()
        self.__mensagens_acerto = ['Tiro certeiro!',
                                   'Acertou em cheio!',
                                   'Embarcação atingida!']
        self.__mensagens_erro = ['Direto no mar...',
                                 'Acertou algum peixe...',
                                 'Nenhuma ebarcação atingida...']

    @property
    def __proximo_id(self):
        ultimo_id = max([jogo.id for jogo in self.jogos], default=0)
        return ultimo_id + 1

    @property
    def jogos(self):
        return self.__jogo_dao.get_all()

    def obter_jogo_por_id(self, id_jogo: int):
        try:
            return self.__jogo_dao.get(id_jogo)
        except NaoEncontradoErro as e:
            self.__jogo_tela.mostra_mensagem(e)

    def salvar_jogo(self, jogo: Jogo):
        jogador = self.__controlador_principal.jogador_logado
        jogador.jogos.append(jogo)
        self.__jogo_dao.add(jogo)
        self.__controlador_principal.jogador_ctrl.salvar_jogador(jogador)

    def remover_jogo(self, jogo: Jogo):
        try:
            self.__jogo_dao.remove(jogo)
            self.__controlador_principal.oceano_ctrl\
                .remover_oceano(jogo.oceano_jogador)
            self.__controlador_principal.oceano_ctrl\
                .remover_oceano(jogo.oceano_pc)
        except NaoEncontradoErro as e:
            self.__jogo_tela.mostra_mensagem(e)

    def iniciar_jogo(self):
        jogador_logado = self.__controlador_principal.jogador_logado
        oceano_jogador, oceano_pc = self.__controlador_principal\
            .oceano_ctrl.cadastrar_oceano()

        novo_jogo = Jogo(self.__proximo_id, jogador_logado,
                         oceano_jogador, oceano_pc)

        self.__jogo_tela.mostra_titulo('PREPARAR CANHÕES! ATIRAR!')
        self.executar_jogadas(novo_jogo)

    def mostrar_situacao_jogo(self, jogo: Jogo):
        self.__jogo_tela.mostra_pontuacoes(jogo.pontuacao_jogador,
                                           jogo.pontuacao_pc)
        self.__jogo_tela.mostra_oceanos(jogo.oceano_jogador.mapa,
                                        jogo.oceano_pc.mapa)

    def executar_jogadas(self, jogo: Jogo):
        self.mostrar_situacao_jogo(jogo)
        self.executar_jogada_jogador(jogo)
        if not jogo.vencedor:
            self.executar_jogada_pc(jogo)
        if jogo.vencedor:
            self.__jogo_tela.mostra_fim_jogo(jogo.vencedor)
            self.salvar_jogo(jogo)
            return
        self.executar_jogadas(jogo)

    def verificar_vitoria(self, jogo: Jogo) -> bool:
        vencedor = None
        if not self.existe_embarcacao_mapa(jogo.oceano_jogador.mapa):
            vencedor = Vencedor.PC
        if not self.existe_embarcacao_mapa(jogo.oceano_pc.mapa):
            vencedor = Vencedor.JOGADOR
        if vencedor:
            jogo.vencedor = vencedor
        return bool(vencedor)

    def existe_embarcacao_mapa(self, mapa: list) -> bool:
        posicoes_mapa = [coluna for linha in mapa for coluna in linha]
        return any([isinstance(posicao, Embarcacao)
                    for posicao
                    in posicoes_mapa])

    def executar_jogada_jogador(self, jogo: Jogo):
        while True:
            try:
                linha, coluna = self.obter_posicao_tiro(jogo)
                acertou = self.computar_tiro(linha, coluna, jogo)
                existe_vencedor = self.verificar_vitoria(jogo)
                self.mostrar_situacao_jogo(jogo)
                if not acertou or existe_vencedor:
                    return
            except ValueError:
                self.__jogo_tela.mostra_mensagem('Você já atirou aqui! '
                                                 'Tente novamente')

    def executar_jogada_pc(self, jogo: Jogo):
        while True:
            try:
                sleep(1)
                linha, coluna = self.obter_posicao_aleatoria(jogo)
                acertou = self.computar_tiro(linha, coluna, jogo, True)
                existe_vencedor = self.verificar_vitoria(jogo)
                self.mostrar_situacao_jogo(jogo)
                if not acertou or existe_vencedor:
                    return
            except ValueError:
                pass

    def obter_posicao_tiro(self, jogo: Jogo) -> tuple:
        tamanho_oceano = jogo.oceano_jogador.tamanho
        self.__jogo_tela.mostra_mensagem('Onde desejar atirar?')
        linha, coluna = self.__controlador_principal\
            .oceano_ctrl.obter_posicao(tamanho_oceano)
        return linha, coluna

    def obter_posicao_aleatoria(self, jogo: Jogo) -> tuple:
        tamanho_oceano = jogo.oceano_jogador.tamanho
        linha = random.randrange(tamanho_oceano)
        coluna = random.randrange(tamanho_oceano)
        return linha, coluna

    def computar_tiro(self,
                      linha: int,
                      coluna: int,
                      jogo: Jogo,
                      is_pc: bool = False) -> bool:
        oceano = jogo.oceano_jogador if is_pc else jogo.oceano_pc
        posicao_tiro = oceano.mapa[linha][coluna]
        if isinstance(posicao_tiro, Embarcacao):
            self.computar_acerto(jogo, posicao_tiro, is_pc)
            oceano.mapa[linha][coluna] = [posicao_tiro]
            return True
        elif not posicao_tiro:
            self.computar_erro(jogo, is_pc)
            oceano.mapa[linha][coluna] = '*'
            return False
        else:
            raise ValueError

    def computar_acerto(self, jogo: Jogo, embarcacao: Embarcacao, is_pc: bool):
        jogador_logado = self.__controlador_principal.jogador_logado
        indice_mensagem = random.randrange(len(self.__mensagens_acerto))
        mensagem = self.__mensagens_acerto[indice_mensagem]
        self.__jogo_tela.mostra_mensagem(
            f'{"PC: " if is_pc else "VOCÊ: "}{mensagem}'
        )

        embarcacao.tomar_dano()
        pontuacao = 1
        if embarcacao.afundou:
            pontuacao += 3
            self.__jogo_tela.mostra_mensagem(f'{"PC: " if is_pc else "VOCÊ: "}'
                                             'Embarcação afundada!')

        if is_pc:
            jogo.aumentar_pontuacao_pc(pontuacao)
            jogo.adicionar_jogada_pc(True, embarcacao.afundou, pontuacao)
        else:
            jogador_logado.aumenta_pontuacao_total(pontuacao)
            jogo.aumentar_pontuacao_jogador(pontuacao)
            jogo.adicionar_jogada_jogador(True, embarcacao.afundou, pontuacao)

    def computar_erro(self, jogo: Jogo, is_pc: bool):
        indice_mensagem = random.randrange(len(self.__mensagens_erro))
        mensagem = self.__mensagens_erro[indice_mensagem]
        self.__jogo_tela.mostra_mensagem(
            f'{"PC: " if is_pc else "VOCÊ: "}{mensagem}'
        )

        if is_pc:
            jogo.adicionar_jogada_pc(False)
        else:
            jogo.adicionar_jogada_jogador(False)

    def mostrar_relatorio_jogo(self):
        id_jogo = self.__jogo_tela.obtem_id_jogo()
        jogo = self.obter_jogo_por_id(id_jogo)
        if jogo:
            vencedor = jogo.vencedor.name if jogo.vencedor else '~'
            self.__jogo_tela.mostra_relatorio_jogo(jogo.id,
                                                   jogo.jogador.nome,
                                                   jogo.jogador.usuario,
                                                   vencedor,
                                                   jogo.data_hora,
                                                   jogo.pontuacao_jogador,
                                                   jogo.pontuacao_pc)
            while True:
                opcao_escolhida = self.__jogo_tela.mostra_menu_relatorio_jogo()
                if opcao_escolhida == 1:
                    self.__jogo_tela.mostra_oceanos(jogo.oceano_jogador.mapa,
                                                    jogo.oceano_pc.mapa)
                elif opcao_escolhida == 2:
                    self.__jogo_tela.mostra_jogadas(jogo.jogadas)
                else:
                    self.__controlador_principal.iniciar_app()
