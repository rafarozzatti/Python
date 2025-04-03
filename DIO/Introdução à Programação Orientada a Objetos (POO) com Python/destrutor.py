# Definição da classe Cachorro
class Cachorro:
    # Método construtor, chamado ao criar uma instância da classe
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')  # Mensagem indicando que um objeto está sendo criado
        self.nome = nome      # Nome do cachorro
        self.cor = cor        # Cor do cachorro
        self.acordado = acordado  # Estado do cachorro (acordado por padrão)

    # Método destrutor, chamado automaticamente quando o objeto é removido da memória
    def __del__(self):
        print('Removendo a instância de classe.')  # Mensagem indicando que o objeto foi destruído

    # Método que simula o cachorro latindo
    def falar(self):
        print('auau')

# Função para criar um cachorro dentro de um escopo local
def criar_cachorro():
    c = Cachorro('Zeus', 'branco e preto', False)  # Criando um objeto dentro da função
    # Como a variável "c" é local, ao final da execução da função, o objeto será destruído automaticamente.

# Criando um objeto da classe Cachorro
c = Cachorro('Chapple', 'amarelo')  # Exibe "Inicializando a classe..."
c.falar()  # Exibe "auau"

# Chamando a função que cria um cachorro
criar_cachorro()
# O objeto "Zeus" criado dentro da função será destruído ao final da função, então o destrutor será chamado.

# O programa termina aqui, e o objeto "c" também será removido da memória, chamando novamente o destrutor.
