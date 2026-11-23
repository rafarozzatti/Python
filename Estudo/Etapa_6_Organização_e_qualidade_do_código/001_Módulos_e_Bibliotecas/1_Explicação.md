## **1. O que são módulos?**

Um módulo é um arquivo Python que contém código que pode ser reutilizado em outros programas.

Por exemplo, imagine que temos um arquivo chamado `operacoes.py`:

```
def somar(a, b):    
    return a + b
    
def subtrair(a, b):    
    return a - b
```

Esse arquivo contém duas funções.

Em vez de copiar essas funções para outro programa, podemos importar o módulo e utilizá-las.

## **2. Importando módulos com&#x20;**`import`

Imagine que temos outro arquivo chamado `main.py`.

Podemos importar o módulo assim:

```
import operacoes

resultado = operacoes.somar(10, 5)

print(resultado)
```

Saída:

```
15
```

Observe:

- `import operacoes` importa o módulo.
- `operacoes.somar()` acessa a função `somar` que está dentro dele.
- Não precisamos copiar a função para o arquivo principal.

**Importante:** os dois arquivos precisam estar em um local que permita ao Python encontrá-los. Vamos aprofundar essa organização mais adiante.

## **3. Importando algo específico com&#x20;**`from`

Também podemos importar somente uma função de determinado módulo.

```
from operacoes import somar

resultado = somar(10, 5)

print(resultado)
```

Saída:

```
15
```

A diferença é que não precisamos escrever `operacoes.somar()`. Podemos chamar diretamente `somar()`.

Também podemos importar várias funções:

```
from operacoes import somar, subtrair

print(somar(10, 5))
print(subtrair(10, 5))
```

## **4. Utilizando apelidos com&#x20;**`as`

Podemos criar um apelido para um módulo ou função utilizando `as`.

Exemplo:

```
import operacoes as op

print(op.somar(10, 5))
```

Nesse caso, `op` é o apelido de `operacoes`.

Isso também funciona com funções:

```
from operacoes import somar as adicao

print(adicao(10, 5))
```

O apelido é útil quando queremos utilizar nomes mais curtos ou evitar conflitos entre nomes.

## **5. Bibliotecas padrão do Python**

O Python já possui diversas bibliotecas disponíveis, sem precisar instalar nada.

Vamos estudar três delas.

### **A) Biblioteca&#x20;**`math`

A biblioteca `math` disponibiliza funções matemáticas.

Primeiro, precisamos importá-la:

```
import math
```

Algumas funções importantes:

`math.sqrt()`**&#x20;— Raiz quadrada**

```
import math

resultado = math.sqrt(25)

print(resultado)
```

Saída:

```
5.0
```

`math.ceil()`**&#x20;— Arredondamento para cima**

```
import math

print(math.ceil(4.2))
```

Saída:

```
5
```

`math.floor()`**&#x20;— Arredondamento para baixo**

```
import math

print(math.floor(4.8))
```

Saída:

```
4
```

`math.pi`**&#x20;— Valor de PI**

```
import math

print(math.pi)
```

Saída:

```
3.141592653589793
```

### **B) Biblioteca&#x20;**`random`

A biblioteca `random` permite gerar valores aleatórios.

Importação:

```
import random
```

`random.randint()`**&#x20;— Número inteiro aleatório**

```
import random

numero = random.randint(1, 10)

print(numero)
```

O resultado será um número inteiro entre 1 e 10, incluindo os dois limites.

`random.choice()`**&#x20;— Escolher um elemento aleatório**

```
import random

nomes = ['Carlos', 'Ana', 'Pedro', 'Mariana']

escolhido = random.choice(nomes)

print(escolhido)
```

O Python escolherá aleatoriamente um dos nomes da lista.

`random.random()`**&#x20;— Número decimal aleatório**

```
import random

numero = random.random()

print(numero)
```

Retorna um número decimal maior ou igual a 0 e menor que 1.

### **C) Biblioteca&#x20;**`datetime`

A biblioteca `datetime` permite trabalhar com datas e horários.

Importação:

```
import datetime
```

`datetime.datetime.now()`**&#x20;— Data e horário atuais**

```
import datetime

agora = datetime.datetime.now()

print(agora)
```

O resultado depende da data e do horário em que o programa for executado.

`datetime.date.today()`**&#x20;— Data atual**

```
import datetime

hoje = datetime.date.today()

print(hoje)
```

Exemplo de saída:

```
2026-11-19
```

**Criando uma data específica**

```
import datetime

data = datetime.date(2026, 12, 25)

print(data)
```

Saída:

```
2026-12-25
```

**Formatando datas com&#x20;**`strftime()`

Podemos apresentar uma data em diferentes formatos:

```
import datetime

hoje = datetime.date.today()

data_formatada = hoje.strftime('%d/%m/%Y')

print(data_formatada)
```

Exemplo de saída:

```
19/11/2026
```

Alguns códigos de formatação:

| Código | Significado            |
| ------ | ---------------------- |
| `%d`   | Dia                    |
| `%m`   | Mês                    |
| `%Y`   | Ano com quatro dígitos |
| `%H`   | Hora                   |
| `%M`   | Minuto                 |
| `%S`   | Segundo                |

## **6. Resumo para suas anotações**

| Comando                     | Finalidade                    |
| --------------------------- | ----------------------------- |
| `import modulo`             | Importa um módulo inteiro     |
| `from modulo import funcao` | Importa uma função específica |
| `as`                        | Cria um apelido               |
| `math.sqrt()`               | Calcula raiz quadrada         |
| `math.ceil()`               | Arredonda para cima           |
| `math.floor()`              | Arredonda para baixo          |
| `math.pi`                   | Retorna o valor de PI         |
| `random.randint()`          | Gera inteiro aleatório        |
| `random.choice()`           | Escolhe elemento aleatório    |
| `random.random()`           | Gera decimal aleatório        |
| `datetime.datetime.now()`   | Retorna data e horário atuais |
| `datetime.date.today()`     | Retorna a data atual          |
| `strftime()`                | Formata datas e horários      |
