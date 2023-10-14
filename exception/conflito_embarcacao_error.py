import string


class ConflitoEmbarcacaoErro(Exception):
    def __init__(self, linha: int, coluna: int):
        self.__indice_letras = {index: letra
                                for index, letra
                                in enumerate(list(string.ascii_uppercase))}
        super().__init__(f'Já existe uma embarcação na linha {linha + 1} '
                         f'e coluna {self.__indice_letras[coluna]}!')
