# Abstração e Encapsulamento na Programação Orientada a Objetos (POO)

## **1. O que é Abstração?**

A **Abstração** é um conceito da POO que permite esconder detalhes internos da implementação de um objeto e expor apenas o que é necessário. Isso ajuda a reduzir a complexidade e melhorar a manutenção do código.

Exemplo prático:

```python
# Importamos a biblioteca abc para criar classes abstratas
from abc import ABC, abstractmethod

# Criamos uma classe abstrata chamada Animal
class Animal(ABC):  # Classe abstrata
    @abstractmethod  # Definimos um método abstrato que deve ser implementado nas subclasses
    def fazer_som(self):
        pass  # O método não possui implementação aqui
```

Neste exemplo, `Animal` é uma classe abstrata que define um comportamento genérico (`fazer_som`), mas não especifica como ele deve ser implementado.

---

## **2. Implementando a Abstração**

Para utilizar a classe abstrata, criamos classes concretas que a estendem e implementam os métodos abstratos.

```python
# Criamos a classe Cachorro que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):  # Implementamos o método abstrato
        return "Au au!"

# Criamos a classe Gato que herda de Animal
class Gato(Animal):
    def fazer_som(self):  # Implementamos o método abstrato
        return "Miau!"

# Criamos instâncias das classes concretas
cachorro = Cachorro()
gato = Gato()

# Chamamos os métodos e imprimimos os resultados
print(cachorro.fazer_som())  # Saída: Au au!
print(gato.fazer_som())      # Saída: Miau!
```

### **Saída:**
```
Au au!
Miau!
```

A classe `Animal` define a estrutura, mas não a implementação, garantindo que todas as subclasses implementem `fazer_som()`.

---

## **3. O que é Encapsulamento?**

O **Encapsulamento** é a técnica de restringir o acesso a certos detalhes internos de um objeto, protegendo os dados e expondo apenas o necessário.

Em Python, usamos diferentes níveis de acesso para os atributos:

- **Público (`public`)**: Pode ser acessado de qualquer lugar.
- **Protegido (`_protected`)**: Indica que o atributo é para uso interno, mas ainda pode ser acessado.
- **Privado (`__private`)**: Não pode ser acessado diretamente de fora da classe.

Exemplo:

```python
# Criamos a classe ContaBancaria para representar uma conta bancária
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self._saldo = saldo  # Atributo protegido
        self.__senha = "1234"  # Atributo privado

    # Método público para depositar dinheiro
    def depositar(self, valor):
        self._saldo += valor  # Modificamos o saldo protegido
        return f"Depósito de R${valor} realizado. Saldo atual: R${self._saldo}"

    # Método público para visualizar o saldo
    def ver_saldo(self):
        return f"Saldo atual de {self.titular}: R${self._saldo}"

# Criamos uma conta bancária para Carlos
conta = ContaBancaria("Carlos", 1000)

# Exibimos o saldo inicial
print(conta.ver_saldo())  # Saída: Saldo atual de Carlos: R$1000

# Realizamos um depósito e mostramos o saldo atualizado
print(conta.depositar(500))  # Saída: Depósito de R$500 realizado. Saldo atual: R$1500
```

### **Saída:**
```
Saldo atual de Carlos: R$1000
Depósito de R$500 realizado. Saldo atual: R$1500
```

---

## **4. Restringindo o Acesso a Dados**

Vamos tentar acessar diretamente os atributos:

```python
# Acessamos o atributo público normalmente
print(conta.titular)  # Funciona (Público)

# Acessamos o atributo protegido (não recomendado, mas possível)
print(conta._saldo)  # Funciona (Protegido)

# Tentamos acessar o atributo privado diretamente (gera erro)
# print(conta.__senha)  # Erro! (Privado)
```

### **Saída:**
```
Carlos
1000
AttributeError: 'ContaBancaria' object has no attribute '__senha'
```

Para acessar atributos privados, usamos **métodos públicos**:

```python
# Criamos uma nova classe com um método para acessar um atributo privado
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self.__senha = "1234"

    # Método público para acessar o atributo privado
    def verificar_senha(self):
        return f"A senha é: {self.__senha}"

# Criamos uma conta
conta = ContaBancaria("Carlos", 1000)

# Chamamos o método público para visualizar a senha
print(conta.verificar_senha())  # Saída: A senha é: 1234
```

### **Saída:**
```
A senha é: 1234
```

O uso de **métodos getter e setter** também é comum para acessar e modificar atributos privados de forma controlada.

---

## **5. Quando Usar Abstração e Encapsulamento?**

✅ **Use Abstração quando:**
- Deseja criar uma estrutura padrão para suas classes.
- Quer garantir que classes filhas implementem determinados comportamentos.

✅ **Use Encapsulamento quando:**
- Precisa proteger os dados de alterações indevidas.
- Quer ocultar a implementação interna e fornecer apenas a interface necessária.

❌ **Evite encapsular atributos sem necessidade**, pois isso pode tornar o código mais complexo sem benefícios reais.

---
