from datetime import datetime
# Implementando o design Pattern Observer para acompanhar a execução das rotas e notificar o sucess ou atraso para o usuário.

notificacoes = []

class Observer:
    def __init__(self, nome):
        self.nome = nome

    def update(self, state):
        notificacoes.append(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} [{self.nome}]: {state}")