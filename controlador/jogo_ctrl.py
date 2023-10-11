from entidade.jogo import Jogo
from tela.jogo_tela import JogoTela


class JogoCtrl:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogo_tela = JogoTela()
        self.__jogos = []
        self.__proximo_id = 1

    @property
    def jogos(self):
        return self.__jogos

    def iniciar_jogo(self):
        oceano_jogador, oceano_pc = self.__controlador_principal\
            .oceano_ctrl.cadastrar_oceano()

        novo_jogo = Jogo(self.__proximo_id, oceano_jogador, oceano_pc)
        self.__proximo_id += 1
        self.__jogos.append(novo_jogo)
        self.__controlador_principal.jogador_logado.jogos.append(novo_jogo)
