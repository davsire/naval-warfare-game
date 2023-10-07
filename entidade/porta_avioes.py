from entidade.embarcacao import Embarcacao


class PortaAvioes(Embarcacao):
    def __init__(self):
        super().__init__('P', 4)
