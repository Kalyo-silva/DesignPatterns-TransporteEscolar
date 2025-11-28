import os
from domain.Rotas import Rota
from domain.Veiculos import Veiculo
from decorators.RouteExecutor import RouteExecutor
from strategies.CobrancaStrategy import *
from infra.data import Data


def clear_screen():
    """Clears the terminal screen for both Windows and Linux/macOS."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS (posix systems)
        os.system('clear')

# Text Art para atitulos
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
    print('\033[93m - By Kalyo Airan da Silva\033[0m')

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

def ResultadosLogo():
    clear_screen()
    print('\033[92m')
    print(' █▀█ █▀▀ █▀ █ █ █   ▀█▀ ▄▀█ █▀▄ █▀█ █▀')
    print(' █▀▄ ██▄ ▄█ █▄█ █▄▄  █  █▀█ █▄▀ █▄█ ▄█\033[0m')


#Menu principal
def mainMenu():
    while True:
        mainLogo()

        if len(Data().listaNotificacoes) != 0:
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

        #try:
        cmd = int(input('\033[94m > '))

        if cmd == 0:
            break

        route(cmd)
        #except:
         #   input('Comando Inválido, tente Novamente')

    
#Roteamento das Funções do menu                                                      
def route(cmd):
    if cmd == 1:
        menuRotas()
    elif cmd == 2:
        menuVeiculos()
    elif cmd == 3:
        menuExecutar()
    elif cmd == 4:
        menuNotificacoes()
    else:
        input('Comando Inválido, tente Novamente')

#Funções das Rotas
def menuRotas():
    while True:
        routesLogo()
        print('--------------------')
        print('\033[94m')
        listarRotas()

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
            elif cmd == 1:
                cadastrarRota()
            elif cmd == 2:
                removerRota()
            else:
                input('Comando Inválido, tente Novamente')
        except:
            input('Comando Inválido, tente Novamente')

def listarRotas():
    print('┌─── Rotas Cadastradas ─────────────────────┐')
    for index, rota in enumerate(Data().getRotas()):
        spacing = ''
        if len(str(index)) + len(rota.titulo) + 8 < 44:
            for i in range(44 - (len(str(index)) + len(rota.titulo) + 7)):
                spacing += ' ' 

        print(f'\033[94m│ \033[95m[{index+1}] - {rota.titulo}{spacing}\033[94m│')
    print('\033[94m└───────────────────────────────────────────┘ ')

def cadastrarRota():
    titulo = input('\033[94mInforme o nome da rota: \033[0m')
    qtdPontos = int(input('\033[94minforme a quantidade de pontos que a rota possui: \033[0m'))
    qtdAlunosVinculados = int(input('\033[94minforme a quantidade de alunos vinculados a rota: \033[0m'))
    distancia = float(input('\033[94minforme a distância da rota (km): \033[0m'))

    print('')
    print('\033[94m┌─ Tipos de Cobrança ───────────────────────┐')
    print('\033[94m│ \033[95m[1] - Individual por Distância \033[94m           │')
    print('\033[94m│ \033[95m[2] - Individual por Aluno \033[94m               │')
    print('\033[94m│ \033[95m[3] - Individual por Quantidade de Pontos \033[94m│')
    print('\033[94m│ \033[95m[4] - Mensal por Aluno \033[94m                   │')
    print('\033[94m└───────────────────────────────────────────┘ ')
    print('Informe o tipo de cobrança: ')

    tipoCobranca = int(input(' > \033[0m'))

    cobranca: CobrancaStrategy = CobrancaStrategy

    if tipoCobranca == 1:
        cobranca = CobrancaKm
    elif tipoCobranca == 2:
        cobranca = CobrancaAluno
    elif tipoCobranca == 3:
        cobranca = CobrancaPontos
    elif tipoCobranca == 4:
        cobranca = CobrancaAlunoMensal
    else:
        return
    

    rota: Rota = Rota(titulo=titulo, 
                      qtdPontos=qtdPontos,
                      qtdAlunosVinculados=qtdAlunosVinculados, 
                      distancia=distancia,
                      tipoCobranca = cobranca)

    notif = input('Deseja ser notificado da execução desta Rota? (S/N): ')
    if notif.upper() == 'S':
        rota.acompanhar()
    elif notif.upper == 'N':
        rota.pararAcompanhamento()
    else:
        return
    
    Data().addRota(rota)
    
def removerRota():
    id = int(input('codigo da rota: '))

    Data().removeRota(id)

#funções dos veículos
def menuVeiculos():
    while True:
        VehiclesLogo()
        print('------------------------------')
        print('\033[94m')
        listarVeiculos()

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
            elif cmd == 1:
                cadastrarVeiculo()
            elif cmd == 2:
                removerVeiculo()
            else:
                input('Comando Inválido, tente Novamente')
        except:
            input('Comando Inválido, tente Novamente')

def listarVeiculos():
    print('┌─ Veículos Cadastrados ──────────────────────┐')
    for index, veiculo in enumerate(Data().getVeiculos()):
        spacing = ''
        if len(str(index)) + len(veiculo.marca) + len(veiculo.modelo) + 7 < 44:
            for i in range(44 - (len(veiculo.marca) + len(veiculo.modelo) + 7)):
                spacing += ' ' 

        print(f'\033[94m│ \033[95m[{index+1}] - {veiculo.marca} {veiculo.modelo}{spacing}\033[94m│')
    print('\033[94m└─────────────────────────────────────────────┘ ')

def cadastrarVeiculo():
    marca = input('\033[94mInforme a marca do veículo: \033[0m')
    modelo = input('\033[94minforme o modelo do veículo: \033[0m')
    consumo = float(input('\033[94minforme a eficiencia de combustível do veículo (Km/L): \033[0m'))

    Data().addVeiculo(Veiculo(marca=marca, 
                              modelo=modelo,
                              consumo=consumo))
    
def removerVeiculo():
    id = int(input('codigo do Veículo: '))

    Data().removeVeiculo(id)


#funções da execução da rota
def menuExecutar():
    while True:
        ExecuteLogo()
        print('---------------------------------')
        print('\033[94m')
        getParametrosExecucao()
        print('\033[0m')
        print('\033[92m [1] \033[93m- Definir Rota')
        print('\033[92m [2] \033[93m- Definir Veículo')
        print('\033[92m [3] \033[93m- Definir Valor do Combustível')
        print('\033[92m [4] \033[93m- Executar')
        print('')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                Data().clearExecuteParams()
                break
            elif cmd == 1:
                setParamRota()
            elif cmd == 2:
                setParamVeículo()
            elif cmd == 3:
                setParamCombustivel()
            elif cmd == 4:
                executaRota(Data().getParametrosExecucao())
                break
            else:
                input('Comando Inválido, tente Novamente')
        except:
            input('Comando Inválido, tente Novamente')
    
def setParamRota():
    listarRotas()
    cmd = int(input('\033[94m Selecione a rota: \033[0m'))
    Data().setRotaParams(Data().getRota(cmd))    

def setParamVeículo():
    listarVeiculos()
    cmd = int(input('\033[94m Selecione o veículo: \033[0m'))
    Data().setVeiculoParams(Data().getVeiculo(cmd))

def setParamCombustivel():
    valor = float(input('informe o valor do Combustível (R$/L): \033[0mR$'))
    Data().setCombustivelParams(valor)

def getSpacingParametros(textoBase,parametro):
    spacing = ''
    if len(str(parametro)) + len(textoBase) < 45:
            for i in range(45 - (len(str(parametro)) + len(textoBase))):
                spacing += ' ' 

    return f"\033[94m{textoBase}\033[0m{parametro}\033[94m{spacing}"

def getParametrosExecucao():
    params = Data().getParametrosExecucao()
    
    print('┌─ Parâmetros de Execução ────────────────────┐')
    if params['rota'] != None:
        print('│'+getSpacingParametros(' [Rota] -> ', params['rota'].titulo)+'│')
    if params['veiculo'] != None:
        print('│'+getSpacingParametros(' [Veículo] -> ', f"{params['veiculo'].marca} {params['veiculo'].modelo}")+'│')
    if params['precoCombustivel'] != 0:
        print('│'+getSpacingParametros(' [Custo do Combustível] -> ', params['precoCombustivel'])+'│')
    print('└─────────────────────────────────────────────┘')

def executaRota(params):
    executor = RouteExecutor(params['rota'], params['veiculo'], params['precoCombustivel'])
    rota: Rota = params['rota']
    veiculo: Veiculo = params['veiculo']
    result, pontosExtras = executor.ExecutaRota()

    ResultadosLogo()
    print('---------------------------------------')
    print('\033[94m')
    print('┌─ Resultados da Execução ────────────────────┐')
    print('│'+getSpacingParametros(' [Rota] -> ', rota.titulo)+'│')
    print('│'+getSpacingParametros('  - Distância: ', rota.distancia)+'│')
    if pontosExtras > 0:
        print('│'+getSpacingParametros('  - Quantidade de Pontos: ', f"{str(rota.qtdPontos)} + {pontosExtras}")+'│')
    else:
        print('│'+getSpacingParametros('  - Quantidade de Pontos: ', rota.qtdPontos)+'│')
    print('│'+getSpacingParametros('  - Quantidade de Alunos Vinculados: ', rota.qtdAlunosVinculados)+'│')
    print('│'+getSpacingParametros('  - Cobrança: ', rota.cobranca.getTipoCobranca())+'│')
    print('├─────────────────────────────────────────────┤')
    print('│'+getSpacingParametros(' [Veiculo] -> ', f"{veiculo.marca} {veiculo.modelo}")+'│')
    print('│'+getSpacingParametros('  - Eficiência de Combustivel (Km/L): ', veiculo.consumoCombustivel)+'│')
    print('├─────────────────────────────────────────────┤')
    print('│'+getSpacingParametros(' [Preço do Combustível] -> ', params['precoCombustivel'])+'│')
    print('├─────────────────────────────────────────────┤')
    print('│'+getSpacingParametros(' [Custo da Rota] -> ', round(result,2))+'│')
    print('└─────────────────────────────────────────────┘')
    input('')

#funções ds Notificacoes
def menuNotificacoes():
    while True:
        NotificationsLogo()
        print('---------------------------------------------')
        listarNotificacoes()
        print('\033[94m')
        print('\033[92m [0] - \033[93mSair')
        print('')

        try:
            cmd = int(input('\033[94m > '))

            if cmd == 0:
                break
        except:
            input('Comando Inválido, tente Novamente')

def listarNotificacoes():
    print('\033[94m┌─ Notificações ───────────────────────────────────────────────────────────────────┐')
    for index, notificacao in enumerate(Data().getNotificacoes()):
        spacing = ''
        if len(str(index)) + len(notificacao) + 6 < 83:
            for i in range(83 - (len(str(index)) + len(notificacao) + 5)):
                spacing += ' ' 

        print(f'\033[94m│ \033[95m[{index+1}] {notificacao}{spacing}\033[94m│')
    print('\033[94m└──────────────────────────────────────────────────────────────────────────────────┘ ')
