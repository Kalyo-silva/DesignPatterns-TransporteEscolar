from datetime import datetime
from infra.data import Data
# Implementando o design Pattern Observer para acompanhar a execução das rotas e notificar o sucess ou atraso para o usuário.

class Observer:
    def __init__(self, nome):
        self.nome = nome

    def update(self, state):
        Data().addNotificacao(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} [{self.nome}]: {state}")