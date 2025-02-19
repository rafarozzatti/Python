# Iteradores e Iteráveis em Python

Em Python, **iteráveis** e **iteradores** são conceitos fundamentais para manipulação de sequências de dados. Eles são amplamente utilizados em estruturas de laço (`for`), compreensões de listas e funções que manipulam coleções.

---

## **1. O que são Iteráveis?**

Um **iterável** é qualquer objeto que pode ser percorrido em um loop (`for`). Exemplos comuns são listas, tuplas, dicionários, conjuntos e strings.

```python
# Exemplo de iteráveis
lista = [1, 2, 3, 4]
tupla = (10, 20, 30)
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto = {100, 200, 300}
string = "Python"
```

Saída:
```
Lista: [1, 2, 3, 4]
Tupla: (10, 20, 30)
Dicionário: {'a': 1, 'b': 2, 'c': 3}
Conjunto: {100, 200, 300}
String: Python
```

Esses objetos possuem um **método especial** chamado `__iter__()`, que os torna iteráveis.

---

## **2. O que são Iteradores?**

Um **iterador** é um objeto que sabe como percorrer um iterável. Ele tem um método especial chamado `__next__()`, que retorna o próximo elemento da sequência.

Para transformar um iterável em um iterador, usamos a função `iter()`, e para obter os elementos um por um, usamos `next()`.

```python
# Transformando um iterável em um iterador
lista = [1, 2, 3]
iterador = iter(lista)  # Criando um iterador

print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
```

Saída:
```
1
2
3
```

Se chamarmos `next(iterador)` novamente, teremos um erro `StopIteration`, pois os elementos já foram consumidos.

---

## **3. Diferença entre Iteráveis e Iteradores**

| Característica                               | Iterável | Iterador |
| -------------------------------------------- | -------- | -------- |
| Possui `__iter__()`                          | Sim      | Sim      |
| Possui `__next__()`                          | Não      | Sim      |
| Pode ser percorrido com `for`                | Sim      | Sim      |
| Pode ser convertido em iterador com `iter()` | Sim      | -        |
| Retorna um valor com `next()`                | Não      | Sim      |

---

## **4. Criando um Iterador Personalizado**

Podemos criar nossos próprios iteradores definindo uma classe com os métodos `__iter__()` e `__next__()`.

```python
# Criando um iterador que conta até um limite
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0
    
    def __iter__(self):
        return self  # Retorna o próprio objeto como iterador
    
    def __next__(self):
        if self.atual < self.limite:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration  # Interrompe a iteração

# Testando o iterador
contador = Contador(3)
for num in contador:
    print(num)
```

Saída:
```
0
1
2
```

---

## **5. Convertendo Iteradores em Listas**

Podemos converter iteradores em listas usando `list()`, o que consome todos os elementos do iterador.

```python
# Criando um iterador
iterador = iter(range(5))

# Convertendo para lista
lista = list(iterador)
print(lista)
```

Saída:
```
[0, 1, 2, 3, 4]
```

---

## **6. Quando Usar Iteradores e Iteráveis?**

✅ Use **iteráveis** quando precisar armazenar e acessar coleções de dados.

✅ Use **iteradores** quando precisar percorrer grandes volumes de dados sem carregar tudo na memória ao mesmo tempo.

❌ Evite criar iteradores quando precisar acessar os elementos múltiplas vezes, pois iteradores são consumidos após a primeira passagem.

---

Os conceitos de iteráveis e iteradores são essenciais para a manipulação eficiente de sequências em Python. Compreendê-los ajuda a escrever códigos mais otimizados e a utilizar melhor recursos como `for`, `map`, `filter` e `zip`.
