

class Jogador:
    def __init__(self, id: int, nome: str, data_nascimento: str, usuario: str, senha: str):
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__usuario = usuario
        self.__senha = senha
        self.__pontuacao_total = 0
        self.__jogos = []

    @property
    def id(self) -> int:
            return self.__id

    @property
    def nome(self) -> str:
            return self.__nome

    @property
    def data_nascimento(self) -> str:
            return self.__data_nascimento

    @property
    def usuario(self) -> str:
            return self.__usuario

    @property
    def senha(self) -> str:
            return self.__senha

    @property
    def pontuacao_total(self) -> int:
            return self.__pontuacao_total

    @property
    def jogos(self) -> list:
            return self.__jogos

    @id.setter
    def id(self, id: int):
            if isinstance(id, int):
                self.__id = id

    @nome.setter
    def nome(self, nome: str):
            if isinstance(nome, str):
                self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
            if isinstance(data_nascimento, str):
                self.__data_nascimento = data_nascimento

    @usuario.setter
    def usuario(self, usuario: str):
            if isinstance(usuario, str):
                self.__usuario = usuario

    @senha.setter
    def senha(self, senha: str):
            if isinstance(senha, str):
                self.__senha = senha

    def aumenta_pontuacao_total(self, pontuacao: int):
        if isinstance(pontuacao, int):
            self.__pontuacao_total += pontuacao
