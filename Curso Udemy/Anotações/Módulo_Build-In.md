# Módulos Built-In do Python

O Python possui vários módulos embutidos (Built-In), que oferecem funcionalidades essenciais sem precisar instalar pacotes adicionais. Esses módulos agilizam o desenvolvimento e são amplamente utilizados em diversas aplicações.

## 1. `math` - Funções matemáticas
O módulo `math` fornece funções matemáticas avançadas, como trigonometria, logaritmos e operações de arredondamento.

```python
import math

# Calcula a raiz quadrada de um número
print(math.sqrt(25))  # Saída: 5.0

# Arredonda um número para baixo
print(math.floor(3.9))  # Saída: 3
```

**Quando usar?** Quando precisar realizar operações matemáticas avançadas.

---

## 2. `random` - Geração de números aleatórios
O `random` permite gerar valores aleatórios para testes, simulações ou jogos.

```python
import random

# Gera um número aleatório entre 1 e 10
print(random.randint(1, 10))

# Escolhe um elemento aleatório de uma lista
print(random.choice(['maçã', 'banana', 'uva']))
```

**Quando usar?** Quando precisar de aleatoriedade em um programa.

---

## 3. `datetime` - Manipulação de datas e horas
O `datetime` permite trabalhar com datas e horários de forma precisa.

```python
from datetime import datetime

# Obtém a data e hora atual
agora = datetime.now()
print(agora)

# Formata uma data em string
print(agora.strftime('%d/%m/%Y %H:%M:%S'))
```

**Quando usar?** Para lidar com datas e horários, como registros de logs e eventos.

---

## 4. `os` - Interação com o sistema operacional
O `os` permite acessar funcionalidades do sistema, como arquivos e variáveis de ambiente.

```python
import os

# Lista arquivos do diretório atual
print(os.listdir('.'))

# Obtém o diretório atual
print(os.getcwd())
```

**Quando usar?** Para manipular arquivos e diretórios dinamicamente.

---

## 5. `sys` - Informações sobre o interpretador Python
O `sys` fornece detalhes sobre a versão do Python, argumentos passados e saída do programa.

```python
import sys

# Exibe a versão do Python
print(sys.version)
```

**Quando usar?** Para obter informações do ambiente de execução e interagir com argumentos de linha de comando.

---

## 6. `json` - Manipulação de dados JSON
O `json` permite converter dados entre JSON e dicionários Python.

```python
import json

# Converte um dicionário para JSON
dados = {'nome': 'Alice', 'idade': 25}
json_string = json.dumps(dados)
print(json_string)

# Converte JSON para dicionário
novo_dados = json.loads(json_string)
print(novo_dados['nome'])
```

**Quando usar?** Quando precisar trabalhar com APIs ou armazenar dados estruturados.

---

## 7. `time` - Controle de tempo e pausas
O `time` permite trabalhar com pausas e medição de tempo.

```python
import time

# Espera 2 segundos antes de continuar
print("Iniciando...")
time.sleep(2)
print("Finalizado!")
```

**Quando usar?** Para medir desempenho ou criar atrasos programados.

---

## 8. `collections` - Estruturas de dados avançadas
O `collections` expande as estruturas de dados padrão do Python.

```python
from collections import Counter

# Conta ocorrências de elementos em uma lista
lista = ['a', 'b', 'a', 'c', 'b', 'a']
contagem = Counter(lista)
print(contagem)
```

**Quando usar?** Quando precisar de contadores, filas e dicionários ordenados.

---

## 9. `itertools` - Ferramentas para manipular iteradores
O `itertools` facilita a manipulação de sequências e repetições.

```python
from itertools import permutations

# Gera todas as permutações de uma lista
print(list(permutations([1, 2, 3])))
```

**Quando usar?** Para trabalhar com combinações e repetições eficientes.

---

## Conclusão
Os módulos Built-In do Python ajudam a tornar o desenvolvimento mais eficiente, evitando a necessidade de reescrever funções comuns. Dependendo do problema, utilizar esses módulos pode reduzir a complexidade e melhorar a performance do código!
