# ** Organização de arquivos e pastas**

Até agora, trabalhamos principalmente com programas em um único arquivo `.py`.

Por exemplo:

**meu_projeto/**

`programa.py`

Isso funciona bem para programas pequenos.

Porém, quando um projeto cresce, colocar todas as funções, cálculos e operações no mesmo arquivo pode dificultar a leitura e a manutenção.

Uma solução é dividir o projeto em arquivos com responsabilidades diferentes.

**Exemplo:**

**sistema_vendas/**

`main.py`

Arquivo principal

`produtos.py`

Funções relacionadas aos produtos

`vendas.py`

Funções relacionadas às vendas

`dados.csv`

Arquivo com dados

Cada arquivo possui uma responsabilidade, facilitando a organização.

# **2. Criando módulos próprios**

Lembra que estudamos módulos e importações no Assunto 1?

Agora vamos aplicar esse conhecimento criando nossos próprios módulos em arquivos diferentes.

Um módulo próprio é simplesmente um arquivo Python (`.py`) que contém código reutilizável.

Imagine que temos dois arquivos:

**Arquivo&#x20;**`operacoes.py`**:**

```
def somar(a, b):    
    return a + b
    
def subtrair(a, b):    
    return a - b
```

Esse arquivo contém duas funções relacionadas a operações matemáticas.

**Arquivo&#x20;**`main.py`**:**

```
import operacoes

resultado = operacoes.somar(10, 5)

print(resultado)
```

Resultado:

```
15
```

O `main.py` importa o módulo `operacoes.py` e utiliza suas funções.

Isso permite separar as funcionalidades sem precisar escrever tudo novamente.

# **3. Importando funções específicas entre arquivos**

Também podemos importar somente as funções que precisamos.

Continuando o exemplo anterior:

**Arquivo&#x20;**`main.py`**:**

```
from operacoes import somar

resultado = somar(10, 5)

print(resultado)
```

Observe a diferença:

| Forma                         | Como utilizar       |
| ----------------------------- | ------------------- |
| `import operacoes`            | `operacoes.somar()` |
| `from operacoes import somar` | `somar()`           |

Também podemos importar várias funções:

```
from operacoes import somar, subtrair

print(somar(10, 5))
print(subtrair(10, 5))
```

# **4. Criando pastas para organizar módulos**

Quando o projeto possui muitos arquivos, podemos separá-los em pastas.

Por exemplo:

**sistema_vendas/**

`main.py`

**funcoes/**

`produtos.py`

`vendas.py`

`__init__.py`

Arquivo de inicialização do pacote

Nesse exemplo:

- `main.py`: arquivo principal do programa.
- `funcoes/`: pasta que reúne funcionalidades.
- `produtos.py`: funções relacionadas aos produtos.
- `vendas.py`: funções relacionadas às vendas.
- `__init__.py`: permite tratar a pasta como um pacote Python tradicional e pode conter código de inicialização.

Para importar uma função de `produtos.py` a partir de `main.py`, podemos utilizar:

```
from funcoes.produtos import cadastrar_produto
```

O ponto (`.`) indica que estamos acessando um módulo dentro de uma pasta.

**Observação:** nas versões modernas do Python, também existem pacotes sem `__init__.py`, chamados de pacotes de namespace. Mas, neste momento, vamos trabalhar com a estrutura tradicional.

# **5. Organização de um projeto na prática**

Vamos imaginar um pequeno sistema de vendas.

Uma organização possível seria:

**controle_vendas/**

`main.py`

**funcoes/**

`clientes.py`

`produtos.py`

`vendas.py`

`__init__.py`

**dados/**

`vendas.csv`

Cada parte tem uma função:

| Arquivo/pasta | Responsabilidade              |
| ------------- | ----------------------------- |
| `main.py`     | Executar o programa principal |
| `clientes.py` | Operações com clientes        |
| `produtos.py` | Operações com produtos        |
| `vendas.py`   | Operações com vendas          |
| `dados/`      | Armazenar arquivos de dados   |

Essa organização facilita encontrar, modificar e reutilizar o código.

# **6. Boas práticas de organização**

Algumas recomendações importantes:

- Utilize nomes claros para arquivos, funções e pastas.
- Evite colocar todas as funcionalidades em um único arquivo.
- Separe funções de acordo com suas responsabilidades.
- Evite repetir código desnecessariamente.
- Mantenha os arquivos relacionados próximos.
- Utilize nomes em letras minúsculas e separe palavras com `_`, como `controle_vendas.py`.

## **Resumo do assunto**

| Conceito          | Significado                                       |
| ----------------- | ------------------------------------------------- |
| Arquivo `.py`     | Arquivo que contém código Python                  |
| Módulo            | Arquivo Python que pode ser importado             |
| Pacote            | Estrutura que organiza módulos em diretórios      |
| `import`          | Importa um módulo                                 |
| `from ... import` | Importa elementos específicos                     |
| `__init__.py`     | Arquivo de inicialização de um pacote tradicional |
| `main.py`         | Geralmente, arquivo principal do projeto          |
