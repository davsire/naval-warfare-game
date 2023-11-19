from dao.dao import DAO
from entidade.oceano import Oceano
from exception.nao_encontrado_error import NaoEncontradoErro


class OceanoDAO(DAO):
    __instancia = None

    def __init__(self):
        super().__init__('oceano.pkl')

    def __new__(cls):
        if OceanoDAO.__instancia is None:
            OceanoDAO.__instancia = object.__new__(cls)
        return OceanoDAO.__instancia
    
    def add(self, oceano: Oceano):
        if isinstance(oceano, Oceano) and isinstance(oceano.id, int):
            super().add(oceano.id, oceano)

    def get(self, id_oceano: int):
        try:
            if isinstance(id_oceano, int):
                return super().get(id_oceano)
        except KeyError:
            raise NaoEncontradoErro('oceano')

    def remove(self, oceano: Oceano):
        try:
            if isinstance(oceano, Oceano) and isinstance(oceano.id, int):
                super().remove(oceano.id)
        except KeyError:
            raise NaoEncontradoErro('oceano')
