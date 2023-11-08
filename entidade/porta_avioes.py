from entidade.embarcacao import Embarcacao, SiglaEmbarcacao


class PortaAvioes(Embarcacao):
    def __init__(self):
        super().__init__(SiglaEmbarcacao.P, 4)
