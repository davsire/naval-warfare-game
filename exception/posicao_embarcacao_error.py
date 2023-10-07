

class PosicaoEmbarcacaoErro(Exception):
    def __init__(self):
        super().__init__('A posição fornecida está incorreta ou '
                         'é diferente do tamanho da embarcação!')
