from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        self._window = None

    def obtem_layout_opcoes(self, opcoes: list, titulo: str = ''):
        layout = []

        if titulo:
            layout.extend([
                [sg.Text('#' * 35, justification='center')],
                [sg.Text(titulo, justification='center')],
                [sg.Text('#' * 35, justification='center', size=(35, 2))],
            ])

        layout.extend([
            [sg.Button(opcao, key=index, size=15)]
            for index, opcao in enumerate(opcoes, start=1)
        ])

        return layout

    def obtem_layout_lista(self, elementos: list, titulo: str = ''):
        layout = []

        if titulo:
            layout.extend([
                [sg.Text('#' * 35, justification='center')],
                [sg.Text(titulo, justification='center')],
                [sg.Text('#' * 35, justification='center', size=(35, 2))],
            ])

        layout = [
            [sg.Text('-' * 35, justification='center')],
            *[[sg.Text(
                elemento,
                size=(35),
                justification='center'
            )] for elemento in elementos],
            [sg.Text('-' * 35, justification='center')],
        ]

        return layout

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

    def confirma_acao(self, mensagem: str) -> bool:
        confirmacao = input(f'{mensagem} [S/n] ')
        return confirmacao.lower() != 'n'

    def mostra_titulo(self, titulo: str):
        print('#' * 35)
        print(titulo)
        print('#' * 35)

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def open(self):
        botao, valores = self._window.Read()
        return botao, valores

    def close(self):
        self._window.Close()
