

class ConflitoEmbarcacaoErro(Exception):
    def __init__(self, linha: int, coluna: int):
        super().__init__(f'Já existe uma embarcação '
                         f'na linha {linha} e coluna {coluna}!')
