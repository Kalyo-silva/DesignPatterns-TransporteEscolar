# Aplica a design pattern Singleton para uma classe que armazenará os dados da aplicação (de forma local sem banco de dados.)
class Data:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.listaRotas = []
            cls._instance.listaVeiculos = []
            cls._instance.listaNotificacoes = []
            cls._instance.executeParams = {
                 "rota" : None,
                 "veiculo" : None,
                 "precoCombustivel" : 0
            }
        return cls._instance

    #funções de manipulação do array de rotas
    def getRotas(self):
        return self.listaRotas
    
    def getRota(self, id):
         if id > 0 or id < (len(self.listaRotas)):
              return self.listaRotas[id-1]

    def addRota(self, rota):
         self.listaRotas.append(rota)

    def removeRota(self, id: int):
         if id > 0:
            self.listaRotas.pop(id-1)

    #funções de manipulação do array de veiculos
    def getVeiculos(self):
         return self.listaVeiculos

    def getVeiculo(self, id):
         if id > 0 or id < (len(self.listaVeiculos)):
              return self.listaVeiculos[id-1]
    
    def addVeiculo(self, veiculo):
         self.listaVeiculos.append(veiculo)
         
    def removeVeiculo(self, id: int):
         if id > 0:
            self.listaVeiculos.pop(id-1)

    #funções de manipulação do array de notificacoes
    def getNotificacoes(self):
         return self.listaNotificacoes
    
    def addNotificacao(self, texto):
         self.listaNotificacoes.append(texto)

    #funções de manipulação do array de parametros de execução
    def getParametrosExecucao(self):
         return self.executeParams

    def setRotaParams(self, rota):
         self.executeParams['rota'] = rota     

    def setVeiculoParams(self, veiculo):
         self.executeParams['veiculo'] = veiculo     
    
    def setCombustivelParams(self, precoCombustivel):
         self.executeParams['precoCombustivel'] = precoCombustivel     

    def clearExecuteParams(self):
         self.executeParams = {
            "rota" : None,
            "veiculo" : None,
            "precoCombustivel" : 0              
         }
         