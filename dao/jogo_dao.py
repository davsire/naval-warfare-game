from dao.dao import DAO
from entidade.jogo import Jogo
from exception.nao_encontrado_error import NaoEncontradoErro


class JogoDAO(DAO):
    __instancia = None

    def __init__(self):
        super().__init__('jogo.pkl')

    def __new__(cls):
        if JogoDAO.__instancia is None:
            JogoDAO.__instancia = object.__new__(cls)
        return JogoDAO.__instancia
    
    def add(self, jogo: Jogo):
        if isinstance(jogo, Jogo) and isinstance(jogo.id, int):
            super().add(jogo.id, jogo)

    def get(self, id_jogo: int):
        try:
            if isinstance(id_jogo, int):
                return super().get(id_jogo)
        except KeyError:
            raise NaoEncontradoErro('jogo')

    def remove(self, jogo: Jogo):
        try:
            if isinstance(jogo, Jogo) and isinstance(jogo.id, int):
                super().remove(jogo.id)
        except KeyError:
            raise NaoEncontradoErro('jogo')
