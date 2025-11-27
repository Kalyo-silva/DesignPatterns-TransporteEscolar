from strategies.CobrancaStrategy import CobrancaStrategy
from observers.Observer import Observer

class Rota():
    def __init__(self, titulo : str, qtdPontos: int, qtdAlunosVinculados: int, distancia: float, tipoCobranca: CobrancaStrategy):
        self.titulo = titulo
        self.qtdPontos = qtdPontos
        self.qtdAlunosVinculados = qtdAlunosVinculados
        self.distancia = distancia
        self.cobranca = tipoCobranca
        self.observador = None

    def calculaValores(self, veiculo, valorCombustivel):
        return self.cobranca.realizarCobraca(self, veiculo, valorCombustivel)

    def acompanhar(self):
        self.observador = Observer(nome=self.titulo)
    
    def pararAcompanhamento(self):
        self.observador = None

    def notificar(self, notificacao):
        if self.observador != None:
            self.observador.update(notificacao)
    
