from abc import ABC, abstractmethod
import PySimpleGUI as sg
from enum import Enum


class OpcaoBotao(Enum):
    VOLTAR = 'VOLTAR',


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        self.__window = None

    def obtem_layout_titulo(self, titulo: str):
        return [
            [sg.Text('#' * 40, justification='center')],
            [sg.Text(titulo, justification='center')],
            [sg.Text('#' * 40, justification='center')],
        ]

    def obtem_layout_opcoes(self, opcoes: list):
        return [
            [sg.Button(opcao, key=index, size=max(20, len(opcao)))]
            for index, opcao in enumerate(opcoes, start=1)
        ]

    def obtem_layout_lista(self, elementos: list):
        return [
            [sg.Text('-' * 80, justification='center')],
            *[[sg.Text(elemento, justification='center')]
              for elemento in elementos],
            [sg.Text('-' * 80, justification='center')],
        ]

    def obtem_layout_mostra_dados(self, dados: dict):
        return [
            [sg.Text('-' * 80, justification='center')],
            *[[
                sg.Text(f'{label}: ', size=20, justification='left'),
                sg.Text(dados[label], size=20, justification='right'),
            ] for label in dados],
            [sg.Text('-' * 80, justification='center')],
        ]

    def obtem_layout_obtem_dados(self,
                                 dados: dict,
                                 label_confirmar: str,
                                 dados_atuais: dict = None):
        if dados_atuais is None:
            dados_atuais = {}
        tamanho_labels = max(20, max([len(label) for label in dados.values()]))
        return [
            *[[
                sg.Text(dados[chave], size=tamanho_labels),
                sg.InputText(
                    dados_atuais[chave] if chave in dados_atuais else '',
                    size=20,
                    key=chave
                )
            ] for chave in dados],
            [
                sg.Submit(label_confirmar, size=(10, 1)),
                sg.Cancel('Voltar', key=OpcaoBotao.VOLTAR, size=(10, 1))
            ]
        ]

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

    def confirma_acao(self, mensagem: str):
        return [
            [sg.Text(mensagem, justification='center')],
            [
                sg.Button('Sim', size=(10, 1), key=True),
                sg.Button('Não', size=(10, 1), key=False)
            ],
        ]

    def mostra_titulo(self, titulo: str):
        print('#' * 35)
        print(titulo)
        print('#' * 35)

    def mostra_mensagem(self, mensagem: str):
        sg.Popup(mensagem, title='Batalha Naval')

    def open(self, layout: list) -> tuple:
        self.__window = sg.Window('Batalha Naval',
                                  layout,
                                  element_justification='center')
        botao, valores = self.__window.Read()
        return botao, valores

    def close(self):
        self.__window.Close()
