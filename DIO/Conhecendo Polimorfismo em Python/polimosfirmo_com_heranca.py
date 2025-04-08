# Define a classe base "Passaro"
class Passaro:
    # Método que representa a ação de voar
    def voar(self):
        print('Voando...')

# Define uma classe "Pardal" que herda de "Passaro"
class Pardal(Passaro):
    # Sobrescreve o método "voar"
    def voar(self):
        # Chama o método "voar" da classe pai (Passaro)
        super().voar()

# Define uma classe "Avestruz" que também herda de "Passaro"
class Avestruz(Passaro):
    # Sobrescreve o método "voar" com um comportamento diferente
    def voar(self):
        print('Avestruz não pode voar')

# Função que aceita um objeto e chama seu método "voar"
def plano_voo(obj):
    obj.voar()

# Cria uma instância de Pardal
p1 = Pardal()

# Cria uma instância de Avestruz
p2 = Avestruz()

# Chama a função "plano_voo" passando o pardal
plano_voo(p1)  # Saída esperada: "Voando..."

# Chama a função "plano_voo" passando o avestruz
plano_voo(p2)  # Saída esperada: "Avestruz não pode voar"
