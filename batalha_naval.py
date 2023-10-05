from controlador.principal_ctrl import PrincipalCtrl


if __name__ == '__main__':
    while True:
        try:
            PrincipalCtrl().iniciar_app()
        except Exception:
            print('Ocorreu um erro inesperado! Redirecionamos você para a tela inicial')
