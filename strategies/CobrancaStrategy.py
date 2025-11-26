from abc import ABC, abstractmethod

# Implementando o design Pattern Strategy com a cobrança das rotas.
class CobrancaStrategy(ABC): 
    """Classe Abstrata que serve como base para os cálculos de cobrança"""
    @abstractmethod
    def realizarCobraca(rota, veiculo, valorCombustivel):
        pass
    

class CobrancaPontos(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdPontos

class CobrancaKm(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel)

class CobrancaAluno(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdAlunosVinculados

class CobrancaAlunoMensal(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return (((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdAlunosVinculados) * 30


