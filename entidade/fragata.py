from entidade.embarcacao import Embarcacao, SiglaEmbarcacao


class Fragata(Embarcacao):
    def __init__(self):
        super().__init__(SiglaEmbarcacao.F, 3)
