

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
        def id(self):
            return self.__id

        @property
        def nome(self):
            return self.__nome

        @property
        def data_nascimento(self):
            return self.__data_nascimento

        @property
        def usuario(self):
            return self.__usuario

        @property
        def senha(self):
            return self.__senha

        @property
        def pontuacao_total(self):
            return self.__pontuacao_total

        @property
        def jogos(self):
            return self.__jogos

        @id.setter
        def id(self, id):
            if isinstance(id, int):
                self.__id = id

        @nome.setter
        def nome(self, nome):
            if isinstance(nome, str):
                self.__nome = nome

        @data_nascimento.setter
        def data_nascimento(self, data_nascimento):
            if isinstance(data_nascimento, str):
                self.__data_nascimento = data_nascimento

        @usuario.setter
        def usuario(self, usuario):
            if isinstance(usuario, str):
                self.__usuario = usuario

        @senha.setter
        def senha(self, senha):
            if isinstance(senha, str):
                self.__senha = senha

        @pontuacao_total.setter
        def pontuacao_total(self, pontuacao_total):
            if isinstance(pontuacao_total, id):
                self.__pontuacao_total = pontuacao_total
