from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def obtem_opcao(self, mensagem: str, opcoes_validas: list = None) -> int:
        while True:
            try:
                opcao_escolhida = int(input(mensagem))
                if opcoes_validas and opcao_escolhida not in opcoes_validas:
                    raise ValueError
                return opcao_escolhida
            except ValueError:
                print('Selecione uma opção válida!')
                if opcoes_validas:
                    print('Opções válidas:', opcoes_validas)

    def mostra_opcoes(self, opcoes: list):
        for index, opcao in enumerate(opcoes, start=1):
            print(f'{index} - {opcao}')

    def obtem_informacao(self, mensagem: str) -> str:
        informacao = input(mensagem)
        return informacao

    def mostra_titulo(self, titulo: str):
        print('#' * 35)
        print(titulo)
        print('#' * 35)

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
