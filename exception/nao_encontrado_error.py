

class NaoEncontradoErro(Exception):
    def __init__(self, entidade: str):
        super().__init__(f'O {entidade} não foi encontrado!')
