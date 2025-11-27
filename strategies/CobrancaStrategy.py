from abc import ABC, abstractmethod

# Implementando o design Pattern Strategy com a cobrança das rotas.
class CobrancaStrategy(ABC): 
    """Classe Abstrata que serve como base para os cálculos de cobrança"""
    @abstractmethod
    def realizarCobraca(rota, veiculo, valorCombustivel):
        pass
    @abstractmethod
    def getTipoCobranca():
        pass

class CobrancaPontos(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdPontos
    def getTipoCobranca():
        return "Individual p/ Qtd. de Pontos"

class CobrancaKm(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel)
    def getTipoCobranca():
        return "Individual p/ Distância"

class CobrancaAluno(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return ((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdAlunosVinculados
    def getTipoCobranca():
        return "Individual p/ Aluno"

class CobrancaAlunoMensal(CobrancaStrategy):
    def realizarCobraca(rota, veiculo, valorCombustivel):
        return (((rota.distancia / veiculo.consumoCombustivel) * valorCombustivel) / rota.qtdAlunosVinculados) * 30
    def getTipoCobranca():
        return "Mensal p/ Aluno"


