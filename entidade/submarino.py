from entidade.embarcacao import Embarcacao, SiglaEmbarcacao


class Submarino(Embarcacao):
    def __init__(self):
        super().__init__(SiglaEmbarcacao.S, 2)
