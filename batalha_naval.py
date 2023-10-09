from controlador.principal_ctrl import PrincipalCtrl


if __name__ == '__main__':
    controlador_principal = PrincipalCtrl()
    while True:
        try:
            controlador_principal.iniciar_app()
        except Exception:
            print('Ocorreu um erro inesperado! Redirecionamos você para a tela inicial')
