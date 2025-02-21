# Programação Orientada a Objetos (POO) em Python

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de "objetos" que possuem atributos (dados) e métodos (funções). Python suporta POO através da criação de **classes** e **objetos**.

---

## **1. Classes e Objetos**

### **O que é uma Classe?**
Uma **classe** é um modelo para criar objetos. Ela define atributos (dados) e métodos (comportamentos) comuns para os objetos daquela classe.

```python
# Criando uma classe chamada Pessoa
class Pessoa:
    pass  # Usamos 'pass' quando não queremos definir nada ainda
```

### **O que é um Objeto?**
Um **objeto** é uma instância de uma classe. Ou seja, quando criamos um objeto, estamos criando uma cópia baseada na estrutura da classe.

```python
# Criando um objeto da classe Pessoa
pessoa1 = Pessoa()  # Criando uma instância da classe Pessoa
pessoa2 = Pessoa()  # Criando outra instância da classe Pessoa
```

### **Saída:**
*(Nenhuma saída, pois apenas instanciamos objetos da classe)*

---

## **2. Atributos em POO**

Os atributos representam as características de um objeto e podem ser:
- **Atributos de Instância** (próprios de cada objeto)
- **Atributos de Classe** (compartilhados por todos os objetos da classe)

### **Atributos de Instância**

Cada objeto pode ter seus próprios valores para os atributos.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

# Criando objetos com atributos diferentes
pessoa1 = Pessoa("Carlos", 25)  # Pessoa chamada Carlos com 25 anos
pessoa2 = Pessoa("Mariana", 30)  # Pessoa chamada Mariana com 30 anos

# Exibindo os atributos dos objetos
print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
```

### **Saída:**
```
Carlos 25
Mariana 30
```

### **Atributos de Classe**

Os atributos de classe são compartilhados entre todas as instâncias.

```python
class Carro:
    rodas = 4  # Atributo de classe (igual para todos)

# Criando objetos
carro1 = Carro()
carro2 = Carro()

# Exibindo o atributo de classe
print(carro1.rodas)
print(carro2.rodas)
```

### **Saída:**
```
4
4
```

---

## **3. Métodos em POO**

Os métodos são funções dentro da classe que definem o comportamento dos objetos.

### **Métodos de Instância**

Os métodos de instância manipulam os atributos do próprio objeto.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Criando um objeto
pessoa1 = Pessoa("Carlos", 25)

# Chamando o método apresentar
print(pessoa1.apresentar())
```

### **Saída:**
```
Olá, meu nome é Carlos e tenho 25 anos.
```

### **Métodos de Classe**

Os métodos de classe utilizam o decorador `@classmethod` e podem acessar apenas atributos de classe.

```python
class Carro:
    rodas = 4  # Atributo de classe
    
    @classmethod
    def mostrar_rodas(cls):
        return f"Todos os carros têm {cls.rodas} rodas."

# Chamando o método de classe
print(Carro.mostrar_rodas())
```

### **Saída:**
```
Todos os carros têm 4 rodas.
```

### **Métodos Estáticos**

Os métodos estáticos usam `@staticmethod` e não acessam atributos da classe nem da instância.

```python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b  # Retorna a soma de dois números

# Chamando o método estático
print(Matematica.somar(5, 3))
```

### **Saída:**
```
8
```

---

## **4. Criando e Utilizando Objetos**

```python
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome  # Nome do cachorro
        self.raca = raca  # Raça do cachorro

    def latir(self):
        return f"{self.nome} está latindo!"

# Criando um objeto da classe Cachorro
cachorro1 = Cachorro("Rex", "Labrador")

# Chamando o método latir
print(cachorro1.latir())
```

### **Saída:**
```
Rex está latindo!
```

---

### **Quando Usar POO?**
✅ Quando seu programa tem muitos objetos com características semelhantes.
✅ Para organizar melhor seu código.
✅ Quando deseja reutilizar código através da herança e polimorfismo.

❌ Evite POO quando o programa for muito simples, pois pode adicionar complexidade desnecessária.

---
