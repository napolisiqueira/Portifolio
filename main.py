# app.py - Boas-Vindas ao Meu Portfólio

class Portfolio:
    def __init__(self, nome="Napoli", cargo="Desenvolvedor"):
        self.nome = nome
        self.cargo = cargo
        self.versao = "1.0.0"

    def iniciar_sessao(self):
        print(f"==========================================")
        print(f"Bem-vindo(a) ao portfólio de {self.nome}!") # -> Felipe Napoli 
        print(f"Cargo: {self.cargo}") # -> Desenvolvedor backend
        print(f"Versão do Sistema: {self.versao}") # -> 1.0.0
        print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") # -> ????-??-?? ??:??:??
        print(f"------------------------------------------")
        print(f"Explorando conceitos, criando soluções...")
        print(f"==========================================")

from datetime import datetime

# Instância e Execução
meu_portfolio = Portfolio(nome="Felipe Napoli Siqueira", cargo="Desenvolvedor Backend")
meu_portfolio.iniciar_sessao()