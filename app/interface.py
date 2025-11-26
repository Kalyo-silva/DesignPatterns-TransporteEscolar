import os
import app.data as data


def clear_screen():
    """Clears the terminal screen for both Windows and Linux/macOS."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS (posix systems)
        os.system('clear')

def mainLogo():
    clear_screen()
    print('\033[92m')
    print('┏━━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋┏━━━┓╋╋╋╋╋╋╋╋┏┓')
    print('┃┏┓┏┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋┃┏━━┛╋╋╋╋╋╋╋╋┃┃')
    print('┗┛┃┃┣┻┳━━┳━┓┏━━┳━━┳━━┳┻┓┏╋━━┓┃┗━━┳━━┳━━┳━━┫┃┏━━┳━┓')
    print('╋╋┃┃┃┏┫┏┓┃┏┓┫━━┫┏┓┃┏┓┃┏┫┃┃┃━┫┃┏━━┫━━┫┏━┫┏┓┃┃┃┏┓┃┏┛')
    print('╋╋┃┃┃┃┃┏┓┃┃┃┣━━┃┗┛┃┗┛┃┃┃┗┫┃━┫┃┗━━╋━━┃┗━┫┗┛┃┗┫┏┓┃┃')
    print('╋╋┗┛┗┛┗┛┗┻┛┗┻━━┫┏━┻━━┻┛┗━┻━━┛┗━━━┻━━┻━━┻━━┻━┻┛┗┻┛')
    print('╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃')
    print('╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛\033[0m')

def routesLogo():
    clear_screen()
    print('\033[92m')
    print(' █▀█ █▀█ ▀█▀ ▄▀█ █▀')
    print(' █▀▄ █▄█  █  █▀█ ▄█\033[0m')


def VehiclesLogo():
    clear_screen()
    print('\033[92m')
    print(' █ █ █▀▀ █ █▀▀ █ █ █   █▀█ █▀')
    print(' ▀▄▀ ██▄ █ █▄▄ █▄█ █▄▄ █▄█ ▄█\033[0m')


def ExecuteLogo():
    clear_screen()
    print('\033[92m')
    print(' █▀▀ ▀▄▀ █▀▀ █▀▀ █ █ ▀█▀ ▄▀█ █▀█')
    print(' ██▄ █ █ ██▄ █▄▄ █▄█  █  █▀█ █▀▄\033[0m')

def NotificationsLogo():
    clear_screen()
    print('\033[92m')
    print(' █▄ █ █▀█ ▀█▀ █ █▀▀ █ █▀▀ ▄▀█ █▀▀ █▀█ █▀▀ █▀')
    print(' █ ▀█ █▄█  █  █ █▀  █ █▄▄ █▀█ █▄▄ █▄█ ██▄ ▄█\033[0m')

def mainMenu(qtdNotificacoes):
    while True:
        mainLogo()

        if qtdNotificacoes != 0:
            itemNotificacoes = f'\033[92m [4] \033[93m- Notificações [!]'
        else:
            itemNotificacoes = f'\033[92m [4] \033[93m- Notificações'
        
        print('')
        print('\033[92m [1] \033[93m- Rotas')
        print('\033[92m [2] \033[93m- Veículos')
        print('\033[92m [3] \033[93m- Executar')
        print(itemNotificacoes)
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break

            route(cmd)
        except:
            input('Comando Inválido, tente Novamente')

def route(cmd):
    if cmd == 1:
        menuRotas()
    elif cmd == 2:
        menuVeiculos()
    elif cmd == 3:
        menuExecutar()
    elif cmd == 4:
        menuNotificacoes()

def listarRotas():
    for index, rota in enumerate(data.getRotas()):
        print(f'\033[95m [{index+1}] - {rota.titulo}')

def menuRotas():
    while True:
        routesLogo()
        print('--------------------')
        print('\033[94m')
        print('--- Rotas Cadastradas ---')
        listarRotas()
        print('\033[94m-------------------------')

        print('\033[0m')
        print('\033[92m [1] \033[93m- Cadastrar')
        print('\033[92m [2] \033[93m- Remover')
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break
        except:
            input('Comando Inválido, tente Novamente')

def menuVeiculos():
    while True:
        VehiclesLogo()
        print('------------------------------')
        print('\033[94m')

        print('\033[0m')
        print('\033[92m [1] \033[93m- Cadastrar')
        print('\033[92m [2] \033[93m- Remover')
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break
        except:
            input('Comando Inválido, tente Novamente')

def menuExecutar():
    while True:
        ExecuteLogo()
        print('---------------------------------')
        print('\033[94m')

        print('\033[0m')
        print('\033[92m [1] \033[93m- Cadastrar')
        print('\033[92m [2] \033[93m- Remover')
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break
        except:
            input('Comando Inválido, tente Novamente')
    

def menuNotificacoes():
    while True:
        NotificationsLogo()
        print('---------------------------------------------')
        print('\033[94m')

        print('\033[0m')
        print('\033[92m [1] \033[93m- Cadastrar')
        print('\033[92m [2] \033[93m- Remover')
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break
        except:
            input('Comando Inválido, tente Novamente')