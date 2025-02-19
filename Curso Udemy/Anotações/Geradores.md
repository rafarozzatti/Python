# Geradores em Python

Os **geradores** são uma forma eficiente de criar iteradores em Python, permitindo a geração de valores sob demanda, sem armazená-los na memória. Eles são definidos utilizando funções que contêm a palavra-chave `yield`.

---

## **1. O que são Geradores?**

Um **gerador** é uma função que pode ser pausada e retomada. Diferente de funções normais, que retornam um valor e encerram, geradores lembram onde pararam e continuam a partir desse ponto.

```python
# Criando um gerador

def meu_gerador():
    yield 1
    yield 2
    yield 3

# Chamando o gerador
meu_gen = meu_gerador()
print(next(meu_gen))  # Saída: 1
print(next(meu_gen))  # Saída: 2
print(next(meu_gen))  # Saída: 3
# print(next(meu_gen))  # StopIteration (fim dos valores)
```

### **Saída:**
```
1
2
3
```

---

## **2. Diferença entre Geradores e Funções Normais**

| Característica   | Função Normal | Gerador |
|-----------------|--------------|---------|
| Retorna valor com `return` | Sim | Não |
| Usa `yield` para gerar valores | Não | Sim |
| Salva estado da execução | Não | Sim |
| Eficiência na memória | Baixa (copia todos os dados) | Alta (gera sob demanda) |

---

## **3. Criando um Gerador para uma Sequência de Números**

```python
# Gerador que cria uma sequência de números até um limite

def sequencia(limite):
    num = 0
    while num < limite:
        yield num
        num += 1

# Testando o gerador
seq = sequencia(5)
for numero in seq:
    print(numero)
```

### **Saída:**
```
0
1
2
3
4
```

---

## **4. Gerador Infinito**

Geradores podem ser usados para criar sequências infinitas sem consumir toda a memória.

```python
# Gerador infinito de números naturais

def infinito():
    num = 0
    while True:
        yield num
        num += 1

# Criando e mostrando os primeiros 5 valores
gen = infinito()
for _ in range(5):
    print(next(gen))
```

### **Saída:**
```
0
1
2
3
4
```

---

## **5. Uso de `yield from` para Sub-Geradores**

Quando um gerador precisa chamar outro gerador, usamos `yield from`.

```python
# Gerador principal chamando outro gerador

def sub_gerador():
    yield 1
    yield 2

def gerador_principal():
    yield from sub_gerador()
    yield 3

# Testando o gerador
for valor in gerador_principal():
    print(valor)
```

### **Saída:**
```
1
2
3
```

---

## **6. Quando Usar Geradores?**

✅ Quando precisar lidar com grandes volumes de dados sem carregar tudo na memória.

✅ Quando quiser criar fluxos de dados infinitos ou sob demanda.

✅ Para otimizar o desempenho em operações que podem ser pausadas e retomadas.

❌ Não use geradores quando precisar acessar os dados várias vezes, pois eles são consumidos uma única vez.

---

Os geradores são poderosas ferramentas para otimização de código, permitindo manipular grandes quantidades de dados de forma eficiente e econômica. Com essa abordagem, você melhora a performance e reduz o uso de memória desnecessária!
