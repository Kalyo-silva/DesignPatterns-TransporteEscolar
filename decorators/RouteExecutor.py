from domain.Rotas import Rota
from domain.Veiculos import Veiculo
import random

# Implementando o design Pattern Decorator com a validação de pontos extras na rota.
class RouteExecutor():
    def __init__(self, rota: Rota, veiculo: Veiculo, precoCombustivel: float):
        self.rota = rota
        self.veiculo = veiculo
        self.precoCombustivel = precoCombustivel 

    def setPrecoCombustivel(self, preco: float):
        self.precoCombustivel = preco

    def verificaPontoExtra(func): #decorator que solicita os pontos extras antes de executar a rota
        def wrapper(*args, **kwargs):
            pontosExtras = int(input('informe a quantidade de pontos extras: '))

            args[0].rota.qtdPontos += pontosExtras # aumenta a quantidade de pontos para executar a rota
            result = func(*args, *kwargs)
            args[0].rota.qtdPontos -= pontosExtras # reduz para o tamanho original da rota
            return result, pontosExtras
        return wrapper
    
    @verificaPontoExtra # wrapping da função executaRota
    def ExecutaRota(self):
        result = self.rota.calculaValores(veiculo=self.veiculo, valorCombustivel=self.precoCombustivel)
        
        atraso = random.randint(1,2) == 1 #chance de 50% de ter atraso na rota

        #notifica a execução para o observer da rota
        if atraso:
            self.rota.notificar('Rota executada com atrasos!')
        else:
            self.rota.notificar('Rota executada com sucesso!')

        return result
    