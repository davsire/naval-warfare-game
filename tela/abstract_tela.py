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
            [sg.Text('-' * 55, justification='center')],
            *[[sg.Text(elemento, justification='center')]
              for elemento in elementos],
            [sg.Text('-' * 55, justification='center')],
        ]

    def obtem_layout_mostra_dados(self, dados: dict):
        return [
            [sg.Text('-' * 55, justification='center')],
            *[[
                sg.Text(f'{label}:', size=20, justification='left'),
                sg.Text(dados[label], size=20, justification='right'),
            ] for label in dados],
            [sg.Text('-' * 55, justification='center')],
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

    def confirma_acao(self, mensagem: str):
        return [
            [sg.Text(mensagem, justification='center')],
            [
                sg.Button('Sim', size=(10, 1), key=True),
                sg.Button('Não', size=(10, 1), key=False)
            ],
        ]

    def mostra_mensagem(self, mensagem: str):
        sg.Popup(mensagem, title='Batalha Naval')

    def mostra_mensagem_rapida(self, mensagem: str, posicao: tuple):
        sg.PopupQuick(mensagem,
                      title='Batalha Naval',
                      auto_close_duration=1.5,
                      keep_on_top=True,
                      relative_location=posicao)

    def open(self, layout: list, timeout: int = None) -> tuple:
        self.__window = sg.Window('Batalha Naval',
                                  layout,
                                  element_justification='center')
        botao, valores = self.__window.Read(timeout=timeout)
        return botao, valores

    def close(self):
        self.__window.Close()
