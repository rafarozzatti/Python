# Getters e Setters em Programação Orientada a Objetos (POO)

Os **getters** e **setters** são métodos utilizados para acessar e modificar atributos privados em uma classe. Eles ajudam a manter o princípio de **encapsulamento**, protegendo os dados e garantindo que qualquer modificação seja feita de maneira controlada.

---

## **1. Atributos Privados**

Em Python, utilizamos um **underscore duplo (`__`)** para indicar que um atributo deve ser tratado como privado.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

pessoa = Pessoa("Carlos", 30)
print(pessoa.__nome)  # Erro! O atributo é privado
```

### **Saída:**
```
AttributeError: 'Pessoa' object has no attribute '__nome'
```

Como o atributo `__nome` está definido como **privado**, ele não pode ser acessado diretamente de fora da classe. Para contornar isso, utilizamos **getters e setters**.

---

## **2. Getters (Métodos para Obter Valores)**

Os **getters** permitem acessar atributos privados de forma segura.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    def get_nome(self):
        return self.__nome  # Retorna o nome
    
    def get_idade(self):
        return self.__idade  # Retorna a idade

pessoa = Pessoa("Carlos", 30)
print(pessoa.get_nome())  # Obtendo o nome
print(pessoa.get_idade())  # Obtendo a idade
```

### **Saída:**
```
Carlos
30
```

---

## **3. Setters (Métodos para Modificar Valores)**

Os **setters** permitem modificar atributos privados, garantindo que as alterações sejam validadas antes de serem aplicadas.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    def get_nome(self):
        return self.__nome  # Retorna o nome

    def get_idade(self):
        return self.__idade  # Retorna a idade
    
    def set_idade(self, nova_idade):
        if nova_idade > 0:  # Validação para idade positiva
            self.__idade = nova_idade
        else:
            print("Idade inválida!")  # Mensagem de erro caso a idade seja negativa

pessoa = Pessoa("Carlos", 30)
pessoa.set_idade(35)  # Modificando a idade
print(pessoa.get_idade())  # Obtendo a idade modificada

pessoa.set_idade(-5)  # Tentativa inválida de alteração
```

### **Saída:**
```
35
Idade inválida!
```

---

## **4. Uso de `@property` para Criar Getters e Setters em Python**

Em Python, podemos utilizar **decoradores** para criar getters e setters de forma mais elegante.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    @property
    def nome(self):
        return self.__nome  # Retorna o nome como propriedade
    
    @property
    def idade(self):
        return self.__idade  # Retorna a idade como propriedade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade  # Modifica a idade se for válida
        else:
            print("Idade inválida!")  # Mensagem de erro caso a idade seja negativa

pessoa = Pessoa("Carlos", 30)
print(pessoa.nome)  # Acesso direto ao atributo como propriedade

pessoa.idade = 35  # Modificando a idade diretamente
print(pessoa.idade)  # Obtendo a idade modificada

pessoa.idade = -5  # Tentativa inválida de alteração
```

### **Saída:**
```
Carlos
35
Idade inválida!
```

---

## **5. Quando Usar Getters e Setters?**

✅ **Use getters e setters quando:**
- Precisa controlar o acesso aos atributos de uma classe.
- Quer validar ou processar dados antes de modificá-los.
- Deseja seguir o princípio do **encapsulamento**.

❌ **Não é necessário usar getters e setters quando:**
- O atributo pode ser acessado diretamente sem necessidade de validação.
- A classe é muito simples e não exige proteção extra.

---
