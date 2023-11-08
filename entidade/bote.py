from entidade.embarcacao import Embarcacao, SiglaEmbarcacao


class Bote(Embarcacao):
    def __init__(self):
        super().__init__(SiglaEmbarcacao.B, 1)
