import random
from entidade.jogo import Jogo
from entidade.oceano import Oceano
from entidade.embarcacao import Embarcacao
from tela.jogo_tela import JogoTela


class JogoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogo_tela = JogoTela()
        self.__jogos = []
        self.__proximo_id = 1
        self.__mensagens_acerto = ['Tiro certeiro!',
                                   'Acertou em cheio!',
                                   'Embarcação atingida!']
        self.__mensagens_erro = ['Direto no mar...',
                                 'Acertou algum peixe...',
                                 'Nenhuma ebarcação atingida...']

    @property
    def jogos(self):
        return self.__jogos

    def iniciar_jogo(self):
        jogador_logado = self.__controlador_principal.jogador_logado
        oceano_jogador, oceano_pc = self.__controlador_principal\
            .oceano_ctrl.cadastrar_oceano()

        novo_jogo = Jogo(self.__proximo_id, jogador_logado,
                         oceano_jogador, oceano_pc)
        self.__proximo_id += 1
        self.__jogos.append(novo_jogo)
        jogador_logado.jogos.append(novo_jogo)

        self.__jogo_tela.mostra_titulo('PREPARAR CANHÕES! ATIRAR!')
        self.executar_jogadas(novo_jogo)

    def executar_jogadas(self, jogo: Jogo):
        self.__jogo_tela.mostra_situacao_jogo(jogo)
        self.executar_jogada_jogador(jogo)
        self.executar_jogada_pc(jogo)
        existe_vencedor = self.verificar_vitoria(jogo)
        if existe_vencedor:
            return
        self.executar_jogadas(jogo)

    def verificar_vitoria(self, jogo: Jogo) -> bool:
        pass

    def executar_jogada_jogador(self, jogo: Jogo):
        while True:
            try:
                linha, coluna = self.obter_posicao_tiro(jogo)
                acertou = self.computar_tiro(linha, coluna, jogo)
                if not acertou:
                    return
                self.__jogo_tela.mostra_situacao_jogo(jogo)
            except ValueError:
                self.__jogo_tela.mostra_mensagem('Você já atirou aqui! '
                                                 'Tente novamente')

    def executar_jogada_pc(self, jogo: Jogo):
        while True:
            try:
                linha, coluna = self.obter_posicao_aleatoria(jogo)
                acertou = self.computar_tiro(linha, coluna, jogo, True)
                if not acertou:
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
            # TODO: mudar tipo do erro
            raise ValueError

    def computar_acerto(self, jogo: Jogo, embarcacao: Embarcacao, is_pc: bool):
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
