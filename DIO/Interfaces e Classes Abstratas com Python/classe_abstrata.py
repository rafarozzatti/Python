# Importa os módulos necessários para trabalhar com classes abstratas
from abc import ABC, abstractmethod

# Define uma classe abstrata chamada ControleRemoto que herda de ABC (Abstract Base Class)
class ControleRemoto(ABC):
    # Método abstrato que deve ser implementado nas subclasses
    @abstractmethod
    def ligar(self):
        pass

    # Outro método abstrato obrigatório nas subclasses
    @abstractmethod
    def desligar(self):
        pass

# Classe concreta que representa um controle de TV, herdando de ControleRemoto
class ControleTV(ControleRemoto):
    # Implementa o método ligar
    def ligar(self):
        print('Ligando a TV...')
        print('Ligada!')

    # Implementa o método desligar
    def desligar(self):
        print('Desligando a TV...')
        print('Desligada!')

# Classe concreta que representa um controle de ar-condicionado, herdando de ControleRemoto
class ControleArCondicionado(ControleRemoto):
    # Implementa o método ligar
    def ligar(self):
        print('Ligando o Ar Condicionado...')
        print('Ligado!')

    # Implementa o método desligar
    def desligar(self):
        print('Desligando o Ar Condicionado...')
        print('Desligado!')

# Cria uma instância da classe ControleTV
controle = ControleTV()
controle.ligar()      # Chama o método ligar da TV
controle.desligar()   # Chama o método desligar da TV

# Cria uma instância da classe ControleArCondicionado
controle = ControleArCondicionado()
controle.ligar()      # Chama o método ligar do ar-condicionado
controle.desligar()   # Chama o método desligar do ar-condicionado
