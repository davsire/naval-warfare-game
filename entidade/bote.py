from entidade.embarcacao import Embarcacao


class Bote(Embarcacao):
    def __init__(self):
        super().__init__('B', 1)


bote = Bote()
