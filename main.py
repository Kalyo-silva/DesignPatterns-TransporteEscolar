from domain.Rotas import Rota
from domain.Veiculos import Veiculo
from strategies.CobrancaStrategy import *
from decorators.RouteExecutor import RouteExecutor
from observers.Observer import notificacoes
import app.interface as interface


rota = Rota(titulo='Rota Teste', qtdPontos=4, distancia=45, qtdAlunosVinculados=30)
rota.setTipoCobranca(CobrancaPontos)

rota.acompanhar()

veiculo = Veiculo(marca='Chevrolet', modelo='Bus', consumo=8)

custoCombustivel = 6.11


interface.mainLogo()
interface.mainMenu(len(notificacoes))

executor = RouteExecutor(rota=rota, veiculo=veiculo)
executor.setPrecoCombustivel(custoCombustivel)


#print(executor.ExecutaRota())

