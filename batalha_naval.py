from controlador.principal_ctrl import PrincipalCtrl
import PySimpleGUI as sg


if __name__ == '__main__':
    controlador_principal = PrincipalCtrl()
    while True:
        try:
            controlador_principal.iniciar_app()
        except Exception:
            sg.Popup('Ocorreu um erro inesperado! '
                     'Redirecionamos você para a tela inicial')
