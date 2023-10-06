from entidade.embarcacao import Embarcacao


class Submarino(Embarcacao):
    def __init__(self):
        super().__init__('S', 2)
