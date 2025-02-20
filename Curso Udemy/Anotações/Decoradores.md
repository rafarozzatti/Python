# Decoradores em Python

Os **decoradores** são uma forma poderosa de modificar o comportamento de funções sem alterar seu código-fonte. Eles permitem adicionar funcionalidades antes e/ou depois da execução da função original.

---

## **1. O que são Decoradores?**

Um **decorador** é uma função que recebe outra função como argumento e retorna uma nova função modificada. Ele é frequentemente usado para **logging, autenticação, caching e validações.**

```python
# Criando um decorador simples

def meu_decorador(funcao):
    def wrapper():
        print("Executando antes da função...")  # Código antes da função
        funcao()  # Executa a função original
        print("Executando depois da função...")  # Código depois da função
    return wrapper

# Aplicando o decorador
@meu_decorador  # Equivalente a -> minha_funcao = meu_decorador(minha_funcao)
def minha_funcao():
    print("Função principal executada.")

minha_funcao()
```

### **Saída:**
```
Executando antes da função...
Função principal executada.
Executando depois da função...
```

---

## **2. Decoradores com Argumentos**

Podemos criar **decoradores que aceitam argumentos**, tornando-os mais flexíveis.

```python
# Criando um decorador que aceita argumentos

def repetir(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)  # Executa a função N vezes
        return wrapper
    return decorador

# Aplicando o decorador com argumentos
@repetir(3)
def saudacao():
    print("Olá, mundo!")

saudacao()
```

### **Saída:**
```
Olá, mundo!
Olá, mundo!
Olá, mundo!
```

---

## **3. Decoradores em Funções com Retorno**

Se a função decorada retorna um valor, devemos garantir que a função interna (`wrapper`) também o retorne.

```python
# Criando um decorador que modifica o retorno da função

def dobrar_resultado(funcao):
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado * 2  # Multiplica o resultado por 2
    return wrapper

# Aplicando o decorador
@dobrar_resultado

def soma(a, b):
    return a + b

print(soma(3, 5))
```

### **Saída:**
```
16
```

---

## **4. Decoradores em Métodos de Classe**

Podemos aplicar decoradores a **métodos de classes**, modificando seu comportamento.

```python
# Criando um decorador para métodos de classe

def verificar_autenticacao(funcao):
    def wrapper(self, *args, **kwargs):
        if not self.autenticado:
            print("Usuário não autenticado!")
            return
        return funcao(self, *args, **kwargs)
    return wrapper

class Usuario:
    def __init__(self, nome, autenticado=False):
        self.nome = nome
        self.autenticado = autenticado

    @verificar_autenticacao
    def acessar_sistema(self):
        print(f"Bem-vindo, {self.nome}!")

# Criando usuários
usuario1 = Usuario("Alice", autenticado=True)
usuario2 = Usuario("Bob", autenticado=False)

usuario1.acessar_sistema()  # Executa normalmente
usuario2.acessar_sistema()  # Bloqueado pelo decorador
```

### **Saída:**
```
Bem-vindo, Alice!
Usuário não autenticado!
```

---

## **5. Quando Usar Decoradores?**

✅ **Quando há lógica repetitiva antes ou depois de uma função** (exemplo: logging, autenticação).

✅ **Quando é necessário modificar funções sem alterar seu código-fonte.**

❌ **Evite decoradores em funções muito simples**, pois podem tornar o código mais difícil de entender.

Os decoradores são uma ferramenta essencial para escrever código limpo e reutilizável em Python. Eles permitem modificar funções de forma eficiente e flexível, tornando o desenvolvimento mais organizado.
