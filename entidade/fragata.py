from entidade.embarcacao import Embarcacao


class Fragata(Embarcacao):
    def __init__(self):
        super().__init__('F', 3)
